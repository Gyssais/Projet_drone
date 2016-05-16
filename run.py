from src.Traitement_image.Detection_Pi.picam import *
import dcapi
import autopilot

if __name__ == '__main__':

    cam = PiCam()
    cam.initialize()
    dcapi.init()
    
    Thread(target=cam.run, name='detector').start()
    Thread(target=autopilot.test_ch, name='autopilot').start()




