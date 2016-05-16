import cv2

if __name__ == '__main__':

	face_cascade = cv2.CascadeClassifier('../Test_Functions/haarcascade_frontalface_alt2.xml')

	cv2.namedWindow('cam')
	camera = cv2.VideoCapture(0)

	while cv2.waitKey(1) != ord('q'):
		_, img = camera.read()
		cv2.imshow('cam', img)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
		cv2.imshow('cam', img)

	cv2.destroyAllWindows()
	camera.release()
