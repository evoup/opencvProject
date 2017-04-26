# -*- coding: utf-8 -*-
import os

import time

import cv2

from config import ADB_DIR, FILE_NAME
from detectMaterial import detect
from grab import adbGrap



def mainLoop():
    os.system(ADB_DIR + "adb shell input swipe 1250 1550 1200 1400")
    adbGrap(ADB_DIR, FILE_NAME)
    try:
        detect()
    except:
        print "pattern recognize fail"
        cv2.destroyAllWindows()
    else:
        print "pattern recognize success"





if __name__ == "__main__":
    while True:
        mainLoop()