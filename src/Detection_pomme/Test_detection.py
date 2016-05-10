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

#compteur = 0
#x_prec = 0
#y_prec = 0
# Initialisation necessaire pour definir la taille du tableau
p_tab = np.array([[0, 0, 0]]) # (x, y, compteur) pour chaque pomme detectee precedement
#trouve = [] # vecteur des pommes trouves dans l'image : liste des indices de p_tab contenant une pomme trouvee sur l'image courante


#ces deux lignes uniquement pour capture courrante de video
while cv2.waitKey(1) != ord('q'):
   _, img =cam.read() # Lecture d'un image à partir du flux video

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Transformation de l'image en niveaux de gris
   apples = apple_cascade.detectMultiScale(gray, 1.3, 5) # detection des pommes

   # Initialisation necessaire pour definir la taille du tableau
   new_p_tab = np.array([[0, 0, 0]])

   for (x,y,w,h) in apples: # Pour chaque pomme detectee

       trouve = False

       # Recherche si pomme detectee deja vue avant
       for i in range(0, p_tab.shape[0]) : # Pour chaque pomme detectee precedemment :
       		if (p_tab[i][0] < x+100 and x-100 < p_tab[i][0] and p_tab[i][1] < y+100 and y-100 < p_tab[i][1]) : # 
           		#compteur = compteur + 1
	   		p_tab[i][2] = p_tab[i][2] + 1 # Incremente compteur de vues consecutives
			# Ajout de la pomme trouvee dans le nouveau tableau
			new_p_tab = np.vstack([new_p_tab, p_tab[i]])
			# Pomme vue sur plusieurs images a la suite : affichage de la detection
       			if p_tab[i][2] > 5:
       				img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       				font = cv2.FONT_HERSHEY_SIMPLEX
       				cv2.putText(img,'Pomme'+str(i),(x,y), font, 1,(255,0,0),2,cv2.LINE_AA)
			break
			trouve = True

       if (not trouve):
		# Ajout d'un nouvelle pomme dans le nouveau tableau
		new_p_tab = np.vstack([new_p_tab, [x, y, 1]])
    
   # Suppression de la première et 2eme ligne, creee a l'initialisation
   np.delete(new_p_tab, 0, 0) 
   # creation de p_tab
   p_tab = new_p_tab


   cv2.imshow('img',img)

cv2.destroyAllWindows()
