from src.Traitement_image.Detection_Pi.picam import *


if __name__ == '__main__':

    cam = PiCam()
    cam.initialize()

    Thread(target=cam.run, name='detector').start()
    Thread(target=gpio.run, name='gpio').start()




