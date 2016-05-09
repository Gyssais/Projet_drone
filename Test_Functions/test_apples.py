import numpy as np
import cv2

nb_apples_found = 0
nb_apples_fit = 0
upper_color = [0, 0, 0]
lower_color = [0, 0, 0]
found = False
tolerance = 0.25
red = [13, 18, 117]

for i in range(3):
    upper_color[i] = red[i]*(1+tolerance)
    lower_color[i] = red[i]*(1-tolerance)

apple_cascade = cv2.CascadeClassifier('cascade_pomme3.xml')

img = cv2.imread('../img/many_apples.jpg')
test = np.zeros(img.shape, np.uint8)
mask = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
apples = apple_cascade.detectMultiScale(gray, 1.3, 5)

try:
    nb_apples_found = apples.size/4
except AttributeError:
    nb_apples_found = 0

for (x, y, w, h) in apples:

    cv2.circle(mask, center=(x+(w/2), y+(h/2)), radius=(w+h)/5, color=(255, 255, 255), thickness=-1)
    color = cv2.mean(img, mask)
    for i in range(3):
        if upper_color[i] > color[i] > lower_color[i]:
            found = True
        else:
            found = False
    if found:
        nb_apples_fit += 1
        cv2.circle(test, center=(x+(w/2), y+(h/2)), radius=(w+h)/5, color=color, thickness=-1)
    found = False

    cv2.circle(mask, center=(x+(w/2), y+(h/2)), radius=(w+h)/5, color=(0, 0, 0), thickness=-1)

cv2.imshow('img', img)
cv2.imshow('test', test)

print 'nb_apples_found = ', nb_apples_found
print 'nb_apples_fit = ', nb_apples_fit

cv2.waitKey(0)
