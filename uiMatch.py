# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

from config import ADB_DIR, SCREEN_WIDTH, SCREEN_HEIGHT, ADB_SERIAL, ADB


def checkTemplate(img, template):
    img_rgb = cv2.imread(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    temp = cv2.imread(template, 0)
    w, h = temp.shape[::-1]
    res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 12)
        print "accurately matched"
        # plt.subplot(121), plt.imshow(res, cmap='gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(im1, cmap='gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.show()
        print "y:%d" % pt[1]
        # 移动不好计算，从最低到最高，分三种情况
        if pt[1] > 2100:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 330")  # 最低的情况
            print "y over 2100"
        elif pt[1] > 2000:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 300")
            print "y over 2000"
        elif pt[1] > 1950:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 350")
            print "y over 1950"
        elif pt[1] > 1900:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 400")
            print "y over 1900"
        elif pt[1] > 1800:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 500")
            print "y over 1800"
        elif pt[1] > 1600:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 600")
            print "y over 1600"
        elif pt[1] > 1400:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 700")
            print "y over 1400"
        elif pt[1] > 1300:  # this line is added when in emulator env
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 750")
            print "y over 1300"
        elif pt[1] > 1200:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 800")
            print "y over 1200"
        elif pt[1] > 1000:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 900")
            print "y over 1000"
        elif pt[1] > 800:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 1100")
            print "y over 800"
        elif pt[1] > 600:
            os.system(ADB + " " + ADB_SERIAL + " shell input swipe 0 1300 0 1150")  # 最上的情况
            print "y over 600"
        return 1
    return 0


