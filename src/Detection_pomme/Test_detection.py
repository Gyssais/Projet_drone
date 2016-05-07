# -*- coding: utf-8 -*-

import numpy as np
import cv2

# Chargement des Classifiers : donnees obtenues par l'entrainement de l'algorithme sur un ensemble d'images
# Des Classifiers pre-entraines pour la detection de visages et d'yeux sont inclus dans openCV
apple_cascade = cv2.CascadeClassifier('cascade_pomme3.xml')
#eye_cascade = cv2.CascadeClassifier('/home/julien/Téléchargements/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')

#capture et detecter a partir des images courrante d'un camera
cam = cv2.VideoCapture(0)


# Ouverture de l'image a traiter(capture et detecter a partir d'une image donnée)
#img = cv2.imread('img_test/applePos90.jpg')
# Affichage de l'image avant traitement

compteur = 0
x_prec = 0
y_prec = 0
p_tab = np.array([[0, 0, 0]]) # (x, y, compteur) pour chaque pomme detectee precedement
trouve = []
########
#ces deux lignes uniquement pour capture courrante de video
while cv2.waitKey(1) != ord('q'):
   _, img =cam.read()
########

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   apples = apple_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in apples:

       trouve = false
       for i in p_tab.size[0] :
       		if (p_tab[i][0] < x+100 and x-100 < p_tab[i][0] and p_tab[i][1] < y+100 and y-100 < p_tab[i][1]) :
           		#compteur = compteur + 1
	   		p_tab[i][2] = p_tab[i][2] + 1
			trouve = trouve + [i]

       		if p_tab[i][2] > 10:
       			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       			font = cv2.FONT_HERSHEY_SIMPLEX
       			cv2.putText(img,'Pomme'+str(i),(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)

    for n in trouve:
    	new_p_tab = np

       #x_prec = x
       #y_prec = y
       #roi_gray = gray[y:y+h, x:x+w]
       #roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

   cv2.imshow('img',img)

cv2.destroyAllWindows()
