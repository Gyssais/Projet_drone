import cv2
import numpy as np
from ColorCalib import *
from Constances import *

CAM_WIN = 'cam'
FILTERED_WIN = 'filtered'


class ColorDetect:

	def __init__(self):
		self._click_position = (0, 0)
		self._upper_color = np.array([0, 0, 0])
		self._lower_color = np.array([0, 0, 0])
		self._tolerance = np.array([0.25, 0.25, 0.25])
		self._cam = None
		self._cam_frame = None
		self._filtered_frame = None
		self._contours = None

	def initialize(self, cam):
		cv2.namedWindow(CAM_WIN)
		cv2.namedWindow(FILTERED_WIN)
		cv2.setMouseCallback(FILTERED_WIN, self._on_mouse)
		self._cam = cv2.VideoCapture(cam)

	def run(self):
		_, self._cam_frame = self._cam.read()
		self._cam_frame = cv2.GaussianBlur(self._cam_frame, (11, 11), 5)
		self._filtered_frame = cv2.cvtColor(self._cam_frame, cv2.COLOR_BGR2HSV)
		self._set_pixel_color_thresh(self._filtered_frame[self._click_position])
		mask_frame = cv2.inRange(self._filtered_frame, self._lower_color, self._upper_color)
		mask_frame = self._opening_op(mask_frame, K_SIZE)
		_, self._contours, _ = cv2.findContours(mask_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	def set_tolerance(self, val):
		self._tolerance = val

	def _set_pixel_color_thresh(self, pixel_color):
		# Set lower and upper thresholds
		self._upper_color = np.array([pixel_color[0]*(1+self._tolerance[0]),
		                              pixel_color[1]*(1+self._tolerance[1]),
		                              pixel_color[2]*(1+self._tolerance[2])])
		self._lower_color = np.array([pixel_color[0]*(1-self._tolerance[0]),
		                              pixel_color[1]*(1-self._tolerance[1]),
		                              pixel_color[2]*(1-self._tolerance[2])])

	def _on_mouse(self, event, x, y, flag, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			# Get mouse position
			self._click_position = (y, x)

	@staticmethod
	def _opening_op(img_thresh, k_size):
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k_size)
		open_img = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
		return open_img
