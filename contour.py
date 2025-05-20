import numpy as np
import cv2
import angle
from math import atan2, pi

bounding_rects = []

CONTOURS_ENABLED = False
CONTOURS_ENABLED2 = False
iBlurKernelSize = 0
iBlurKernelSize2 = 0

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



iPolyKernelSize2 = 0
PolyKernel2 = (3,3)
iEpsilon2 = 1
PolyEpsilon2 = 0.01
iPolyArea2 = 0
PolyArea2 = 0.005
MaxArea2 = 0

CONTOUR_settings = [['Blurkernel', (5,5)]]
CONTOUR_settings2 = [['Blurkernel2', (5,5)]]

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
	global iBlurKernelSize2
	global BlurKernel2

	# get trackbar positions
	iBlurKernelSize2 = cv2.getTrackbarPos('BlurKernelSize2', 'additional')

	#print(iBlurKernelSize)

	if(iBlurKernelSize2 == 0):
		BlurKernel2 = (5,5)
	elif(iBlurKernelSize2 == 1):
		BlurKernel2 = (9,9)
	elif(iBlurKernelSize2 == 2):
		BlurKernel2 = (13,13)
	elif(iBlurKernelSize2 == 3):
		BlurKernel2 = (21,21)
	elif(iBlurKernelSize2 == 4):
		BlurKernel2 = (31,31)
	elif(iBlurKernelSize2 == 5):
		BlurKernel2 = (51,51)
	else:
		BlurKernel2 = (5,5)

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
	global iPolyKernelSize2
	global PolyKernel2

	# get trackbar positions
	iPolyKernelSize2 = cv2.getTrackbarPos('PolyKernelSize', 'additional')

	#print(iPolyKernelSize)

	if(iPolyKernelSize2 == 0):
		PolyKernel2 = (5,5)
	elif(iPolyKernelSize2 == 1):
		PolyKernel2 = (11,11)
	elif(iPolyKernelSize2 == 2):
		PolyKernel2 = (21,21)
	elif(iPolyKernelSize2 == 3):
		PolyKernel2 = (41,41)
	elif(iPolyKernelSize2 == 4):
		PolyKernel2 = (71,71)
	elif(iPolyKernelSize2 == 5):
		PolyKernel2 = (101,101)
	else:
		PolyKernel2 = (5,5)

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
	global iEpsilon2
	global PolyEpsilon2

	# get trackbar positions
	iEpsilon2 = cv2.getTrackbarPos('PolyEpsilon2', 'additional')


	#print(iEpsilon)
	if(iEpsilon2 == 0):
		PolyEpsilon2 = 0.01
	elif(iEpsilon2 == 1):
		PolyEpsilon2 = 0.02
	elif(iEpsilon2 == 2):
		PolyEpsilon2 = 0.025
	elif(iEpsilon2 == 3):
		PolyEpsilon2 = 0.05
	elif(iEpsilon2 == 4):
		PolyEpsilon2 = 0.075
	elif(iEpsilon2 == 5):
		PolyEpsilon2 = 0.1
	elif(iEpsilon2 == 6):
		PolyEpsilon2 = 0.2
	elif(iEpsilon2 == 7):
		PolyEpsilon2 = 0.25
	elif(iEpsilon2 == 8):
		PolyEpsilon2 = 0.3
	elif(iEpsilon2 == 9):
		PolyEpsilon2 = 0.4
	elif(iEpsilon2 == 10):
		PolyEpsilon2 = 0.5
	else:
		PolyEpsilon2 = 0.05

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
	global iPolyArea2
	global PolyArea2

	# get trackbar positions
	iPolyArea2 = cv2.getTrackbarPos('PolygonArea', 'additional')


	#print(iPolyArea)
	if(iPolyArea2 == 0):
		PolyArea2 = 0.005
	elif(iPolyArea2 == 1):
		PolyArea2 = 0.01
	elif(iPolyArea2 == 2):
		PolyArea2 = 0.05
	elif(iPolyArea2== 3):
		PolyArea2 = 0.1
	elif(iPolyArea2 == 4):
		PolyArea2 = 0.2
	elif(iPolyArea2 == 5):
		PolyArea2 = 0.25
	elif(iPolyArea2 == 6):
		PolyArea2 = 0.30
	elif(iPolyArea2 == 7):
		PolyArea2 = 0.35
	elif(iPolyArea2 == 8):
		PolyArea2 = 0.40
	elif(iPolyArea2 == 9):
		PolyArea2 = 0.45
	elif(iPolyArea2 == 10):
		PolyArea2 = 0.50
	else:
		PolyArea2 = 0.005

	#print(PolyArea)

