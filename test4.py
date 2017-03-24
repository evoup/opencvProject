import numpy as np
import cv2

# img = cv2.imread('ybmq.jpg')
img = cv2.imread('./materials/appui/0319_9.png')
img = cv2.resize(img, (402, 743), interpolation=cv2.INTER_LINEAR)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
x, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(imgray, contours, 3, (0, 255, 0), 3)
cv2.imshow('img', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
