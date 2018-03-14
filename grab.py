import os

from config import MATERIAL_SAVE_DIR


def adbGrap(ADB, FILE_NAME, ADB_SERIAL):
    os.system(ADB + " " + ADB_SERIAL + " shell screencap /sdcard/" + FILE_NAME)
    os.system(ADB + " " + ADB_SERIAL + " pull /sdcard/" + FILE_NAME + " " + MATERIAL_SAVE_DIR + "/" + FILE_NAME)
    os.system(ADB + " " + ADB_SERIAL + " shell rm /sdcard/" + FILE_NAME)
