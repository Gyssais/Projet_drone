import cv2
from Constances import *

# Recommended value by doc
K_SIZE = (13, 13)


def opening_op(img_thresh):
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, K_SIZE)
	open_img = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
	return open_img


if __name__ == "__main__":
	img = cv2.imread("Fruits.jpg")
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, img_thresh = cv2.threshold(img_gray, MAX_PIXEL_VAL/2, MAX_PIXEL_VAL, cv2.THRESH_BINARY)
	cv2.imshow("open_op", opening_op(img_thresh))
	cv2.waitKey(0)
	cv2.destroyAllWindows()
