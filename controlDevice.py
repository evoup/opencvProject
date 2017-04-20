# -*- coding: utf-8 -*-
import os

import time

import cv2

from detectMaterial import detect
from grab import adbGrap

ADB_DIR = "/home/evoup/Android/Sdk/platform-tools/"
FILE_NAME = "ad_screenshot.png"

def mainLoop():
    os.system(ADB_DIR + "adb shell input swipe 1250 1550 1250 1300")
    adbGrap(ADB_DIR, FILE_NAME)
    #time.sleep(5)
    #os.system("sleep 2")
    try:
        detect()
    except:
        print "mode recognize fail"
        cv2.destroyAllWindows()
    else:
        print "mode recognize success"





if __name__ == "__main__":
    while True:
        mainLoop()