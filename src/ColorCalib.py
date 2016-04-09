import cv2

WINDOW_NAME = 'Color calibrator'
H_NAME = 'Hue tolerance'
S_NAME = 'Saturation tolerance'
V_NAME = 'Value tolerance'

MIN_TOLERANCE = 0
MAX_TOLERANCE = 100


class ColorCalib:

	def __init__(self):
		self._h_tol_val = 0
		self._s_tol_val = 0
		self._v_tol_val = 0

	def on_change_h(self, pos):
		self._h_tol_val = pos/100.0

	def on_change_s(self, pos):
		self._s_tol_val = pos/100.0

	def on_change_v(self, pos):
		self._v_tol_val = pos/100.0

	def get_tolerance(self):
		print 'tolerance = ', [self._h_tol_val, self._s_tol_val, self._v_tol_val]
		return [self._h_tol_val, self._s_tol_val, self._v_tol_val]

	def create(self):
		cv2.namedWindow(WINDOW_NAME)
		cv2.createTrackbar(H_NAME, WINDOW_NAME, MIN_TOLERANCE, MAX_TOLERANCE, self.on_change_h)
		cv2.createTrackbar(S_NAME, WINDOW_NAME, MIN_TOLERANCE, MAX_TOLERANCE, self.on_change_s)
		cv2.createTrackbar(V_NAME, WINDOW_NAME, MIN_TOLERANCE, MAX_TOLERANCE, self.on_change_v)


if __name__ == '__main__':

	track_bar = ColorCalib()
	track_bar.create()

	while cv2.waitKey(1) != ord('q'):
		print track_bar.get_tolerance()

	cv2.destroyAllWindows()

	my_file = 'image' + str(1) + '.jpg'
	print my_file

