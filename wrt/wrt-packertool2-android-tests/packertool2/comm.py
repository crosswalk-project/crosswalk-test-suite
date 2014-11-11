#!/usr/bin/env python

import unittest
import os, sys, commands
import Queue, thread

Devices = list()
SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
MainPath = os.getcwd()
APP_PATH = MainPath + "/resource/"
Pck_Tools = MainPath + "/tools/crosswalk/"
MANIFEST_PATH = ["manifest.json", "./manifest.json", MainPath + "/resource/manifest.json"]
INDEX_PATH = ["index.html", "./index.html", ConstPath + "/index.html"]

def setUp():
    global ARCH, MODE, AppName

    DeviceQueue = Queue.Queue()
    if "DEVICE_ID" in os.environ:
        for device in os.environ["DEVICE_ID"].split(","):
            Devices.append(device)
            DeviceQueue.put(device)
    else:
        print "Can't read DEVICE_ID in os.environ"
        sys.exit(1)
    
    #for device in Devices:
     #   thread.start_new_thread(TestPackertoolsFunctions, (device,DeviceQueue))
   # DeviceQueue.join()

    fp = open(MainPath + "/arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(MainPath + "/mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
        AppName = "World_" + ARCH +".apk"
    else:
        MODE = "shared"
        AppName = "World.apk"
    mode.close()
