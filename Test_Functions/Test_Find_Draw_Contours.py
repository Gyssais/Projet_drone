import numpy as np
import cv2
from matplotlib import pyplot as plt


im = cv2.imread('apple.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

cv2.imshow("img", im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Uncomment this for showing image using pyplot
# plt.imshow(im), plt.show()

