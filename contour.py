import numpy as np
import cv2

bounding_rects = []

CONTOURS_ENABLED = False
CONTOURS_ENABLED2 = False
iBlurKernelSize = 0
BlurKernel = (5,5)
POLYGONS_ENABLED = False
POLYGONS_ENABLED2 = False
iPolyKernelSize = 0
PolyKernel = (3,3)
iEpsilon = 1
PolyEpsilon = 0.01
iPolyArea = 0
PolyArea = 0.005
MaxArea = 0

CONTOUR_settings = [['Blurkernel', (5,5)]]
CONTOUR_settings2 = [['Blurkernel', (5,5)]]

def BlurKernelCallback(x):
	global iBlurKernelSize
	global BlurKernel

	# get trackbar positions
	iBlurKernelSize = cv2.getTrackbarPos('BlurKernelSize', 'main')

	#print(iBlurKernelSize)

	if(iBlurKernelSize == 0):
		BlurKernel = (5,5)
	elif(iBlurKernelSize == 1):
		BlurKernel = (9,9)
	elif(iBlurKernelSize == 2):
		BlurKernel = (13,13)
	elif(iBlurKernelSize == 3):
		BlurKernel = (21,21)
	elif(iBlurKernelSize == 4):
		BlurKernel = (31,31)
	elif(iBlurKernelSize == 5):
		BlurKernel = (51,51)
	else:
		BlurKernel = (5,5)

	#print(BlurKernel)

def BlurKernelCallback2(x):
	global iBlurKernelSize
	global BlurKernel

	# get trackbar positions
	iBlurKernelSize = cv2.getTrackbarPos('BlurKernelSize', 'additional')

	#print(iBlurKernelSize)

	if(iBlurKernelSize == 0):
		BlurKernel = (5,5)
	elif(iBlurKernelSize == 1):
		BlurKernel = (9,9)
	elif(iBlurKernelSize == 2):
		BlurKernel = (13,13)
	elif(iBlurKernelSize == 3):
		BlurKernel = (21,21)
	elif(iBlurKernelSize == 4):
		BlurKernel = (31,31)
	elif(iBlurKernelSize == 5):
		BlurKernel = (51,51)
	else:
		BlurKernel = (5,5)

	#print(BlurKernel)

def PolyKernelCallback(x):
	global iPolyKernelSize
	global PolyKernel

	# get trackbar positions
	iPolyKernelSize = cv2.getTrackbarPos('PolyKernelSize', 'main')

	#print(iPolyKernelSize)

	if(iPolyKernelSize == 0):
		PolyKernel = (5,5)
	elif(iPolyKernelSize == 1):
		PolyKernel = (11,11)
	elif(iPolyKernelSize == 2):
		PolyKernel = (21,21)
	elif(iPolyKernelSize == 3):
		PolyKernel = (41,41)
	elif(iPolyKernelSize == 4):
		PolyKernel = (71,71)
	elif(iPolyKernelSize == 5):
		PolyKernel = (101,101)
	else:
		PolyKernel = (5,5)

	#print(PolyKernel)

def PolyKernelCallback2(x):
	global iPolyKernelSize
	global PolyKernel

	# get trackbar positions
	iPolyKernelSize = cv2.getTrackbarPos('PolyKernelSize', 'additional')

	#print(iPolyKernelSize)

	if(iPolyKernelSize == 0):
		PolyKernel = (5,5)
	elif(iPolyKernelSize == 1):
		PolyKernel = (11,11)
	elif(iPolyKernelSize == 2):
		PolyKernel = (21,21)
	elif(iPolyKernelSize == 3):
		PolyKernel = (41,41)
	elif(iPolyKernelSize == 4):
		PolyKernel = (71,71)
	elif(iPolyKernelSize == 5):
		PolyKernel = (101,101)
	else:
		PolyKernel = (5,5)

	#print(PolyKernel)

