import cv2
from Constances import *


def draw_contours(img, img_thresh, contours_colors, contours_thickness):
	_, contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, ALL_CONTOURS, contours_colors, thickness=contours_thickness)
	return contours


if __name__ == "__main__":
	img = cv2.imread("Fruits.jpg")
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, img_thresh = cv2.threshold(img_gray, MAX_PIXEL_VAL/2, MAX_PIXEL_VAL, cv2.THRESH_BINARY)
	img = draw_contours(img, img_thresh, GREEN)
	cv2.imshow("", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


