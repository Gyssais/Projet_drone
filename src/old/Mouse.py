import cv2


def on_mouse(event, x, y, flag, param):
	global m_x, m_y
	if event == cv2.EVENT_LBUTTONDOWN:
		m_x = x
		m_y = y
	return flag


if __name__ == "__main__":
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("cam")
	cv2.setMouseCallback("cam", on_mouse)

	while cv2.waitKey(1) == -1:
		ret_cam, frame = cam.read()
		cv2.imshow("cam", frame)
		print(m_x, m_y)

	cv2.destroyAllWindows()
	cam.release()






