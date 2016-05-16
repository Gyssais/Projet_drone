
#!/bin/bash

while true
do
    sshpass -p 'raspberry' scp pi@192.168.43.94:~/Projet_drone/src/report.txt ./
    cat report.txt
    sleep 1
done
