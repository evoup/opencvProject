import os


def adbGrap(ADB_DIR, FILE_NAME, ADB_SERIAL):
    os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell screencap /sdcard/" + FILE_NAME)
    os.system(ADB_DIR + "adb " + ADB_SERIAL + " pull /sdcard/" + FILE_NAME)
    os.system(ADB_DIR + "adb " + ADB_SERIAL + " shell rm /sdcard/" + FILE_NAME)
