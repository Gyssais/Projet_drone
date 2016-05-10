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