import cv2
import numpy as np

HSV_ENABLED = False
HSV_ENABLED2 = False

LOW_H  = 0
HIGH_H = 1
LOW_S  = 2
HIGH_S = 3
LOW_V  = 4
HIGH_V = 5

NAME   = 0
VALUE  = 1

HSV_settings = [['lowH', 40],['highH', 179], ['lowS', 53], ['highS', 89], ['lowV', 100], ['highV', 203]]
HSV_settings2 = [['lowH', 0],['highH', 38], ['lowS', 64], ['highS', 177], ['lowV',191], ['highV', 255]]

def HSVcallback(x):
	global HSV_settings

	# get trackbar positions
	HSV_settings[LOW_H][VALUE] = cv2.getTrackbarPos(HSV_settings[LOW_H][NAME], 'main')
	HSV_settings[HIGH_H][VALUE] = cv2.getTrackbarPos(HSV_settings[HIGH_H][NAME], 'main')
	HSV_settings[LOW_S][VALUE] = cv2.getTrackbarPos(HSV_settings[LOW_S][NAME], 'main')
	HSV_settings[HIGH_S][VALUE] = cv2.getTrackbarPos(HSV_settings[HIGH_S][NAME], 'main')
	HSV_settings[LOW_V][VALUE] = cv2.getTrackbarPos(HSV_settings[LOW_V][NAME], 'main')
	HSV_settings[HIGH_V][VALUE] = cv2.getTrackbarPos(HSV_settings[HIGH_V][NAME], 'main')

	#print("low Hue: ", HSV_settings[0][1])
	#print("high Hue: ", HSV_settings[1][1])
	#print("low Saturation: ", HSV_settings[2][1])
	#print("high Saturation: ", HSV_settings[3][1])
	#print("low Value: ", HSV_settings[4][1])
	#print("high Value: ", HSV_settings[5][1])

def HSVcallback2(x):
	global HSV_settings2

	# get trackbar positions
	HSV_settings2[LOW_H][VALUE] = cv2.getTrackbarPos(HSV_settings2[LOW_H][NAME], 'additional')
	HSV_settings2[HIGH_H][VALUE] = cv2.getTrackbarPos(HSV_settings2[HIGH_H][NAME], 'additional')
	HSV_settings2[LOW_S][VALUE] = cv2.getTrackbarPos(HSV_settings2[LOW_S][NAME], 'additional')
	HSV_settings2[HIGH_S][VALUE] = cv2.getTrackbarPos(HSV_settings2[HIGH_S][NAME], 'additional')
	HSV_settings2[LOW_V][VALUE] = cv2.getTrackbarPos(HSV_settings2[LOW_V][NAME], 'additional')
	HSV_settings2[HIGH_V][VALUE] = cv2.getTrackbarPos(HSV_settings2[HIGH_V][NAME], 'additional')

	#print("low Hue: ", HSV_settings[0][1])
	#print("high Hue: ", HSV_settings[1][1])
	#print("low Saturation: ", HSV_settings[2][1])
	#print("high Saturation: ", HSV_settings[3][1])
	#print("low Value: ", HSV_settings[4][1])
	#print("high Value: ", HSV_settings[5][1])

def create_hsv_sliders(window_name): #changed from 'main' to 'window_name'

	if window_name == 'main':
		global HSV_ENABLED
		global HSV_ENABLED2
		global HSV_settings

		# create trackbars for color change
		cv2.createTrackbar(HSV_settings[LOW_H][NAME], window_name, HSV_settings[LOW_H][VALUE], 179, HSVcallback)
		cv2.createTrackbar(HSV_settings[HIGH_H][NAME], window_name, HSV_settings[HIGH_H][VALUE], 179, HSVcallback)
		cv2.createTrackbar(HSV_settings[LOW_S][NAME], window_name, HSV_settings[LOW_S][VALUE], 255, HSVcallback)
		cv2.createTrackbar(HSV_settings[HIGH_S][NAME], window_name, HSV_settings[HIGH_S][VALUE], 255, HSVcallback)
		cv2.createTrackbar(HSV_settings[LOW_V][NAME], window_name, HSV_settings[LOW_V][VALUE], 255, HSVcallback)
		cv2.createTrackbar(HSV_settings[HIGH_V][NAME], window_name, HSV_settings[HIGH_V][VALUE], 255, HSVcallback)
		HSV_ENABLED = True
	else:
		cv2.createTrackbar(HSV_settings2[LOW_H][NAME], window_name, HSV_settings2[LOW_H][VALUE], 179, HSVcallback2)
		cv2.createTrackbar(HSV_settings2[HIGH_H][NAME], window_name, HSV_settings2[HIGH_H][VALUE], 179, HSVcallback2)
		cv2.createTrackbar(HSV_settings2[LOW_S][NAME], window_name, HSV_settings2[LOW_S][VALUE], 255, HSVcallback2)
		cv2.createTrackbar(HSV_settings2[HIGH_S][NAME], window_name, HSV_settings2[HIGH_S][VALUE], 255, HSVcallback2)
		cv2.createTrackbar(HSV_settings2[LOW_V][NAME], window_name, HSV_settings2[LOW_V][VALUE], 255, HSVcallback2)
		cv2.createTrackbar(HSV_settings2[HIGH_V][NAME], window_name, HSV_settings2[HIGH_V][VALUE], 255, HSVcallback2)
		HSV_ENABLED2 = True

def toHSV(img , window_name):
	if window_name == 'main':
		global HSV_settings
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		lower_hsv = np.array([HSV_settings[LOW_H][VALUE], HSV_settings[LOW_S][VALUE], HSV_settings[LOW_V][VALUE]])
		higher_hsv = np.array([HSV_settings[HIGH_H][VALUE], HSV_settings[HIGH_S][VALUE], HSV_settings[HIGH_V][VALUE]])
		mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

		return cv2.bitwise_and(img, img, mask=mask)
	else:
		global HSV_settings2
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		lower_hsv = np.array([HSV_settings2[LOW_H][VALUE], HSV_settings2[LOW_S][VALUE], HSV_settings2[LOW_V][VALUE]])
		higher_hsv = np.array([HSV_settings2[HIGH_H][VALUE], HSV_settings2[HIGH_S][VALUE], HSV_settings2[HIGH_V][VALUE]])
		mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

		return cv2.bitwise_and(img, img, mask=mask)


def execute_hsv(img, settings):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower_hsv = np.array([settings[LOW_H][VALUE], settings[LOW_S][VALUE], settings[LOW_V][VALUE]])
	higher_hsv = np.array([settings[HIGH_H][VALUE], settings[HIGH_S][VALUE], settings[HIGH_V][VALUE]])
	mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

	return cv2.bitwise_and(img, img, mask=mask)

	return img
