# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time


while cv2.waitKey(1) != ord('q'):
    img = np.zeros((240, 320, 3), np.uint8)
    f = open('report.txt', 'r')
    Pas_pomme = true
    for line in f:
	Pas_pomme = false
	print line
    	info = line.strip().split(',')
	cv2.circle(img, (int(info[0]), int(info[1])), int(info[2]), (float(info[3]), float(info[4]), float(info[5])), thickness=-1)
    	print 'Nombre de pommes détectées : '+info[6]
    	print 'Nombre de pommes mures (rouge) : '+info[7]

    if Pas_pomme:
    	print 'Nombre de pommes détectées : 0'
    	print 'Nombre de pommes mures (rouge) : 0'	
    cv2.imshow('img', img)
    time.sleep(1)


