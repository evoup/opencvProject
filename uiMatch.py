# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

from config import ADB_DIR, SCREEN_WIDTH, SCREEN_HEIGHT


def checkTemplate(img, template):
    im1 = cv2.imread(img)
    im2 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    wimg, himg = im2.shape[::-1]
    temp = cv2.imread(template, 0)
    w, h = temp.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(im2, temp, method)
    threshold = 0.9997
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 12)
        print "accurately matched"
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(im1, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()
        # 移动不好计算，从最低到最高，分三种情况
        if pt[1] > 1500:
            #vs = 0.268  # 移到最顶的情况下，赞助标记和整体屏幕的估计百分比
            print "drag top"
            distance = 2560 - pt[1]
            distance = 1300 - distance
            os.system(ADB_DIR + "adb shell input swipe 1250 1300 1250 " + repr(distance))  # 最低的情况，算偏移
        elif pt[1] > 1200:
            os.system(ADB_DIR + "adb shell input swipe 1250 1300 1250 700")  # 中间的情况，移动中等距离
        elif pt[1] > 750:
            os.system(ADB_DIR + "adb shell input swipe 1250 1300 1250 1000")  # 最上的情况，移动小量距离
        return 1
    return 0


