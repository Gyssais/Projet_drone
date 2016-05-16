from src.Traitement_image.Detection_Pi.picam import *
import dcapi

if __name__ == '__main__':

    cam = PiCam()
    cam.initialize()
    dcapi.init()
    
    Thread(target=cam.run, name='detector').start()
    Thread(target=dcapi.run, name='autopilot').start()




