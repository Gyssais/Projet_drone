import cv2
import numpy as np
from Morph_Trans import *
from Contours import *
from Constances import *


m_x = 0
m_y = 0
hsv = [0, 0, 0]
lower_hsv = np.array([0, 0, 0])
upper_hsv = np.array([0, 0, 0])


def on_mouse(event, x, y, flag, param):
	global m_x, m_y, hsv_frame, hsv, upper_hsv, lower_hsv
	if event == cv2.EVENT_LBUTTONDOWN:
		m_x = x
		m_y = y
		hsv = get_hsv_point(hsv_frame, x, y)
		upper_hsv, lower_hsv = set_hsv_thresh(hsv)
	return None


def get_hsv_point(hsv_frame, x, y):
	return hsv_frame[x, y]


def set_hsv_thresh(hsv):
	upper_hsv = np.array([hsv[0]*(1+TOLERANCE), hsv[1]*(1+TOLERANCE), hsv[2]*(1+TOLERANCE)])
	lower_hsv = np.array([hsv[0]*(1-TOLERANCE), hsv[1]*(1-TOLERANCE), hsv[2]*(1-TOLERANCE)])
	return upper_hsv, lower_hsv


cv2.namedWindow("cam")
cv2.namedWindow("hsv")
cv2.setMouseCallback("hsv", on_mouse)
cam = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:

	ret_cam, frame = cam.read()

	frame = cv2.GaussianBlur(frame, (11, 11), 5)

	hsv_frame = frame
	# hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)

	print(m_x, m_y, hsv[0], hsv[1], hsv[2])

	mask_frame = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)

	# mask_frame = opening_op(mask_frame)
	# mask_frame = cv2.erode(mask_frame, K_SIZE, iterations=2)
	# mask_frame = cv2.dilate(mask_frame, K_SIZE, iterations=2)

	# draw_contours(frame, mask_frame, CONTOURS_COLOR)

	cv2.imshow("hsv", hsv_frame)
	cv2.imshow("cam", frame)
	cv2.imshow("mask", mask_frame)


cv2.destroyAllWindows()
cam.release()





