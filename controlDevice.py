# -*- coding: utf-8 -*-
import os

import time

import cv2

from detectMaterial import detect


def mainLoop():
    adbDir = "/home/evoup/Android/Sdk/platform-tools/"
    adScreenshotName = "ad_screenshot.png"
    os.system(adbDir + "adb shell input swipe 1250 1550 1250 1300")
    os.system(adbDir + "adb shell screencap /sdcard/" + adScreenshotName)
    os.system(adbDir + "adb pull /sdcard/" + adScreenshotName)
    os.system(adbDir + "adb shell rm /sdcard/" + adScreenshotName)
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