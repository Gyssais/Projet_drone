
#!/bin/bash

while true
do
    sshpass -p 'raspberry' scp pi@192.168.43.94:~/Projet_drone/Traitement_image/Detection_Pi/report.txt ./
    cat report.txt
    sshpass -p 'raspberry' scp pi@192.168.43.94:~/Projet_drone/Traitement_image/Detection_Pi/img.jpeg ./
    sleep 1
done