def PolyEpsilonCallback(x):
	global iEpsilon
	global PolyEpsilon

	# get trackbar positions
	iEpsilon = cv2.getTrackbarPos('PolyEpsilon', 'main')


	#print(iEpsilon)
	if(iEpsilon == 0):
		PolyEpsilon = 0.01
	elif(iEpsilon == 1):
		PolyEpsilon = 0.02
	elif(iEpsilon == 2):
		PolyEpsilon = 0.025
	elif(iEpsilon == 3):
		PolyEpsilon = 0.05
	elif(iEpsilon == 4):
		PolyEpsilon = 0.075
	elif(iEpsilon == 5):
		PolyEpsilon = 0.1
	elif(iEpsilon == 6):
		PolyEpsilon = 0.2
	elif(iEpsilon == 7):
		PolyEpsilon = 0.25
	elif(iEpsilon == 8):
		PolyEpsilon = 0.3
	elif(iEpsilon == 9):
		PolyEpsilon = 0.4
	elif(iEpsilon == 10):
		PolyEpsilon = 0.5
	else:
		PolyEpsilon = 0.05

	#print(PolyEpsilon)


def PolyEpsilonCallback2(x):
	global iEpsilon
	global PolyEpsilon

	# get trackbar positions
	iEpsilon = cv2.getTrackbarPos('PolyEpsilon', 'additional')


	#print(iEpsilon)
	if(iEpsilon == 0):
		PolyEpsilon = 0.01
	elif(iEpsilon == 1):
		PolyEpsilon = 0.02
	elif(iEpsilon == 2):
		PolyEpsilon = 0.025
	elif(iEpsilon == 3):
		PolyEpsilon = 0.05
	elif(iEpsilon == 4):
		PolyEpsilon = 0.075
	elif(iEpsilon == 5):
		PolyEpsilon = 0.1
	elif(iEpsilon == 6):
		PolyEpsilon = 0.2
	elif(iEpsilon == 7):
		PolyEpsilon = 0.25
	elif(iEpsilon == 8):
		PolyEpsilon = 0.3
	elif(iEpsilon == 9):
		PolyEpsilon = 0.4
	elif(iEpsilon == 10):
		PolyEpsilon = 0.5
	else:
		PolyEpsilon = 0.05

	#print(PolyEpsilon)

def PolyAreaCallback(x):
	global iPolyArea
	global PolyArea

	# get trackbar positions
	iPolyArea = cv2.getTrackbarPos('PolygonArea', 'main')


	#print(iPolyArea)
	if(iPolyArea == 0):
		PolyArea = 0.005
	elif(iPolyArea == 1):
		PolyArea = 0.01
	elif(iPolyArea == 2):
		PolyArea = 0.05
	elif(iPolyArea == 3):
		PolyArea = 0.1
	elif(iPolyArea == 4):
		PolyArea = 0.2
	elif(iPolyArea == 5):
		PolyArea = 0.25
	elif(iPolyArea == 6):
		PolyArea = 0.30
	elif(iPolyArea == 7):
		PolyArea = 0.35
	elif(iPolyArea == 8):
		PolyArea = 0.40
	elif(iPolyArea == 9):
		PolyArea = 0.45
	elif(iPolyArea == 10):
		PolyArea = 0.50
	else:
		PolyArea = 0.005

	#print(PolyArea)

def PolyAreaCallback2(x):
	global iPolyArea
	global PolyArea

	# get trackbar positions
	iPolyArea = cv2.getTrackbarPos('PolygonArea', 'additional')


	#print(iPolyArea)
	if(iPolyArea == 0):
		PolyArea = 0.005
	elif(iPolyArea == 1):
		PolyArea = 0.01
	elif(iPolyArea == 2):
		PolyArea = 0.05
	elif(iPolyArea == 3):
		PolyArea = 0.1
	elif(iPolyArea == 4):
		PolyArea = 0.2
	elif(iPolyArea == 5):
		PolyArea = 0.25
	elif(iPolyArea == 6):
		PolyArea = 0.30
	elif(iPolyArea == 7):
		PolyArea = 0.35
	elif(iPolyArea == 8):
		PolyArea = 0.40
	elif(iPolyArea == 9):
		PolyArea = 0.45
	elif(iPolyArea == 10):
		PolyArea = 0.50
	else:
		PolyArea = 0.005

	#print(PolyArea)

