import cv2
import numpy as np
from Constances import *
from ColorCalib import *


click_position = (0, 0)
upper_color = np.array([0, 0, 0])
lower_color = np.array([0, 0, 0])
tolerance = np.array([0.25, 0.25, 0.25])


# Return two threshold values acceptable for a color within a tolerance of TOLERANCE
def set_pixel_color_thresh(pixel_color):
	global upper_color, lower_color, tolerance
	# Set lower and upper thresholds
	upper_color = np.array([pixel_color[0]*(1+tolerance[0]), pixel_color[1]*(1+tolerance[1]), pixel_color[2]*(1+tolerance[2])])
	lower_color = np.array([pixel_color[0]*(1-tolerance[0]), pixel_color[1]*(1-tolerance[1]), pixel_color[2]*(1-tolerance[2])])


# On mouse event function, which is defined to take 5 params, no more, no less
def on_mouse(event, x, y, flag, param):
	global click_position
	if event == cv2.EVENT_LBUTTONDOWN:
		# Get mouse position
		click_position = (y, x)
		print 'position = (', x, ',', y, ')'


def opening_op(img_thresh, k_size):
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k_size)
	open_img = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
	return open_img


if __name__ == '__main__':

	# Create tolerance track bar
	track_bar = ColorCalib()
	track_bar.create()

	# Create windows for actual image, filtered image and masked image
	cv2.namedWindow("cam")
	cv2.namedWindow("filtered")

	# Set mouse handler event on the filtered window
	cv2.setMouseCallback("filtered", on_mouse)

	# Initialize the camera
	cam = cv2.VideoCapture(0)

	# Loop forever
	while cv2.waitKey(1) != ord('q'):

		# Get tolerance value
		tolerance = track_bar.get_tolerance()

		# Read image from camera and get the next image
		ret_cam, frame = cam.read()

		# Blur image in order to remove some noises
		frame = cv2.GaussianBlur(frame, (11, 11), 5)

		# Filter actual image
		filtered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		set_pixel_color_thresh(filtered_frame[click_position])

		# Mask image, only keep the colors inside the thresholds
		mask_frame = cv2.inRange(filtered_frame, lower_color, upper_color)

		# Some morph operations for removing noises
		mask_frame = opening_op(mask_frame, K_SIZE)

		# Simply just draw big contours
		_, contours, _ = cv2.findContours(mask_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		nb_object = len(contours)
		if len(contours) != 0:
			for contour_nb in xrange(len(contours)):
				# Finding the center of a contour
				M = cv2.moments(contours[contour_nb])
				if M['m00'] > 40*40:
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
					cv2.circle(frame, (cx, cy), 3, RED, thickness=3)
					cv2.drawContours(frame, contours, contour_nb, GREEN, thickness=CONTOURS_THICKNESS)
					mean = cv2.mean(frame, mask=mask_frame)
					# print mean

		# Show all three windows
		cv2.imshow("filtered", filtered_frame)
		cv2.imshow("cam", frame)

	# Press 'q' to exit
	cv2.destroyAllWindows()
	cam.release()
