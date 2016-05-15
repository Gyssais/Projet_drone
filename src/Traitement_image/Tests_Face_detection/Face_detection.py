# -*- coding: utf-8 -*-

import numpy as np
import cv2

# Chargement des Classifiers : donnees obtenues par l'entrainement de l'algorithme sur un ensemble d'images
# Des Classifiers pre-entraines pour la detection de visages et d'yeux sont inclus dans openCV
face_cascade = cv2.CascadeClassifier('/home/julien/Téléchargements/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/julien/Téléchargements/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')

# Ouverture de l'image a traiter
img = cv2.imread('Mon_image.jpg')
# Affichage de l'image avant traitement
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