def create_contour_sliders(window_name):
	global iBlurKernelSize
	global iPolyKernelSize
	global iEpsilon
	global iPolyArea

	if window_name == 'main':
		global CONTOURS_ENABLED
		

		cv2.createTrackbar('BlurKernelSize', 'main', iBlurKernelSize, 5, BlurKernelCallback)
		cv2.createTrackbar('PolyKernelSize', 'main', iPolyKernelSize, 5, PolyKernelCallback)
		cv2.createTrackbar('PolyEpsilon', 'main', iEpsilon, 10, PolyEpsilonCallback)
		cv2.createTrackbar('PolygonArea', 'main', iPolyArea, 10, PolyAreaCallback)

		iBlurKernelSize = 0
		cv2.setTrackbarPos('BlurKernelSize', 'main', iBlurKernelSize)

		iPolyKernelSize = 0
		cv2.setTrackbarPos('PolyKernelSize', 'main', iPolyKernelSize)

		iEpsilon = 1
		cv2.setTrackbarPos('PolyEpsilon', 'main', iEpsilon)

		iPolyArea = 0
		cv2.setTrackbarPos('PolygonArea', 'main', iPolyArea)

		CONTOURS_ENABLED = True
	else:
		global CONTOURS_ENABLED2


		cv2.createTrackbar('BlurKernelSize', 'additional', iBlurKernelSize, 5, BlurKernelCallback2)
		cv2.createTrackbar('PolyKernelSize', 'additional', iPolyKernelSize, 5, PolyKernelCallback2)
		cv2.createTrackbar('PolyEpsilon', 'additional', iEpsilon, 10, PolyEpsilonCallback2)
		cv2.createTrackbar('PolygonArea', 'additional', iPolyArea, 10, PolyAreaCallback2)

		iBlurKernelSize = 0
		cv2.setTrackbarPos('BlurKernelSize', 'additional', iBlurKernelSize)

		iPolyKernelSize = 0
		cv2.setTrackbarPos('PolyKernelSize', 'additional', iPolyKernelSize)

		iEpsilon = 1
		cv2.setTrackbarPos('PolyEpsilon', 'additional', iEpsilon)

		iPolyArea = 0
		cv2.setTrackbarPos('PolygonArea', 'additional', iPolyArea)	
		CONTOURS_ENABLED2 = True

