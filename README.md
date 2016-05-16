# Projet_drone
Projet de drone d'aide à l'agriculture. Comprend :
 - Algorithme de reconnaissance de formes et de couleurs appliqué à la détection de pommes.<br \>
 - Pilote automatique du drone : commande du drone via une Raspberry Pi, sans utilisation de la télécommande. <br \>
Requis : Python 2.7 + OpenCV 3.1.0 + Numpy 1.11.0rc1

Julien Chatelais, Xue Zhang, Lilian Cabé, Théophile Leurent, Vu Hoang Phan. INSA Toulouse, 2016.

Le fichier apple_detect.py s'exécute sur la Raspberry. Il permet de réaliser la détection de pommes et d'en extraire la couleur. Il écrit le résultat du traitement dans le fichier report.txt.
Les fichiers comPi.sh et affichage_coul.py sont à exécuter sur le PC pour récupérer, chaque seconde, les résultats du traitement d'image.
