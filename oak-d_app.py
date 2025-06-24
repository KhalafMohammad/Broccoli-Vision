import time 
import cv2
import depthai as dai
import numpy as np
from math import atan2, cos, sin, sqrt, pi
import angle

import hsv
import thresh
import contour
import oak

import anglecalc

import queue
import threading
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def start_client(coordinateQueue):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		while True:
			try:
				s.connect((HOST, PORT))
				# message = "Hallo van de client!"
				while True:
					if coordinateQueue.qsize != 0:
						message = coordinateQueue.get()
					# message = "test"
						s.sendall(message.encode())
					# data = s.recv(1024)
					# print(f"Antwoord van server: {data.decode()}")
			except:
				pass

vision_algorithm = []
iThreshFirstTime = True

# Independent state for the additional window
vision_algorithm_additional = []
iThreshFirstTime2 = True

RETRIEVE_DEPTH_ADDITIONAL = False
RETRIEVE_DEPTH = False

object_area_stam = 0
object_area_kop = 0

x1 = 0
y1 = 0
y2 = 0
x2 = 0


last_command_add_time = 0
last_command_sing_len = 0

last_captrue_time = time.time()
def destroy(window_name):
	cv2.destroyWindow(window_name)
	cv2.namedWindow(window_name)

	hsv.HSV_ENABLED = False
	hsv.HSV_ENABLED2 = False
	thresh.THRESH_ENABLED = False
	contour.CONTOURS_ENABLED = False
	contour.CONTOURS_ENABLED2 = False
	thresh.iThreshFirstTime = True

def assemble(window_name): # for main window
	global vision_algorithm
	if window_name == 'main':
		if hsv.HSV_ENABLED:
			vision_algorithm.append(['HSV', hsv.HSV_settings])
		elif thresh.THRESH_ENABLED:
			vision_algorithm.append(['THRESH', thresh.THRESH_settings])
		elif contour.CONTOURS_ENABLED:
			vision_algorithm.append(['CONTOUR', contour.CONTOUR_settings])
			contour.CONTOURS_ENABLED = False
		print(len(vision_algorithm))

	elif window_name == 'additional': # for additional window
		global vision_algorithm_additional
		if hsv.HSV_ENABLED2:
			vision_algorithm_additional.append(['HSV', hsv.HSV_settings2])
		elif thresh.THRESH_ENABLED2:
			vision_algorithm_additional.append(['THRESH', thresh.THRESH_settings])
		elif contour.CONTOURS_ENABLED2:
			vision_algorithm_additional.append(['CONTOUR', contour.CONTOUR_settings2])
			contour.CONTOURS_ENABLED2 = False
		print(len(vision_algorithm_additional))


def disassemble():
	global vision_algorithm
	global vision_algorithm_additional

	vision_algorithm.clear()
	vision_algorithm_additional.clear()

