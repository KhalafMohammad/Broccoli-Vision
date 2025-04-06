import cv2
import ctypes

THRESH_ENABLED = False
THRESH_ENABLED2 = False

BINARY     = 0
BINARY_INV = 1
OTSU_INV   = 2
GAUSS_INV  = 3
MEAN_INV   = 4

NAME   = 0
VALUE  = 1

THRESH_settings = [['Binary', 0],['BinaryInv', 0], ['Otsu', 0], ['AdaptiveGaussian', 0], ['AdaptiveMean', 0]]

def MessageBox(title, text, style):
	##  Styles:
	##  0 : OK
	##  1 : OK | Cancel
	##  2 : Abort | Retry | Ignore
	##  3 : Yes | No | Cancel
	##  4 : Yes | No
	##  5 : Retry | Cancel 
	##  6 : Cancel | Try Again | Continue
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def ThreshCallback(x):
	global THRESH_settings

	# get trackbar positions
	THRESH_settings[BINARY][VALUE] = cv2.getTrackbarPos(THRESH_settings[BINARY][NAME], 'main')
	THRESH_settings[BINARY_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[BINARY_INV][NAME], 'main')
	THRESH_settings[OTSU_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[OTSU_INV][NAME], 'main')
	THRESH_settings[GAUSS_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[GAUSS_INV][NAME], 'main')
	THRESH_settings[MEAN_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[MEAN_INV][NAME], 'main')

	if(THRESH_settings[BINARY][VALUE] + THRESH_settings[BINARY_INV][VALUE] + THRESH_settings[OTSU_INV][VALUE] + THRESH_settings[GAUSS_INV][VALUE] + THRESH_settings[MEAN_INV][VALUE] > 1):
		MessageBox('Info', 'Warning: only 1 threshold operator allowed', 0)
		ResetThreshTrackbar('main')


def ThreshCallback2(x):
	global THRESH_settings

	# get trackbar positions
	THRESH_settings[BINARY][VALUE] = cv2.getTrackbarPos(THRESH_settings[BINARY][NAME], 'additional')
	THRESH_settings[BINARY_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[BINARY_INV][NAME], 'additional')
	THRESH_settings[OTSU_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[OTSU_INV][NAME], 'additional')
	THRESH_settings[GAUSS_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[GAUSS_INV][NAME], 'additional')
	THRESH_settings[MEAN_INV][VALUE] = cv2.getTrackbarPos(THRESH_settings[MEAN_INV][NAME], 'additional')

	if(THRESH_settings[BINARY][VALUE] + THRESH_settings[BINARY_INV][VALUE] + THRESH_settings[OTSU_INV][VALUE] + THRESH_settings[GAUSS_INV][VALUE] + THRESH_settings[MEAN_INV][VALUE] > 1):
		MessageBox('Info', 'Warning: only 1 threshold operator allowed', 0)
		ResetThreshTrackbar('additional')




