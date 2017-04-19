# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

fileName = os.getcwd() + '/../materials/appui/screenshot.png'
fileName_grayed = os.getcwd() + '/../materials/appui/ad_gray.png'
img = cv2.imread(fileName, 0)

def resize():
    global img
    #height, width = img.shape[:2]
    img = cv2.resize(img, (402, 743), interpolation=cv2.INTER_LINEAR)
resize()


def detect():
    global img
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
    adBoundPos = {}
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) >= 4 and peri < float(1826) and peri > float(130):
            i += 1
            print 'contour %d detected, perimeter:%d' % (i, peri)
            cntx0 = approx[0][0][0]
            cntx1 = approx[2][0][0]
            cnty0 = approx[0][0][1]
            cnty1 = approx[2][0][1]
            print 'cnt left x:%d cnt right x:%d top y:%d bottom y:%d' % (cntx0, cntx1, cnty0, cnty1)
            width = cntx1 - cntx0
            height = cnty1 - cnty0
            if abs(402 - width) > 5 and width > 100:  # width limitation
                if height > 100:  # must be our target
                    res = cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
                    adBoundPos['topLeft'] = box[1]
                    adBoundPos['topRight'] = box[2]
                    adBoundPos['bottomLeft'] = box[0]
                    adBoundPos['bottomRight'] = box[3]
                    print '>>draw contour %d' % i
                else:  # is a component area
                    res = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
                    componentHeight = box[0][1] - box[2][1]
                    adBoundPos['bottomLeft'] = [adBoundPos['bottomLeft'][0], adBoundPos['bottomLeft'][1] - height - 8]
                    adBoundPos['bottomRight'] = [adBoundPos['bottomRight'][0],
                                                 adBoundPos['bottomRight'][1] - height - 8]
                    print '>>draw contour %d' % i
                    # print approx
                    # break
    # draw ad area
    cv2.drawContours(img, [
        np.array([adBoundPos['topLeft'], adBoundPos['bottomLeft'], adBoundPos['bottomRight'], adBoundPos['topRight']])],
                     0, (255, 0, 0), 1)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect()





