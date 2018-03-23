# -*- coding: utf-8 -*-
import os

import time
import traceback

import cv2

from config import ADB_SERIAL, ADB
from detectMaterial import detect
from grab import adbGrap



def mainLoop():
    moveShell = ADB + " " + ADB_SERIAL + " shell input swipe 0 1550 0 1300"
    os.system(moveShell)
    time.sleep(1.7) # wait to check if close to bottom
    adbGrap()
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
    open_shell = ADB + " " + ADB_SERIAL +  " shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1"
    os.system(open_shell)
    time.sleep(3)
    while True:
        mainLoop()
