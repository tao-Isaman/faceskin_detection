# TechVidvan Object detection of similar color
import cv2
import numpy as np

def detect_yellow(img: bytes) -> bytes:
    
    cv2_img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    # Reading the image
    # img = cv2.imread('image.png')

    # convert to hsv colorspace
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower bound and upper bound for Green color
    lower_bound = np.array([0, 0, 160])   
    upper_bound = np.array([100, 255, 255])

    # find the colors within the boundaries
    mask = cv2.inRange(cv2_img, lower_bound, upper_bound)
    cv2.imwrite('yellow.jpg', mask)
    
    image_bytes = cv2.imencode('.jpg', mask)
    
    return image_bytes

