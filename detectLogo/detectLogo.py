# -*- coding: utf-8 -*-
import cv2
import numpy as np

fileName = '../materials/appui/0319_11.png'
fileName_grayed = '../materials/appui/0319_11_gray.png'
# from matplotlib import pyplot as plt
img = cv2.imread(fileName, 0)

def resize():
    global img
    height, width = img.shape[:2]
    img = cv2.resize(img, (402, 743), interpolation=cv2.INTER_LINEAR)
resize()

_, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
cv2.imshow('img', img)
cv2.waitKey(0)

######
cv2.imwrite(fileName_grayed, img)
oldImg = img.copy()
img = cv2.imread(fileName_grayed, 1)
resize()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 250, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# i = 0
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     rect = cv2.minAreaRect(cnt)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     res = cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
#     print 'contour %d drawed' % i
#     i += 1


# loop over our contours
for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        res = cv2.drawContours(img, [screenCnt], 0, (0, 255, 0), 2)
        break
######
cv2.imshow('img', img)
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