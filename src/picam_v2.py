from picamera.array import PiRGBArray
from picamera import PiCamera
from constance import *


class PiVideoStream:

    def __init__(self, resolution=(640, 480), frame_rate=32, stream_format='bgr'):
        # initialize the camera and stream
        self._camera = PiCamera()
        self._camera.resolution = resolution
        self._camera.frame_rate = frame_rate
        self._rawCapture = PiRGBArray(self._camera, size=resolution)
        self._stream = self._camera.capture_continuous(self._rawCapture, format=stream_format, use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self._frame = None
        self._stop = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.run, args=()).start()

    def run(self):
        # keep looping infinitely until the thread is stopped
        for f in self._stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self._frame = f.array
            self._rawCapture.truncate(0)

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self._stop:
                self._stream.close()
                self._rawCapture.close()
                self._camera.close()
                break

    def read(self):
        # return the frame most recently read
        return self._frame

    def stop(self):
        # indicate that the thread should be stopped
        self._stop = True


if __name__ == '__main__':

    picam = PiVideoStream()
    Thread(target=picam.run()).start()

    while cv2.waitKey(1) != ord('q'):
        try:
            cv2.imshow('img', picam.read())
        except cv2.error:
            print 'No frame yet'

    cv2.destroyAllWindows()
    picam.stop()
