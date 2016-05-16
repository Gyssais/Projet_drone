from picam_v2 import *
from apple_detect import *
from color_calib import ColorPickerBGR

if __name__ == '__main__':

    video_stream = PiVideoStream()
    apple_detector = AppleDetect()
    color_picker = ColorPickerBGR()

    color_picker.create()

    Thread(target=video_stream.run, name='pi_camera').start()
    Thread(target=color_picker.set_color, name='color_picker').start()
