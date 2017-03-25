# -*- coding: utf-8 -*-
import cv2
import numpy as np

fileName = '../materials/appui/0319_15.png'
fileName_grayed = '../materials/appui/0319_15_gray.png'
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
i = 0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    if len(approx) == 4 and peri < float(1826) and peri > float(880):
        res = cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
        print 'contour %d drawed, perimeter:%d' % (i, peri)
        print approx
        i += 1
        #break


# for c in contours:
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#     if len(approx) == 4:
#         ctaCnt = approx
#         res = cv2.drawContours(img, [ctaCnt], 0, (0, 255, 0), 2)
#         break
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