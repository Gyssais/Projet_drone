# import src.Pilote_automatique.dcapi
from src.Pilote_automatique.autopilot import *
from src.Traitement_image.Detection_Pi.picam import *

if __name__ == '__main__':

    cam = PiCam()
    cam.initialize()
    dcapi.init()
    
    Thread(target=cam.run).start()
    Thread(target=test_ch, name='autopilot').start()




