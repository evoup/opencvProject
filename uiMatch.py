# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


def checkTemplate(img, template):
    im1 = cv2.imread(img)
    im2 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    temp = cv2.imread(template, 0)
    w, h = temp.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(im2, temp, method)
    threshold = 0.997
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 12)
        print "accurately matched"
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(im1, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()
        return 1
    return 0


