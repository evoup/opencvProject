# -*- coding: utf-8 -*-
import cv2
from PIL import Image
import imagehash
import numpy as np
import os

import time

import scipy.misc

from config import ADB_DIR, FILE_NAME, SCREEN_WIDTH, SCREEN_HEIGHT, COUNTRY, GRAB_MOBILE_WEB, ADB_SERIAL, SAVE_DIR
from grab import adbGrap
from uiMatch import checkTemplate


def detect():
    # fileName = os.getcwd() + '/materials/appui/0419_2.png'
    fileName = os.getcwd() + "/" + FILE_NAME
    if GRAB_MOBILE_WEB:
        tempImg = os.getcwd() + '/materials/components/base/mobileWeb/sponsor_content_' + COUNTRY + '_web.png'
    else:
        tempImg = os.getcwd() + '/materials/components/base/sponsor_content_'+ COUNTRY + '.png'
    ###
    bottomTempImg = os.getcwd() + '/materials/components/base/bottom.png'
    if checkTemplate(fileName, bottomTempImg):
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + 'at bottom, let`s go top and do next round'
        os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 0 1550 0 13000")
        time.sleep(1)
        os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 0 1550 0 12000")
        time.sleep(1)
        os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 0 1550 0 8000")
        os.exit(0)
    ###
    if not checkTemplate(fileName, tempImg):
       return
    time.sleep(0.3)
    adbGrap(ADB_DIR, FILE_NAME, ADB_SERIAL)
    fileName_grayed = os.getcwd() + '/materials/appui/ad_gray.png'
    img = cv2.imread(fileName, 0)
    #resize
    img = cv2.resize(img, (SCREEN_WIDTH, SCREEN_HEIGHT), interpolation=cv2.INTER_LINEAR)
    global img
    _, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
    #cv2.imshow('img', img)
    #cv2.waitKey(0)
    ######
    cv2.imwrite(fileName_grayed, img)
    oldImg = img.copy()
    img = cv2.imread(fileName_grayed, 1)
    img = cv2.resize(img, (SCREEN_WIDTH, SCREEN_HEIGHT), interpolation=cv2.INTER_LINEAR)
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
        cv2.drawContours(img, [box], 0, (0, 255, 255), 2) # yellow means all polygon
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
            try:
                if componentTop > 0:
                    pass
            except NameError:
                componentTop = SCREEN_HEIGHT
            else:
                pass

            if abs(SCREEN_WIDTH - width) > 1 and width > 100:  # width limitation
                if height > 100:  # must be our target
                    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
                    adBoundPos['topLeft'] = box[1]
                    adBoundPos['topRight'] = box[2]
                    adBoundPos['bottomLeft'] = box[0]
                    adBoundPos['bottomRight'] = box[3] # should be topRight!
                    print '>>draw contour %d' % i
                else:  # is a component area
                    cv2.drawContours(img, [box], 0, (0, 0, 255), 1)
                    componentHeight = box[0][1] - box[2][1]
                    componentTopLeft = box[3]
                    if componentTopLeft[1] < componentTop:
                        componentTop = componentTopLeft[1] # save component position so we can adjust target according to it
                    adBoundPos['bottomLeft'] = [adBoundPos['bottomLeft'][0], adBoundPos['bottomLeft'][1] - height - 8]
                    adBoundPos['bottomRight'] = [adBoundPos['bottomRight'][0],
                                                 adBoundPos['bottomRight'][1] - height - 8]
                    print '>>draw contour %d' % i
                    # print approx
                    # break6
    # draw ad area
    findMaterial = False
    if abs(adBoundPos['topLeft'][1] - adBoundPos['topRight'][1]) > 10:
        print "not a valid rectangle region"
    else:
        # adjust target bottom position
        if componentTop - adBoundPos['bottomLeft'][1] > 10:
            adBoundPos['bottomLeft'][1] = componentTop
            adBoundPos['bottomRight'][1] = componentTop
        print "componentTop:%d" % componentTop
        ###print "adBoundPos['bottomLeft'][1]:" + adBoundPos['bottomLeft'][1]
        ###print "adBoundPos['bottomRight'][1]:" + adBoundPos['bottomRight'][1]
        cv2.drawContours(img, [
            np.array([adBoundPos['topLeft'], adBoundPos['bottomLeft'], adBoundPos['bottomRight'], adBoundPos['topRight']])],
                         0, (255, 0, 0), 1)
        print "got target material!"
        findMaterial = True
        #crop image by y1 y2 x1 x2
        img1 = cv2.imread(fileName, 1)
        img1 = cv2.resize(img1, (SCREEN_WIDTH, SCREEN_HEIGHT), interpolation=cv2.INTER_LINEAR)
        cropImage = img1[adBoundPos['topLeft'][1]:adBoundPos['bottomRight'][1],
                    adBoundPos['topLeft'][0]:adBoundPos['bottomRight'][0]].copy()
        cv2.imshow("cropImage", cropImage)
        grayImg = cv2.cvtColor(cropImage, cv2.COLOR_BGR2GRAY)
        cv2.imshow("grayImg", grayImg)
        # convert cv to PIL.Image
        hash = imagehash.average_hash(Image.fromarray(cv2.cvtColor(cropImage, cv2.COLOR_BGR2RGB)))
        myHash = str(hash)
        cv2.imwrite(SAVE_DIR + myHash + ".png", cropImage)
        cv2.waitKey(0)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    #time.sleep(3)
    cv2.destroyAllWindows()
    carouselDetect(adBoundPos)
    if findMaterial:
        os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 1250 1550 1250 1000")


# is a carousel?
def carouselDetect(adBoundPos):
    adWidthVSScreenWidth = (adBoundPos['bottomRight'][0] - adBoundPos['bottomLeft'][0]) / float(SCREEN_WIDTH)
    if adWidthVSScreenWidth > 0.7 and adWidthVSScreenWidth < 0.75:
        print "it`s a carousel ad pane"
        img1 = cv2.imread(os.getcwd() + "/" + FILE_NAME, 1)
        img1 = cv2.resize(img1, (SCREEN_WIDTH, SCREEN_HEIGHT), interpolation=cv2.INTER_LINEAR)
        cropImage = img1[adBoundPos['topLeft'][1]:adBoundPos['bottomRight'][1],
                    adBoundPos['topLeft'][0]:adBoundPos['bottomRight'][0]].copy()
        cv2.imshow("cropImage", cropImage)
        cv2.waitKey(0)
        os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 1250 1300 900 1300")
        time.sleep(0.3)
        # wait a moment to prevent hasn`t finish move
        img1 = cv2.imread(FILE_NAME, 1)
        adbGrap(ADB_DIR, FILE_NAME, ADB_SERIAL)
        img2 = cv2.imread(FILE_NAME, 1)
        if is_similar(img1, img2):
            print "same"
            os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell input swipe 1250 1550 1250 1000")
        else:
            print "different"
        #carouselDetect(adBoundPos)
        detect()


def is_similar(im1, im2):
    return im1.shape == im2.shape and not(np.bitwise_xor(im1, im2).any())



if __name__ == "__main__":
    detect()