def ResetThreshTrackbar(window_name):
	if window_name == 'main':
		global THRESH_settings

		THRESH_settings[BINARY][VALUE] = 0
		THRESH_settings[BINARY_INV][VALUE] = 0
		THRESH_settings[OTSU_INV][VALUE] = 0
		THRESH_settings[GAUSS_INV][VALUE] = 0
		THRESH_settings[MEAN_INV][VALUE] = 0

		cv2.setTrackbarPos(THRESH_settings[BINARY][NAME], 'main', THRESH_settings[BINARY][VALUE])
		cv2.setTrackbarPos(THRESH_settings[BINARY_INV][NAME], 'main', THRESH_settings[BINARY_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[OTSU_INV][NAME], 'main', THRESH_settings[OTSU_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[GAUSS_INV][NAME], 'main', THRESH_settings[GAUSS_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[MEAN_INV][NAME], 'main', THRESH_settings[MEAN_INV][VALUE])
	elif window_name == 'additional':
		global THRESH_settings2

		THRESH_settings[BINARY][VALUE] = 0
		THRESH_settings[BINARY_INV][VALUE] = 0
		THRESH_settings[OTSU_INV][VALUE] = 0
		THRESH_settings[GAUSS_INV][VALUE] = 0
		THRESH_settings[MEAN_INV][VALUE] = 0

		cv2.setTrackbarPos(THRESH_settings[BINARY][NAME], 'additional', THRESH_settings[BINARY][VALUE])
		cv2.setTrackbarPos(THRESH_settings[BINARY_INV][NAME], 'additional', THRESH_settings[BINARY_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[OTSU_INV][NAME], 'additional', THRESH_settings[OTSU_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[GAUSS_INV][NAME], 'additional', THRESH_settings[GAUSS_INV][VALUE])
		cv2.setTrackbarPos(THRESH_settings[MEAN_INV][NAME], 'additional', THRESH_settings[MEAN_INV][VALUE])

def create_thresh_buttons(window_name):
	if window_name == 'main':
		global THRESH_ENABLED

		cv2.createTrackbar(THRESH_settings[BINARY][NAME], 'main', THRESH_settings[BINARY][VALUE], 1, ThreshCallback)
		cv2.createTrackbar(THRESH_settings[BINARY_INV][NAME], 'main', THRESH_settings[BINARY_INV][VALUE], 1, ThreshCallback)
		cv2.createTrackbar(THRESH_settings[OTSU_INV][NAME], 'main', THRESH_settings[OTSU_INV][VALUE], 1, ThreshCallback)
		cv2.createTrackbar(THRESH_settings[GAUSS_INV][NAME], 'main', THRESH_settings[GAUSS_INV][VALUE], 1, ThreshCallback)
		cv2.createTrackbar(THRESH_settings[MEAN_INV][NAME], 'main', THRESH_settings[MEAN_INV][VALUE], 1, ThreshCallback)

		THRESH_ENABLED = True
	elif window_name == 'additional':
		global THRESH_ENABLED2

		cv2.createTrackbar(THRESH_settings[BINARY][NAME], 'additional', THRESH_settings[BINARY][VALUE], 1, ThreshCallback2)
		cv2.createTrackbar(THRESH_settings[BINARY_INV][NAME], 'additional', THRESH_settings[BINARY_INV][VALUE], 1, ThreshCallback2)
		cv2.createTrackbar(THRESH_settings[OTSU_INV][NAME], 'additional', THRESH_settings[OTSU_INV][VALUE], 1, ThreshCallback2)
		cv2.createTrackbar(THRESH_settings[GAUSS_INV][NAME], 'additional', THRESH_settings[GAUSS_INV][VALUE], 1, ThreshCallback2)
		cv2.createTrackbar(THRESH_settings[MEAN_INV][NAME], 'additional', THRESH_settings[MEAN_INV][VALUE], 1, ThreshCallback2)

		THRESH_ENABLED2 = True



def toThresh(img):
	global THRESH_settings

	src_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	if THRESH_settings[BINARY][VALUE] == 1:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY)
	elif THRESH_settings[BINARY_INV][VALUE] == 1:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY_INV)
	elif THRESH_settings[OTSU_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		ret, src_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	elif THRESH_settings[GAUSS_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		src_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	elif THRESH_settings[MEAN_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		src_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	else:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY)

	return src_thresh

def execute_thresh(img, settings):
	global THRESH_settings

	src_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	if THRESH_settings[BINARY][VALUE] == 1:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY)
	elif THRESH_settings[BINARY_INV][VALUE] == 1:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY_INV)
	elif THRESH_settings[OTSU_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		#blur = cv2.medianBlur(src_grey, 5)
		ret, src_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	elif THRESH_settings[GAUSS_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		#blur = cv2.medianBlur(src_grey, 5)
		src_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	elif THRESH_settings[MEAN_INV][VALUE] == 1:
		blur = cv2.GaussianBlur(src_grey, (5,5), 0)
		#blur = cv2.medianBlur(src_grey, 5)
		src_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	else:
		ret, src_thresh = cv2.threshold(src_grey, 127, 255, cv2.THRESH_BINARY)

	return img
