# -*- coding: utf-8 -*-
import os

import time
import traceback

import cv2

from config import ADB_DIR, FILE_NAME
from detectMaterial import detect
from grab import adbGrap



def mainLoop():
    os.system(ADB_DIR + "adb shell input swipe 1250 1550 1200 1300")
    adbGrap(ADB_DIR, FILE_NAME)
    try:
        detect()
    except Exception,e:
        print "pattern recognize fail"
        #print str(e)
        #traceback.print_exc()
        cv2.destroyAllWindows()
    else:
        print "pattern recognize success"





if __name__ == "__main__":
    while True:
        mainLoop()