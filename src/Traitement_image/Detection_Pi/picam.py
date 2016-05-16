import time
from color_detect import *
from color_calib import *
from apple_detect import *
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread

STREAM_FORMAT = 'bgr'


class PiCam:

    def __init__(self):
        self._cam = PiCamera()
        self._raw_capt = None
        self._img = None
        self.apple_detector = AppleDetect()

    def initialize(self, resolution=(320, 240)):
        self._cam.resolution = resolution
        self._cam.awb_mode = 'tungsten'
        self._raw_capt = PiRGBArray(cam, size=resolution)
        self.apple_detector.set_all_color()
        time.sleep(1)

    def get_img(self):
        return self._img

    def detect_n_send_info(self, img):
        self.apple_detector.detect_and_filter(img)
        f = open('report.txt', 'w')
        for i in iter(self.apple_detector.info_apples_fit):
            cv2.circle(img, i[0], i[1], i[2], thickness=-1)
            f.write(repr(i[0][0])+','+
                    repr(i[0][1])+','+
                    repr(i[1]   )+','+
                    repr(i[2][0])+','+
                    repr(i[2][1])+','+
                    repr(i[2][2])+','+
                    repr(self.apple_detector.nb_apples_found)+','+
                    repr(self.apple_detector.nb_apples_fit)+'\n')
        cv2.imwrite('img.jpeg', img) 
        self.apple_detector.reset_info()
        cv2.imshow('cam', img)
        f.close()
        print 'nb de pommes detectees: ', self.apple_detector.nb_apples_found
        print 'nb de pommes mures: ', self.apple_detector.nb_apples_fit
        self.apple_detector.reset_info()

    def run_no_detect(self):
        while cv2.waitKey(1) != ord('q'):
            self._cam.capture(self._raw_capt, format=STREAM_FORMAT, use_video_port=True)
            self._img = self._raw_capt.array
            self._raw_capt.truncate(0)
    
    def run(self):
        # capture frames from the camera
        while cv2.waitKey != ord('q'):
            self._cam.capture(self._raw_capt, format=STREAM_FORMAT, use_video_port=True)
            img = self._raw_capt.array
            # clear previous stream
            self.apple_detector.detect_and_filter(img)
            f = open('report.txt', 'w')
            for i in iter(self.apple_detector.info_apples_fit):
                cv2.circle(img, i[0], i[1], i[2], thickness=-1)
                f.write(repr(i[0][0])+','+
                        repr(i[0][1])+','+
                        repr(i[1]   )+','+
                        repr(i[2][0])+','+
                        repr(i[2][1])+','+
                        repr(i[2][2])+','+
                        repr(self.apple_detector.nb_apples_found)+','+
                        repr(self.apple_detector.nb_apples_fit)+'\n')   
            cv2.imwrite('img.jpeg', img) 
            self.apple_detector.reset_info()
            cv2.imshow('cam', img)
            f.close()
            self._raw_capt.truncate(0)
            print 'nb de pommes detectees: ', self.apple_detector.nb_apples_found
            print 'nb de pommes mures: ', self.apple_detector.nb_apples_fit
            self.apple_detector.reset_info()

            # if the `q` key was pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                    break
    

if __name__ == '__main__':
    cam = PiCam()
    cam.initialize()
    Thread(target=cam.run).start()
    while True:
        try:
            img = cam.get_img()
            cam.detect_n_send_info(img)
            cv2.imshow('cam', img)
        except cv2.error:
            print 'no frame yet'




    
