import os

from config import SAVE_FILE_NAME, FILE_NAME, ADB, ADB_SERIAL


def adbGrap():
    os.system(ADB + " " + ADB_SERIAL + " shell screencap /sdcard/" + FILE_NAME)
    os.system(ADB + " " + ADB_SERIAL + " pull /sdcard/" + FILE_NAME + " " + SAVE_FILE_NAME)
    os.system(ADB + " " + ADB_SERIAL + " shell rm /sdcard/" + FILE_NAME)