def execute(img, depthimg, spatiald,spatialciq, window_name):
	if window_name == 'main':
		global vision_algorithm
		global iThreshFirstTime
		global RETRIEVE_DEPTH

		for x in vision_algorithm:
			if x[0] == 'HSV':
				#print(x[1])
				img = hsv.execute_hsv(img, x[1])
			elif x[0] == 'THRESH':
				#print(x[1])
				img = thresh.execute_thresh(img, x[1])

				if iThreshFirstTime:
					cv2.destroyWindow(root_window)
					cv2.namedWindow(root_window)
					iThreshFirstTime = False
			elif x[0] == 'CONTOUR' and not RETRIEVE_DEPTH:
				#print('Contour')
				img = contour.execute_contour(img, x[1])

		if RETRIEVE_DEPTH:# and not len(contour.bounding_rects) == 0:
			# get contours
			img, x1g,y1g = contour.getContours(img)

			# yes, get coordinates and show in depth image
			center, corners = oak.getBoundingBox(img, contour.bounding_rects, depthimg)
			depthData, depthFrameColor = oak.depth_of_roi(depthimg, spatiald, corners, center, spatialciq, 'main')


			printColor = (255, 255, 255)
			fontType = cv2.FONT_HERSHEY_TRIPLEX

			cv2.rectangle(img, (oak.roiCamObject[0], oak.roiCamObject[1]), (oak.roiCamObject[2], oak.roiCamObject[3]), printColor, 1)
			cv2.putText(img, f"X: {oak.distanceCamObject[0]} mm", (oak.roiCamObject[0] + 10, oak.roiCamObject[1] + 50), fontType, 0.5, printColor)
			cv2.putText(img, f"Y: {oak.distanceCamObject[1]} mm", (oak.roiCamObject[0] + 10, oak.roiCamObject[1] + 65), fontType, 0.5, printColor)
			cv2.putText(img, f"Z: {oak.distanceCamObject[2]} mm", (oak.roiCamObject[0] + 10, oak.roiCamObject[1] + 80), fontType, 0.5, printColor)

			
		return img
	elif window_name == 'additional':
		global vision_algorithm_additional
		global iThreshFirstTime2
		global RETRIEVE_DEPTH_ADDITIONAL

		for x in vision_algorithm_additional:
			if x[0] == 'HSV':
				img = hsv.execute_hsv(img, x[1])
			elif x[0] == 'THRESH':
				img = thresh.execute_thresh(img, x[1])
				if iThreshFirstTime2:
					cv2.destroyWindow(additional_window)
					cv2.namedWindow(additional_window)
					iThreshFirstTime2 = False
			elif x[0] == 'CONTOUR' and not RETRIEVE_DEPTH_ADDITIONAL:
				img = contour.execute_contour(img, x[1])

		if RETRIEVE_DEPTH_ADDITIONAL:
			img, x2g,y2g = contour.getContours(img)
			center, corners = oak.getBoundingBox(img, contour.bounding_rects, depthimg)
			depthData, depthFrameColor = oak.depth_of_roi(depthimg, spatiald, corners, center, spatialciq, 'additional')

			printColor = (255, 255, 255)
			fontType = cv2.FONT_HERSHEY_TRIPLEX

			cv2.rectangle(img, (oak.roiCamObject2[0], oak.roiCamObject2[1]), (oak.roiCamObject2[2], oak.roiCamObject2[3]), printColor, 1)
			cv2.putText(img, f"X: {oak.distanceCamObject2[0]} mm", (oak.roiCamObject2[0] + 10, oak.roiCamObject2[1] + 50), fontType, 0.5, printColor)
			cv2.putText(img, f"Y: {oak.distanceCamObject2[1]} mm", (oak.roiCamObject2[0] + 10, oak.roiCamObject2[1] + 65), fontType, 0.5, printColor)
			cv2.putText(img, f"Z: {oak.distanceCamObject2[2]} mm", (oak.roiCamObject2[0] + 10, oak.roiCamObject2[1] + 80), fontType, 0.5, printColor)

		return img



# def main():
coordinateQueue = queue.Queue()
coordinateThread = threading.Thread(target=start_client, args=(coordinateQueue,), daemon=True)
coordinateThread.start()
# coordinateQueue.

# name root window
root_window = "main"
cv2.namedWindow(root_window)

