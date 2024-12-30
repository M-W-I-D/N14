import cv2
import numpy as np

# Tăng sáng
def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = cv2.add(hsv[:, :, 2], value)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Làm mờ nền
def blur_background(image):
    blurred = cv2.GaussianBlur(image, (21, 21), 0)
    return blurred

# Hiệu ứng hoạt hình
def cartoon_filter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    blurred = cv2.medianBlur(image, 7)
    return cv2.bitwise_and(blurred, blurred, mask=edges)

# Hiệu ứng tranh sơn dầu
def oil_paint_effect(image):
    return cv2.xphoto.oilPainting(image, 7, 1)
