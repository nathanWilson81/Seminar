import cv2
import numpy as np

img = cv2.imread('test1.png', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
print(area)