# Create a second window
additional_window = "additional"
cv2.namedWindow(additional_window)
av_angle = []
command_sing = []
command_sing_flag = False
with oak.oak_init() as device:
	

	
	# Get the output queue
	q_video = device.getOutputQueue(name="video", maxSize=4, blocking=False)
	frame_count = 0

	#init the config and corners
	newConfig = False
	center = None
	corners = None

	# Output queue will be used to get the depth frames from the outputs defined above
	depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)
	spatialCalcQueue = device.getOutputQueue(name="spatialData", maxSize=4, blocking=False)
	spatialCalcConfigInQueue = device.getInputQueue("spatialCalcConfig")
	video = device.getOutputQueue(name="video", maxSize=4, blocking=False)

	while True:
		# retrieve depth data
		inDepth = depthQueue.get()  # Blocking call, will wait until a new data has arrived
		depthFrame = inDepth.getFrame()  # depthFrame values are in millimeters

		depth_downscaled = depthFrame[::4]
		if np.all(depth_downscaled == 0):
			min_depth = 0  # Set a default minimum depth value when all elements are 0
		else:
			# clear the array with previously found contours
			contour.bounding_rects.clear()

			# retrieve min and max depth and generate depth color frame
			min_depth = np.percentile(depth_downscaled[depth_downscaled != 0], 1)
			max_depth = np.percentile(depth_downscaled, 99)
			depthFrameColor = np.interp(depthFrame, (min_depth, max_depth), (0, 255)).astype(np.uint8)
			depthFrameColor = cv2.applyColorMap(depthFrameColor, cv2.COLORMAP_HSV)

			# retrieve the spatial data
			spatialData = spatialCalcQueue.get().getSpatialLocations()

			# start timer every 0.5 seconds to get a frame for stable processing
			# this is needed to prevent the camera from capturing too fast and causing a lag in the processing
			# the camera is capturing at 30 fps, so we need to wait 0.5 seconds to get a new frame
			# this is not needed for the depth image, because it is already captured at 30 fps
		
			CurrentTime = time.time()
			if (CurrentTime - last_captrue_time) >= 0.0:
			# Get the next frame from the color camera
				in_video = q_video.get()
				frame = in_video.getCvFrame()
				frame2 = in_video.getCvFrame()
			
				last_captrue_time = CurrentTime
			
			# in_video = q_video.get()
			# frame = in_video.getCvFrame()
			# frame2 = in_video.getCvFrame()

			# if the camera is mounted up-side-down 180 degrees rotation is needed
			#frame = cv2.rotate(frame, cv2.ROTATE_180)

			# have vision operators been added to the algorithm? additional window
			if not len(vision_algorithm_additional) == 0:
				# execute the vision algorithm that is stored now
				src_executea = execute(frame2,depthFrameColor,spatialData,spatialCalcConfigInQueue, 'additional')

				if hsv.HSV_ENABLED2:
					# show hsv image
					src_hsva = hsv.toHSV(src_executea, 'additional')
					cv2.imshow(additional_window, src_hsva)
				elif thresh.THRESH_ENABLED2:
					# show thresh image
					src_thra = thresh.toThresh(src_executea)
					#print(src_thr.shape)
					cv2.imshow(additional_window, src_thra)
				elif contour.CONTOURS_ENABLED2:
					# show contours image
					src_cnta, x2,y2, object_area_stam = contour.getContours(src_executea)

					# are there contours with a bounding rectangle?
					if not len(contour.bounding_rects) == 0:
						# yes, get coordinates and show in depth image
						center, corners = oak.getBoundingBox(frame2, contour.bounding_rects, depthFrameColor)
						depthData2, depthFrameColor = oak.depth_of_roi(depthFrameColor, spatialData, corners, center, spatialCalcConfigInQueue, 'additional')

					cv2.imshow(additional_window, src_cnta)
				else:
					# show original image
					cv2.imshow(additional_window, src_executea)
			else:
				if hsv.HSV_ENABLED2:
					# show hsv image
					src_hsva = hsv.toHSV(frame2, 'additional')
					cv2.imshow(additional_window, src_hsva)
				elif thresh.THRESH_ENABLED:
					# show thresh image
					src_thra = thresh.toThresh(frame2)
					cv2.imshow(additional_window, src_thra)
				# elif contour.CONTOURS_ENABLED2:
				# 	# show contours image
				# 	src_contoursa = contour.getContours(frame2)
				# 	cv2.imshow(root_window, src_contoursa)
				else:
					# show original image
					cv2.imshow(additional_window, frame2)
			
			
			# have vision operators been added to the algorithm? main window
			if not len(vision_algorithm) == 0:
				# execute the vision algorithm that is stored now
				src_execute = execute(frame,depthFrameColor,spatialData,spatialCalcConfigInQueue, 'main')

				if hsv.HSV_ENABLED:
					# show hsv image
					src_hsv = hsv.toHSV(src_execute, 'main')
					cv2.imshow(root_window, src_hsv)
				elif thresh.THRESH_ENABLED:
					# show thresh image
					src_thr = thresh.toThresh(src_execute)
					#print(src_thr.shape)
					cv2.imshow(root_window, src_thr)
				elif contour.CONTOURS_ENABLED:
					# show contours image
					src_cnt, x1,y1, object_area_kop = contour.getContours(src_execute)

					# are there contours with a bounding rectangle?
					if not len(contour.bounding_rects) == 0:
						# yes, get coordinates and show in depth image
						center, corners = oak.getBoundingBox(frame, contour.bounding_rects, depthFrameColor)
						depthData, depthFrameColor = oak.depth_of_roi(depthFrameColor, spatialData, corners, center, spatialCalcConfigInQueue, 'main')

					cv2.imshow(root_window, src_cnt)
				else:
					# show original image
					cv2.imshow(root_window, src_execute)
			else:
				if hsv.HSV_ENABLED:
					# show hsv image
					src_hsv = hsv.toHSV(frame, 'main')
					cv2.imshow(root_window, src_hsv)
				elif thresh.THRESH_ENABLED:
					# show thresh image
					src_thr = thresh.toThresh(frame)
					cv2.imshow(root_window, src_thr)
				# elif contour.CONTOURS_ENABLED:
				# 	# show contours image
				# 	src_contours = contour.getContours(frame)
				# 	cv2.imshow(root_window, src_contours)
				else:
					# show original image
					cv2.imshow(root_window, frame)

			
			_avrage_angle = 0.0
			
			# if object_area_kop > 20000 and object_area_stam > 1200: # 21000 & 5000

				
			# 	if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
					
			# 		command_sing_flag = True
			# 		_angle = anglecalc.get_angle(x1,y1,x2,y2)
				
			# 		av_angle.append(_angle)
			# 		if len(av_angle) > 5:
			# 			av_angle.pop(0)
			# 		# elif len(av_angle) == 3:
			# 		_avrage_angle = ( sum(av_angle)) / len(av_angle) # av_angle[0] + av_angle[1] + av_angle[2]
			# 		# print(f"Angle: {_angle:.0f}, AV: {_avrage_angle:.0f} degrees")
				
			# 	else:
			# 		anglecalc.angle = 0.0
			# 		print("Angle: N/A")

			# 	_avr_ang_str_0f = (f"{_avrage_angle:.0f}")
			# 	stam_coordinaten = (x2.__str__() + ";" + y2.__str__() + ";" + _avr_ang_str_0f) # coordinates of the stem point
			# 	# print(f"Coordinates: {stam_coordinaten}")

			# 	command_sing.append(stam_coordinaten)
	
			# else:
			# 	command_sing_flag = False

			# if not command_sing_flag and len(command_sing) > 5:
			# 	print(f"Command sing: {command_sing[len(command_sing) -1]}")
			# 	coordinateQueue.put(command_sing[len(command_sing) -1])
			# 	command_sing_flag = True
			# 	command_sing.clear() 
			
			if object_area_kop > 15000 and object_area_stam > 1200:
				if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
					command_sing_flag = True
					_angle = anglecalc.get_angle(x1, y1, x2, y2)

					av_angle.append(_angle)
					if len(av_angle) > 5:
						av_angle.pop(0)

					_avrage_angle = sum(av_angle) / len(av_angle)

				else:
					anglecalc.angle = 0.0
					print("Angle: N/A")

				_avr_ang_str_0f = f"{_avrage_angle:.0f}"
				stam_coordinaten = f"{x2};{y2};{_avr_ang_str_0f}"

				command_sing.append(stam_coordinaten)
				last_command_add_time = time.time()  # track last time something was added
				last_command_sing_len = len(command_sing)

			else:
				command_sing_flag = False

			# Delayed sending after no new additions
			if not command_sing_flag and len(command_sing) > 2 :
				time_since_last_add = time.time() - last_command_add_time

				if time_since_last_add >= 1.5:
					if "319;239" in command_sing[-1]:
						print(f"Command sing: {command_sing[-2]}")
						coordinateQueue.put(command_sing[-2])
					else:
						print(f"Command sing: {command_sing[-1]}")
						coordinateQueue.put(command_sing[-1])
					command_sing_flag = True  # prevent repeat sending
					print(command_sing)
					command_sing.clear()
		
			# print(command_sing)
			# print(len(command_sing))

			# Handle key presses
			key = cv2.waitKey(1)
			if key == ord('p'): # voor additional window
				# show window with hsv sliders
				if not hsv.HSV_ENABLED2:
					hsv.create_hsv_sliders('additional')
					# hsv.HSV_ENABLED2 = True
					# hsv.toHSV(frame2, 'additional')

			if key == ord('c'):
				# show window with contour sliders
				if not contour.CONTOURS_ENABLED:
					contour.CONTOURS_ENABLED = True
					contour.create_contour_sliders('main')
				if not contour.CONTOURS_ENABLED2:
					contour.CONTOURS_ENABLED2 = True
					# contour.create_contour_sliders('additional')
			if key == ord('h'):
				# show window with hsv sliders
				if not hsv.HSV_ENABLED:
					hsv.create_hsv_sliders('main')
					# hsv.HSV_ENABLED = True
					# hsv.toHSV(frame, 'main')
			if key == ord('r'):
				# enable depth retrieval
				RETRIEVE_DEPTH = True
				RETRIEVE_DEPTH_ADDITIONAL = True
			if key == ord('s'):
				# disable depth retrieval
				RETRIEVE_DEPTH = False
				RETRIEVE_DEPTH_ADDITIONAL = False
			elif key == ord('t'):
				# show window with treshold sliders
				if not thresh.THRESH_ENABLED:
					if hsv.HSV_ENABLED:
						cv2.destroyWindow(root_window)
						cv2.namedWindow(root_window)
						hsv.HSV_ENABLED = False

					thresh.create_thresh_buttons('additional')
					thresh.create_thresh_buttons('main')
			if key == ord('n'):
				if not hsv.HSV_ENABLED2:
					hsv.create_hsv_sliders('additional')
				if not hsv.HSV_ENABLED:
					hsv.create_hsv_sliders('main')
				assemble('main')
				assemble('additional')
				destroy('main')
				destroy('additional')
				if not contour.CONTOURS_ENABLED:
					contour.CONTOURS_ENABLED = True
					contour.create_contour_sliders('main')
				if not contour.CONTOURS_ENABLED2:
					contour.CONTOURS_ENABLED2 = True
			if key == ord('A'):
				# assemble vision algorithm by adding current operator
				assemble('main')
				assemble('additional')
			if key == ord('C'):
				# clear vision algorithm
				disassemble()
			if key == ord('D'):
				# destroy window and sliders
				destroy('main')
				destroy('additional')
			elif key == ord('Q'):
				# Exit the loop when 'q' is pressed
				break
			elif key == ord('S'):
				# Save the frame when 's' is pressed
				filename = f"frame_{frame_count}.png"

				# check current image
				if hsv.HSV_ENABLED:
					cv2.imwrite(filename, src_hsv)
				elif thresh.THRESH_ENABLED:
					cv2.imwrite(filename, src_thr)
				else:
					cv2.imwrite(filename, frame)

				print(f"Saved {filename}")
				frame_count += 1

		# uncomment below line to show depth image
		#cv2.imshow("depth", depthFrameColor)

	# Clean up
	cv2.destroyAllWindows()
