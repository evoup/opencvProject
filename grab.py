import os


def adbGrap(ADB_DIR, FILE_NAME):
    os.system(ADB_DIR + "adb shell screencap /sdcard/" + FILE_NAME)
    os.system(ADB_DIR + "adb pull /sdcard/" + FILE_NAME)
    os.system(ADB_DIR + "adb shell rm /sdcard/" + FILE_NAME)