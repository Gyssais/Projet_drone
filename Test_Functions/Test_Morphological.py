import cv2
import numpy as np

# Black pixel
MAX_PIXEL_VAL = 255

img = cv2.imread("Fruits.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, normal_thresh = cv2.threshold(img_gray, MAX_PIXEL_VAL/2, MAX_PIXEL_VAL, cv2.THRESH_BINARY)

# Different morphological operations
kernel= cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# erd_img = cv2.erode(normal_thresh, kernel)
# dil_img = cv2.dilate(normal_thresh, kernel)
open_img = cv2.morphologyEx(normal_thresh, cv2.MORPH_OPEN, kernel)
# close_img = cv2.morphologyEx(normal_thresh, cv2.MORPH_CLOSE, kernel)

# Show images
cv2.imshow("img", img)
# cv2.imshow("normal_thresh", normal_thresh)
# cv2.imshow("erode", erd_img)
# cv2.imshow("dilate", dil_img)
cv2.imshow("open", open_img)
# cv2.imshow("close", close_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

