# -*- coding: utf-8 -*-
import os

# ADB_DIR = 'C:/Program Files (x86)/Nox/bin/'
ADB_DIR = os.path.join("c:", "adbdir")
ADB = os.path.join("c:/", "adbdir", "adb")
FILE_NAME = "ad_screenshot.png"
SAVE_FILE_NAME = os.path.join("d:/", "grabData", FILE_NAME)
SCREEN_WIDTH = 402
SCREEN_HEIGHT = 743
COUNTRY = 'en'
#MATERIAL_SAVE_DIR = os.path.join("d:/", "grabData")
GRAB_MOBILE_WEB = False
ADB_SERIAL = "-s 127.0.0.1:62001"
SAVE_DIR = os.path.join("D:/", "grabFbAd")
DEBUG = False