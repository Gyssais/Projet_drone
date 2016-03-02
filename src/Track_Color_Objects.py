import cv2
import numpy as np
from Contours import *
from Constances import *


pixel_color = [0, 0, 0]
lower_pixel_color = np.array([0, 0, 0])
upper_pixel_color = np.array([0, 0, 0])


# Return a pixel information at a point (x,y)
def get_pixel_color_point(filtered_frame, x, y):
	return filtered_frame[y, x]


# Return two threshold values acceptable for a color within a tolerance of TOLERANCE
def set_pixel_color_thresh(pixel_color):
	global upper_pixel_color, lower_pixel_color
	# Set lower and upper thresholds
	upper_pixel_color = np.array([pixel_color[0]*(1+TOLERANCE), pixel_color[1]*(1+TOLERANCE), pixel_color[2]*(1+TOLERANCE)])
	lower_pixel_color = np.array([pixel_color[0]*(1-TOLERANCE), pixel_color[1]*(1-TOLERANCE), pixel_color[2]*(1-TOLERANCE)])
	return upper_pixel_color, lower_pixel_color


# Set mouse left click event, each left click will return the mouse's position (x,y) and the pixel's three color values
def on_mouse(event, x, y, flag, param):
	global filtered_frame, pixel_color, upper_pixel_color, lower_pixel_color
	if event == cv2.EVENT_LBUTTONDOWN:
		# Get mouse position and update color thresholds
		pixel_color = get_pixel_color_point(filtered_frame, x, y)
		upper_pixel_color, lower_pixel_color = set_pixel_color_thresh(pixel_color)
		# Print on-click information
		print(x, y, pixel_color[0], pixel_color[1], pixel_color[2])
	return None


if __name__ == '__main__':

	# Create windows for actual image, filtered image and masked image
	cv2.namedWindow("cam")
	cv2.namedWindow("filtered")
	cv2.namedWindow("mask")

	# Set mouse handler event on the filtered window
	cv2.setMouseCallback("filtered", on_mouse)

	# Initialize the camera
	cam = cv2.VideoCapture(0)

	# Loop forever
	while cv2.waitKey(1) == -1:

		# Read image from camera and get the next image
		ret_cam, frame = cam.read()

		# Blur image in order to remove some noises
		frame = cv2.GaussianBlur(frame, (11, 11), 5)

		# Filter actual image
		filtered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# Mask image, only keep the colors inside the thresholds
		mask_frame = cv2.inRange(filtered_frame, lower_pixel_color, upper_pixel_color)

		# Simply just draw contours
		draw_contours(frame, mask_frame, GREEN, CONTOURS_THICKNESS)

		# Show all three windows
		cv2.imshow("filtered", filtered_frame)
		cv2.imshow("cam", frame)
		cv2.imshow("mask", mask_frame)

	# Escape
	cv2.destroyAllWindows()
	cam.release()





