# -*- coding: utf-8 -*-
import os

import time


def mainLoop():
    os.system("/home/evoup/Android/Sdk/platform-tools/adb shell input swipe 1250 1550 1250 1000")
    time.sleep(2)

if __name__ == "__main__":
    while True:
        mainLoop()