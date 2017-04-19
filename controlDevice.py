# -*- coding: utf-8 -*-
import os

import time

from detectMaterial import detect


def mainLoop():
    os.system("/home/evoup/Android/Sdk/platform-tools/adb shell input swipe 1250 1550 1250 1000")
    time.sleep(2)
    detect()

if __name__ == "__main__":
    while True:
        mainLoop()