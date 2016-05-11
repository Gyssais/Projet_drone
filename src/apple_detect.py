from constance import *


class AppleDetect:

    def __init__(self, cascade='cascade_pomme3.xml'):
        self._apples = None
        self._cascade = cv2.CascadeClassifier(cascade)
        self.nb_apples_found = 0
        self.nb_apples_fit = 0
        self.info_apples_fit = []
        self._upper_color = [0, 0, 0]
        self._lower_color = [0, 0, 0]

    def detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self._apples = self._cascade.detectMultiScale(gray, 1.3, 5)
        try:
            self.nb_apples_found = self._apples.size / 4
        except AttributeError:
            self.nb_apples_found = 0

    def detect_and_filter(self, img):
        self.detect(img)
        mask = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
        found = False
        for (x, y, w, h) in self._apples:
            cv2.circle(mask, center=(x+(w/2), y+(h/2)), radius=(w+h)/5, color=WHITE, thickness=-1)
            color = cv2.mean(img, mask)
            for i in range(3):
                if self._upper_color[i] > color[i] > self._lower_color[i]:
                    found = True
                else:
                    found = False
            if found:
                self.nb_apples_fit += 1
                self.info_apples_fit.append([(x+(w/2), y+(h/2)), (w+h)/5, color])
            found = False
            cv2.circle(mask, center=(x+(w/2), y+(h/2)), radius=(w+h)/5, color=BLACK, thickness=-1)

    def set_color_thresh(self, color, tolerance):
        for i in range(3):
            self._upper_color[i] = color[i]*(1+tolerance)
            self._lower_color[i] = color[i]*(1-tolerance)

    def set_all_color(self):
        self._upper_color = WHITE
        self._lower_color = BLACK

    def reset_info(self):
        self.info_apples_fit = []


if __name__ == '__main__':

    img = cv2.imread('../img/many_apples.jpg')

    apple_detector = AppleDetect()
    apple_detector.set_all_color()
    apple_detector.detect_and_filter(img)

    for i in iter(apple_detector.info_apples_fit):
        cv2.circle(img, i[0], i[1], i[2], thickness=-1)

    cv2.imshow('img', img)
    cv2.waitKey(0)