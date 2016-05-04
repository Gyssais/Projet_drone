import time
from color_detect import *
from color_calib import *
from picamera.array import PiRGBArray
from picamera import PiCamera

STREAM_FORMAT = 'bgr'


class PiCam:
    def __init__(self):
        self._cam = PiCamera()
        self._raw_capt = None

    def initialize(self, resolution=(640, 480), fps=32):
        self._cam.resolution = resolution
        self._cam.framerate = fps
        self._raw_capt = PiRGBArray(cam, size=resolution)
        time.sleep(1)

    def run(self, func=None):
        # capture frames from the camera
        for frame in self._cam.capture_continuous(self._raw_capt, format=STREAM_FORMAT, use_video_port=True):

            img = frame.array
            if func:
                func(img)
            # clear previous stream

            cv2.imshow('cam', img)
            self._raw_capt.truncate(0)

            # if the `q` key was pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break


if __name__ == '__main__':
    cam = PiCam()
    cam.initialize()

    color_detect = ColorDetect()
    color_detect.initialize()

    track_bar = ColorCalib()
    track_bar.create()


    def img_proc(img):
        color_detect.set_tolerance(track_bar.get_tolerance())
        color_detect.run(frame)
        color_detect.draw_contours()
        color_detect.display()


    cam.run(img_proc)
