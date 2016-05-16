import cv2

# Constant names
TRACK_BARS_WINDOW_NAME = "Track bars"
H_MIN_NAME = "H_Min"
H_MAX_NAME = "H_Max"
S_MIN_NAME = "S_Min"
S_MAX_NAME = "S_Max"
V_MIN_NAME = "V_Min"
V_MAX_NAME = "V_Max"
MIN = 0
MAX = 255


# Null function
def nothing(x):
    pass


# Function create HSV track bars
def create_hsv_track_bars():
    cv2.namedWindow(TRACK_BARS_WINDOW_NAME)
    cv2.createTrackbar(H_MIN_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    cv2.createTrackbar(H_MAX_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    cv2.createTrackbar(S_MIN_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    cv2.createTrackbar(S_MAX_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    cv2.createTrackbar(V_MIN_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    cv2.createTrackbar(V_MAX_NAME, TRACK_BARS_WINDOW_NAME, MIN, MAX, nothing)
    return None


# Get HSV values from the track bars
def get_hsv_val():
    h_min = cv2.getTrackbarPos(H_MIN_NAME, TRACK_BARS_WINDOW_NAME)
    h_max = cv2.getTrackbarPos(H_MAX_NAME, TRACK_BARS_WINDOW_NAME)
    s_min = cv2.getTrackbarPos(S_MIN_NAME, TRACK_BARS_WINDOW_NAME)
    s_max = cv2.getTrackbarPos(S_MAX_NAME, TRACK_BARS_WINDOW_NAME)
    v_min = cv2.getTrackbarPos(V_MIN_NAME, TRACK_BARS_WINDOW_NAME)
    v_max = cv2.getTrackbarPos(V_MAX_NAME, TRACK_BARS_WINDOW_NAME)
    return h_min, h_max, s_min, s_max, v_min, v_max








