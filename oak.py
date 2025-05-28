import cv2
import depthai as dai
import numpy as np

roiCamObject = [0, 0, 0, 0]
distanceCamObject = [0, 0, 0]

roiCamObject2 = [0, 0, 0, 0]
distanceCamObject2 = [0, 0, 0]

def oak_init():
	# Create a pipeline
	pipeline = dai.Pipeline()

	# Define the source and output for color
	cam_rgb = pipeline.create(dai.node.ColorCamera)
	xout_video = pipeline.create(dai.node.XLinkOut)
	xout_video.setStreamName("video")

	#Define the source and output for depth
	monoLeft = pipeline.create(dai.node.MonoCamera)
	monoRight = pipeline.create(dai.node.MonoCamera)
	stereo = pipeline.create(dai.node.StereoDepth)
	spatialLocationCalculator = pipeline.create(dai.node.SpatialLocationCalculator)
	xoutDepth = pipeline.create(dai.node.XLinkOut)
	xoutSpatialData = pipeline.create(dai.node.XLinkOut)
	xinSpatialCalcConfig = pipeline.create(dai.node.XLinkIn)
	xoutDepth.setStreamName("depth")
	xoutSpatialData.setStreamName("spatialData")
	xinSpatialCalcConfig.setStreamName("spatialCalcConfig")

	# Camera properties for color
	cam_rgb.setPreviewSize(640, 480)
	cam_rgb.setInterleaved(False)
	cam_rgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

	# Camera properties for depth
	monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
	monoLeft.setCamera("left")
	monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
	monoRight.setCamera("right")

	# multiple streams so no blocking
	xout_video.input.setBlocking(False)
	xout_video.input.setQueueSize(1)

	#Settings for stereo depth
	stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
	stereo.setLeftRightCheck(True)
	stereo.setSubpixel(True)
	stereo.setExtendedDisparity(False)

	#config for depth //See https://docs.luxonis.com/hardware/platform/depth/configuring-stereo-depth
	config = dai.SpatialLocationCalculatorConfigData()
	config.depthThresholds.lowerThreshold = 100
	config.depthThresholds.upperThreshold = 10000
	calculationAlgorithm = dai.SpatialLocationCalculatorAlgorithm.MEDIAN

	# # use a region of interest for finding the distance for a specific part of the image
	# topLeft = dai.Point2f(0.4, 0.4)
	# bottomRight = dai.Point2f(0.6, 0.6)
	# config.roi = dai.Rect(topLeft, bottomRight)

	spatialLocationCalculator.inputConfig.setWaitForMessage(False)
	spatialLocationCalculator.initialConfig.addROI(config)

	# Link the camera output to the XLink output for color
	cam_rgb.preview.link(xout_video.input)

	#link the mono channels to the stereo depth
	monoLeft.out.link(stereo.left)
	monoRight.out.link(stereo.right)

	spatialLocationCalculator.passthroughDepth.link(xoutDepth.input)
	stereo.depth.link(spatialLocationCalculator.inputDepth)

	spatialLocationCalculator.out.link(xoutSpatialData.input)
	xinSpatialCalcConfig.out.link(spatialLocationCalculator.inputConfig)

	return dai.Device(pipeline)

