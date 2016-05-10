import time
from color_detect import *
from color_calib import *
from apple_detect import *
from picamera.array import PiRGBArray
from picamera import PiCamera

STREAM_FORMAT = 'bgr'


class PiCam:
    def __init__(self):
        self._cam = PiCamera()
        self._raw_capt = None
        self.apple_detector = AppleDetect()

    def initialize(self, resolution=(640, 480), fps=32):
        self._cam.resolution = resolution
        self._cam.framerate = fps
        self._cam.awb_mode = 'tungsten'
        self._raw_capt = PiRGBArray(cam, size=resolution)
        time.sleep(1)

    def run(self, func=None):
        # capture frames from the camera
        for frame in self._cam.capture_continuous(self._raw_capt, format=STREAM_FORMAT, use_video_port=True):

            img = frame.array
            if func:
                func(img)
            # clear previous stream
            self.apple_detector.set_all_color()
            self.apple_detector.detect_and_filter(img)
            for i in iter(self.apple_detector.info_apples_fit):
                cv2.circle(img, i[0], i[1], i[2], thickness=-1)
            cv2.imshow('cam', img)
            self._raw_capt.truncate(0)

            # if the `q` key was pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break


if __name__ == '__main__':
    cam = PiCam()
    cam.initialize()
    cam.run()
