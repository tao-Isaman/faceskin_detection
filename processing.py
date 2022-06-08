# TechVidvan Object detection of similar color
import cv2
import numpy as np

from model.color_parameter import ColorParameter

def detect_color(color_parameter: ColorParameter) -> bytes:
    # Reading the image
    cv2_img = cv2.imdecode(np.frombuffer(color_parameter.img, np.uint8), cv2.IMREAD_COLOR)
    
    # convert to hsv color space
    hsv = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2HSV)

    # lower bound and upper bound for Green color
    # lower boundary RED color range values; Hue (0 - 10)
    lower_bound = np.array([color_parameter.h_min, color_parameter.s_min, color_parameter.v_min])   
    upper_bound = np.array([color_parameter.h_max, 255, 255])

    if color_parameter.check_red:
        # upper boundary RED color range values; Hue (160 - 180)
        lower_bound_red = np.array([color_parameter.h_red_min, color_parameter.s_min, color_parameter.v_min])   
        upper_bound_red = np.array([color_parameter.h_red_max, 255, 255])

        lower_mask = cv2.inRange(hsv, lower_bound, upper_bound)
        upper_mask = cv2.inRange(hsv, lower_bound_red, upper_bound_red)

        mask = lower_mask + upper_mask
    else:
        # find the colors within the boundaries
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

    cv2.imwrite('mask.jpg', mask)
    
    img_bytes_mask = cv2.imencode('.jpg', mask)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(cv2_img, cv2_img, mask= mask)
    cv2.imwrite('res.jpg', res)

    img_bytes_res = cv2.imencode('.jpg', res)
    
    return img_bytes_mask, img_bytes_res