# Function for bounding box
def getBoundingBox(img, rects, depthFrameColor):
	center = None
	corners = None

	for x, y, w, h in rects:
		corners = [(x, y), (x + w, y), (x, y + h), (x + w, y + h)]
		center = (x + w // 2, (y + h // 2) - 20)
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

		if center is not None:
			cv2.circle(depthFrameColor, center, 5, (255, 0, 0), -1)
			cv2.circle(img, center, 5, (255, 0, 0), -1)

	return center, corners

# Function for depth in roi
def depth_of_roi(depthFrameColor, spatialData, corners, center, spatialCalcConfigInQueue, window_name):
	if window_name == "main":
		
		global distanceCamObject
		global roiCamObject

		for depthData in spatialData:
			if corners is not None:
				# new roi and update the config -> keep measure roi small for higher accuracy
				newRectangle = (int(center[0] - 10), int(center[1] - 10), 20, 20)

				config = dai.SpatialLocationCalculatorConfigData()

				config.roi = dai.Rect(newRectangle[0], newRectangle[1], newRectangle[2], newRectangle[3])
				cfg = dai.SpatialLocationCalculatorConfig()
				cfg.addROI(config)
				spatialCalcConfigInQueue.send(cfg)

				roi = depthData.config.roi
				roi = roi.denormalize(width=depthFrameColor.shape[1], height=depthFrameColor.shape[0])
				xmin = int(roi.topLeft().x)
				ymin = int(roi.topLeft().y)
				xmax = int(roi.bottomRight().x)
				ymax = int(roi.bottomRight().y)

				roiCamObject.clear()
				roiCamObject.append(xmin)
				roiCamObject.append(ymin)
				roiCamObject.append(xmax)
				roiCamObject.append(ymax)

				if not (int(depthData.spatialCoordinates.x) == 0 and int(depthData.spatialCoordinates.y) == 0 and int(depthData.spatialCoordinates.z) == 0):
					#print(int(depthData.spatialCoordinates.x))
					#print(int(depthData.spatialCoordinates.y))
					#print(int(depthData.spatialCoordinates.z))
					#print(" ")

					distanceCamObject.clear()
					distanceCamObject.append(int(depthData.spatialCoordinates.x))
					distanceCamObject.append(int(depthData.spatialCoordinates.y))
					distanceCamObject.append(int(depthData.spatialCoordinates.z))

					roiCamObject.clear()
					roiCamObject.append(xmin)
					roiCamObject.append(ymin)
					roiCamObject.append(xmax)
					roiCamObject.append(ymax)

				printColor = (255, 255, 255)
				fontType = cv2.FONT_HERSHEY_TRIPLEX
				cv2.rectangle(depthFrameColor, (xmin, ymin), (xmax, ymax), printColor, 1)
				cv2.putText(depthFrameColor, f"X: {int(depthData.spatialCoordinates.x)} mm", (xmin + 10, ymin + 50), fontType, 0.5, printColor)
				cv2.putText(depthFrameColor, f"Y: {int(depthData.spatialCoordinates.y)} mm", (xmin + 10, ymin + 65), fontType, 0.5, printColor)
				cv2.putText(depthFrameColor, f"Z: {int(depthData.spatialCoordinates.z)} mm", (xmin + 10, ymin + 80), fontType, 0.5, printColor)

		return depthData, depthFrameColor
	elif window_name == "additional":
		global distanceCamObject2
		global roiCamObject2

		for depthData in spatialData:
			if corners is not None:
				# new roi and update the config -> keep measure roi small for higher accuracy
				newRectangle = (int(center[0] - 10), int(center[1] - 10), 20, 20)

				config = dai.SpatialLocationCalculatorConfigData()

				config.roi = dai.Rect(newRectangle[0], newRectangle[1], newRectangle[2], newRectangle[3])
				cfg = dai.SpatialLocationCalculatorConfig()
				cfg.addROI(config)
				spatialCalcConfigInQueue.send(cfg)

				roi = depthData.config.roi
				roi = roi.denormalize(width=depthFrameColor.shape[1], height=depthFrameColor.shape[0])
				xmin = int(roi.topLeft().x)
				ymin = int(roi.topLeft().y)
				xmax = int(roi.bottomRight().x)
				ymax = int(roi.bottomRight().y)

				roiCamObject2.clear()
				roiCamObject2.append(xmin)
				roiCamObject2.append(ymin)
				roiCamObject2.append(xmax)
				roiCamObject2.append(ymax)

				if not (int(depthData.spatialCoordinates.x) == 0 and int(depthData.spatialCoordinates.y) == 0 and int(depthData.spatialCoordinates.z) == 0):
					#print(int(depthData.spatialCoordinates.x))
					#print(int(depthData.spatialCoordinates.y))
					#print(int(depthData.spatialCoordinates.z))
					#print(" ")

					distanceCamObject2.clear()
					distanceCamObject2.append(int(depthData.spatialCoordinates.x))
					distanceCamObject2.append(int(depthData.spatialCoordinates.y))
					distanceCamObject2.append(int(depthData.spatialCoordinates.z))

					roiCamObject2.clear()
					roiCamObject2.append(xmin)
					roiCamObject2.append(ymin)
					roiCamObject2.append(xmax)
					roiCamObject2.append(ymax)

				printColor = (255, 255, 255)
				fontType = cv2.FONT_HERSHEY_TRIPLEX
				cv2.rectangle(depthFrameColor, (xmin, ymin), (xmax, ymax), printColor, 1)
				cv2.putText(depthFrameColor, f"X: {int(depthData.spatialCoordinates.x)} mm", (xmin + 10, ymin + 50), fontType, 0.5, printColor)
				cv2.putText(depthFrameColor, f"Y: {int(depthData.spatialCoordinates.y)} mm", (xmin + 10, ymin + 65), fontType, 0.5, printColor)
				cv2.putText(depthFrameColor, f"Z: {int(depthData.spatialCoordinates.z)} mm", (xmin + 10, ymin + 80), fontType, 0.5, printColor)

		return depthData, depthFrameColor