def create_contour_sliders(window_name):
	bounding_rects.clear()

	if window_name == 'main':
		global CONTOURS_ENABLED
		global iBlurKernelSize
		global iPolyKernelSize
		global iEpsilon
		global iPolyArea

		CONTOURS_ENABLED = True
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
		if CONTOURS_ENABLED == False:
			CONTOURS_ENABLED = True
	elif window_name == 'additional':
		global CONTOURS_ENABLED2
		global iBlurKernelSize2
		global iPolyKernelSize2
		global iEpsilon2
		global iPolyArea2

		CONTOURS_ENABLED2 = True
		cv2.createTrackbar('BlurKernelSize2', 'additional', iBlurKernelSize2, 5, BlurKernelCallback2)
		cv2.createTrackbar('PolyKernelSize2', 'additional', iPolyKernelSize2, 5, PolyKernelCallback2)
		cv2.createTrackbar('PolyEpsilon2', 'additional', iEpsilon2, 10, PolyEpsilonCallback2)
		cv2.createTrackbar('PolygonArea2', 'additional', iPolyArea2, 10, PolyAreaCallback2)

		iBlurKernelSize2 = 0
		cv2.setTrackbarPos('BlurKernelSize2', 'additional', iBlurKernelSize2)

		iPolyKernelSize2 = 0
		cv2.setTrackbarPos('PolyKernelSize2', 'additional', iPolyKernelSize2)

		iEpsilon2 = 1
		cv2.setTrackbarPos('PolyEpsilon2', 'additional', iEpsilon2)

		iPolyArea2 = 0
		cv2.setTrackbarPos('PolygonArea2', 'additional', iPolyArea2)	
		if CONTOURS_ENABLED2 == False:
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
				rows,cols = src_cnt.shape[:2]
				cnt = contour
				rect = cv2.minAreaRect(cnt)
				box = cv2.boxPoints(rect)
				box = np.int0(box)

				center = (int(rect[0][0]),int(rect[0][1])) # center of the rectangle
				
				cv2.drawContours(src_cnt,[box],0,(0,0,255),2)
				[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
				lefty = int((-x*vy/vx) + y)
				righty = int(((cols-x)*vy/vx)+y)
				cv2.line(src_cnt,(cols-1,righty),(0,lefty),(0,255,0),2)

				x1,y2 = center

				# retrieve contour perimeter - uncomment if to be used
				#perimeter = cv2.arcLength(contour, True)
				#print(perimeter)

				# store and draw bounding box
				x,y,w,h = cv2.boundingRect(contour)
				bounding_rects.append((x,y,w,h))
				cv2.rectangle(src_cnt,(x,y),(x+w,y+h),(0,255,0),2)

	return src_cnt, x1 ,y2

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

def create_polygon_sliders(window_name):

	global iPolyKernelSize
	global iEpsilon
	global iPolyArea
	

	if window_name == 'main':
		global POLYGONS_ENABLED


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
	elif window_name == 'additional':
		global POLYGONS_ENABLED2


		cv2.createTrackbar('PolyKernelSize', 'additional', iPolyKernelSize, 5, PolyKernelCallback)
		cv2.createTrackbar('PolyEpsilon', 'additional', iEpsilon, 10, PolyEpsilonCallback)
		cv2.createTrackbar('PolygonArea', 'additional', iPolyArea, 10, PolyAreaCallback)

		iPolyKernelSize = 0
		cv2.setTrackbarPos('PolyKernelSize', 'additional', iPolyKernelSize)

		iEpsilon = 1
		cv2.setTrackbarPos('PolyEpsilon', 'additional', iEpsilon)

		iPolyArea = 0
		cv2.setTrackbarPos('PolygonArea', 'additional', iPolyArea)

		CONTOURS_ENABLED2 = True
		POLYGONS_ENABLED2 = True

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