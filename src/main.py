from color_calib import *
from color_detect import *

if __name__ == '__main__':

    color_detect = ColorDetect()
    color_detect.initialize()

    track_bar = HSVToleranceCalib()
    track_bar.create()

    cam = cv2.VideoCapture(0)

    while cv2.waitKey(1) != ord('q'):
        _, frame = cam.read()
        color_detect.set_tolerance(track_bar.get_tolerance())
        color_detect.run(frame)
        color_detect.draw_contours()
        color_detect.display()

    cam.release()
    cv2.destroyAllWindows()
