from apple_detect import *
from color_calib import *


class WebcamStream:

    def __init__(self):
        self._cam = cv2.VideoCapture(0)
        self._frame = None
        self._stop = False

    def get_frame(self):
        return self._frame

    def stop(self):
        self._stop = True

    def run(self):
        while self._stop is False:
            _, self._frame = self._cam.read()


if __name__ == '__main__':

    apple_detector = AppleDetect()
    color_picker = ColorPickerBGR()
    cam = WebcamStream()

    color_picker.create()
    apple_detector.set_all_color()

    Thread(target=cam.run).start()
    time.sleep(2)

    while cv2.waitKey(1) != ord('q'):
        try:
            img = cam.get_frame()
            apple_detector.detect_and_filter(img)
            for i in iter(apple_detector.info_apples_fit):
                cv2.circle(img, i[0], i[1], i[2], thickness=-1)
            apple_detector.reset_info()
            cv2.imshow('img', img)
            color_picker.set_color()
        except cv2.error:
            print 'No frame'

    cam.stop()
    cv2.destroyAllWindows()
