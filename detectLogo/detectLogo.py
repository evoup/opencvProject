# -*- coding: utf-8 -*-
import cv2
import numpy as np


# from matplotlib import pyplot as plt
im_gray = cv2.imread('../materials/appui/0319_14.png', 0)

height, width = im_gray.shape[:2]
img = cv2.resize(im_gray, (402, 743), interpolation=cv2.INTER_LINEAR)

_, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
cv2.imshow('img', img)


image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

cv2.waitKey(0)
cv2.destroyAllWindows()





# height, width = img.shape[:2]
# img = cv2.resize(img, (402, 743), interpolation=cv2.INTER_LINEAR)
# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 250, 255, 0)
# image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     rect = cv2.minAreaRect(cnt)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
# cv2.imshow('img', img)