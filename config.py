# -*- coding: utf-8 -*-
import os

# ADB_DIR = 'C:/Program Files (x86)/Nox/bin/'
from optparse import OptionParser
from sys import argv

# ADB_DIR = os.path.join("c:/", "adbdir")
ADB = os.path.join("c:/", "adbdir", "adb")
FILE_NAME = "ad_screenshot.png"
SAVE_FILE_NAME = os.path.join("d:/", "grabData", FILE_NAME)
SCREEN_WIDTH = 402
SCREEN_HEIGHT = 743
COUNTRY = 'en'
# MATERIAL_SAVE_DIR = os.path.join("d:/", "grabData")
GRAB_MOBILE_WEB = False
# ADB_SERIAL = "-s 127.0.0.1:62001"
ADB_SERIAL = "-s 127.0.0.1:62001"
SAVE_DIR = os.path.join("D:/", "grabFbAd")
DEBUG = False

# get arguments
parser = OptionParser(description='Manages collectors which gather '
                                  'data and report back.')

parser.add_option('-s', '--adb-serial-number', dest='adb_serial_number', metavar='ADB_SERIAL_NUMBER',
                  default="127.0.0.1:62025",
                  help='adb serial number, e.g.: 127.0.0.1:62025')

parser.add_option('-x', '--snapshot_file_suffix', dest='snapshot_file_suffix', metavar='SNAPSHOT_FILE_SUFFIX',
                  default="_0",
                  help='snapshot file suffix, different from every collector process. e.g.: _1 should be snapshot_1.png '
                       'in the end')

parser.add_option('-d', '--debug', dest='debugmode', metavar='DEBUGMODE',
                  default="",
                  help='debug mode, default is not debug mode, if set with 1, then will be in debug mode')

(options, args) = parser.parse_args(args=argv[1:])

if options.adb_serial_number:
    ADB_SERIAL = "-s " + options.adb_serial_number

if options.snapshot_file_suffix:
    FILE_NAME = "ad_screenshot" + options.snapshot_file_suffix + ".png"

if options.debugmode:
    DEBUG = True
print "test"