def getContours(img):
	global BlurKernel
	global PolyKernel
	global PolyEpsilon
	global PolyArea
	global MaxArea
	global bounding_rect

	# create copy of source image
	src_cnt = np.copy(img)

	# use regular preprocessing (gray scale conversion, blurring) and threshold
	src_grey = cv2.cvtColor(src_cnt, cv2.COLOR_BGR2GRAY)
	
	blur = cv2.GaussianBlur(src_grey, BlurKernel, 0)
	ret, src_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	# find the contours in the threshold image
	contours, hierachy = cv2.findContours(src_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	#print(len(contours))
	contour_counter = 0

	for contour in contours:
		if contour_counter == 0:
			contour_counter = contour_counter + 1
			continue
		else:
			w,h = src_cnt.shape[0], src_cnt.shape[1]
			MaxArea = w * h
			#print(MaxArea)
			ThreshArea = int(MaxArea * PolyArea)
			#print(ThreshArea)

			if(cv2.contourArea(contour) > ThreshArea):
				# draw the contour in the source image
				cv2.drawContours(src_cnt, contour, -1, (0,0,255), 3)

				# retrieve contour perimeter - uncomment if to be used
				#perimeter = cv2.arcLength(contour, True)
				#print(perimeter)

				# store and draw bounding box
				x,y,w,h = cv2.boundingRect(contour)
				bounding_rects.append((x,y,w,h))
				cv2.rectangle(src_cnt,(x,y),(x+w,y+h),(0,255,0),2)

	return src_cnt

def execute_contour(img, settings):
	global BlurKernel
	global PolyKernel
	global PolyEpsilon
	global PolyArea
	global MaxArea
	global bounding_rect

	# create copy of source image
	src_cnt = np.copy(img)

	# use regular preprocessing (gray scale conversion, blurring) and threshold
	src_grey = cv2.cvtColor(src_cnt, cv2.COLOR_BGR2GRAY)
	
	blur = cv2.GaussianBlur(src_grey, BlurKernel, 0)
	ret, src_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	# find the contours in the threshold image
	contours, hierachy = cv2.findContours(src_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	#print(len(contours))
	contour_counter = 0

	for contour in contours:
		if contour_counter == 0:
			contour_counter = contour_counter + 1
			continue
		else:
			w,h = src_cnt.shape[0], src_cnt.shape[1]
			MaxArea = w * h
			#print(MaxArea)
			ThreshArea = int(MaxArea * PolyArea)
			#print(ThreshArea)

			if(cv2.contourArea(contour) > ThreshArea):
				# draw the contour in the source image
				cv2.drawContours(src_cnt, contour, -1, (0,0,255), 3)

				# retrieve contour perimeter - uncomment if to be used
				#perimeter = cv2.arcLength(contour, True)
				#print(perimeter)

				# store and draw bounding box
				x,y,w,h = cv2.boundingRect(contour)
				bounding_rects.append((x,y,w,h))
				cv2.rectangle(src_cnt,(x,y),(x+w,y+h),(0,255,0),2)

	return src_cnt

def create_polygon_sliders():
	global POLYGONS_ENABLED
	global iPolyKernelSize
	global iEpsilon
	global iPolyArea

	cv2.createTrackbar('PolyKernelSize', 'main', iPolyKernelSize, 5, PolyKernelCallback)
	cv2.createTrackbar('PolyEpsilon', 'main', iEpsilon, 10, PolyEpsilonCallback)
	cv2.createTrackbar('PolygonArea', 'main', iPolyArea, 10, PolyAreaCallback)

	iPolyKernelSize = 0
	cv2.setTrackbarPos('PolyKernelSize', 'main', iPolyKernelSize)

	iEpsilon = 1
	cv2.setTrackbarPos('PolyEpsilon', 'main', iEpsilon)

	iPolyArea = 0
	cv2.setTrackbarPos('PolygonArea', 'main', iPolyArea)

	CONTOURS_ENABLED = True
	POLYGONS_ENABLED = True

def getPolygons(img):
	global PolyKernel
	global PolyEpsilon
	global PolyArea
	global MaxArea
	
	# create copy of source image
	src_poly = np.copy(img)

	# use regular preprocessing (gray scale conversion, blurring) and threshold
	src_grey = cv2.cvtColor(src_poly, cv2.COLOR_BGR2GRAY)
	
	blur = cv2.GaussianBlur(src_grey, PolyKernel, 0)

	ret, src_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	# find the contours in the threshold image
	contours, hierachy = cv2.findContours(src_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	#print(len(contours))
	contour_counter = 0

	for contour in contours:
		# skip the biggest contour in the image (= entire image)
		if contour_counter == 0:
			contour_counter = contour_counter + 1
			continue
		else:
			w,h = src_poly.shape[0], src_poly.shape[1]
			MaxArea = w * h
			print(MaxArea)
			ThreshArea = int(MaxArea * PolyArea)
			print(ThreshArea)

			# draw the contour in the source image
			cv2.drawContours(src_poly, contour, -1, (0,0,255), 3)

			perimeter = cv2.arcLength(contour, True)

			if(cv2.contourArea(contour) > ThreshArea):
				max_deviation = PolyEpsilon * perimeter
				#print(max_deviation)

				# get the approximate polygon of the contour
				approx = cv2.approxPolyDP(contour, max_deviation, True)

				# draw the draw the approximated polygon in the source image
				cv2.drawContours(src_poly, [approx], -1, (0,255,0), 3)

				# get the number of vertices
				vertices = len(approx)
				#print(vertices)

				if(vertices == 3):
					text = '3 vertices'

					# put text on image
					org = (25, 25)  # Bottom-left corner of the text string in the image
					font = cv2.FONT_HERSHEY_SIMPLEX
					fontScale = 1
					color = (255, 0, 0)  # Blue color in BGR
					thickness = 2
					cv2.putText(src_poly, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
				if(vertices >= 12):
					text = '12 or more vertices'

					# put text on image
					org = (25, 25)  # Bottom-left corner of the text string in the image
					font = cv2.FONT_HERSHEY_SIMPLEX
					fontScale = 1
					color = (255, 0, 0)  # Blue color in BGR
					thickness = 2
					cv2.putText(src_poly, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

	return src_poly