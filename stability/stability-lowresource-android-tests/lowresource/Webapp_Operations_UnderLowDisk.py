#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Li, Hao<haox.li@intel.com>

import unittest
import os
import sys
import commands
import shutil
import time
import subprocess
import glob
from TestApp import *
reload(sys)
sys.setdefaultencoding('utf-8')

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
appsrc = ConstPath + "/../testapp/helloworld"
approot = ConstPath + "/helloworld"
app_tools_dir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
instaled_app_list = []

def setUp():
    global device, apptools, crosswalkzip
    #device = 'E6OKCY411012'
    device = os.environ.get('DEVICE_ID')
    global device_abi
    device_abi = getDeviceCpuAbi(device)
    if not device:
        print 'Get env error\n'
        sys.exit(1)

    if not app_tools_dir:
        print ("Not find CROSSWALK_APP_TOOLS_CACHE_DIR\n")
        sys.exit(1)

    # app tools commend
    apptools = "crosswalk-pkg"
    if os.system(apptools) != 0:
        apptools = app_tools_dir + "/crosswalk-app-tools/src/crosswalk-pkg"

    # crosswalk lib
    zips = glob.glob(os.path.join(app_tools_dir, "crosswalk-*.zip"))
    if len(zips) == 0:
        print ("Not find crosswalk zip in CROSSWALK_APP_TOOLS_CACHE_DIR\n")
        sys.exit(1)
    # latest version
    zips.sort(reverse = True)
    crosswalkzip = zips[0]

def getFreeDiskSize(device):
    # Disk size: M
    cmd = "%s -s %s shell df|grep %s |awk -F \" \" '{print $4}'" % (ADB_CMD, device, "/data")
    (return_code, output) = doCMD(cmd)
    for line in output:
        if line.endswith("G"):
            # 1G = 1024M
            return  int(float(line[0:-1]) * 1024)
        else:
            return  int(float(line[0:-1]))

def getDeviceCpuAbi(device):
    cmd = "%s -s %s shell getprop|grep \"\[ro.product.cpu.abi\]\"" % (ADB_CMD, device)
    (return_code, output) = doCMD(cmd)
    for line in output:
        if "x86" in line:
            return "x86"
        else:
            return "arm"

def getFileSize(filepath):
    filesize = 0
    if os.path.exists(filepath):
      filesize = float(os.stat(filepath).st_size)
      # size: M
      filesize = filesize/1024/1024
    else:
        print "-->> %s does not exists" % filepath

    return filesize


def createAPK(appname):
    action_status = True
    # Remove existed manifest.json
    if os.path.exists(appsrc + "/manifest.json"):
        os.remove(appsrc + "/manifest.json")
    # build apk
    cmd = "%s --crosswalk=%s --platforms=android --android=%s --targets=%s -m " \
          "\"{\\\"name\\\": \\\"%s\\\", \\\"start_url\\\": \\\"index.html\\\", \\\"xwalk_package_id\\\": \\\"org.xwalk.%s\\\"}\" %s" % \
          (apptools,
           crosswalkzip,
           "embedded",
           device_abi,
           appname,
           appname,
           appsrc)
    (return_code, output) = doCMD(cmd)
    if return_code == 0:
        print "-->> org.xwalk.%s success to build." % appname
        cmd = "mv *.apk %s/%s.apk" % (approot, appname)
        (return_code, output) = doCMD(cmd)
    else:
        print "-->> org.xwalk.%s fail to build." % appname
        action_status = False

    return action_status


def deleteAPK(testapp):
    cmd = "rm -rf %s" % (testapp.location)
    (return_code, output) = doCMD(cmd)
    if return_code == 0:
        print "-->> %s success to delete." % testapp.location
        return True
    else:
        print "-->> %s fail to delete." % testapp.location
        return False

def cleanWork():
    cmd = "rm -rf %s" % (appsrc + "/*.temp.3gp")
    (return_code, output) = doCMD(cmd)
    cmd = "rm -rf %s" % (approot)
    (return_code, output) = doCMD(cmd)
    for i in range(len(instaled_app_list)):
        instaled_app_list[i].uninstall()

def makeLowDisk():
    cleanWork()
    action_status = False

    if not os.path.exists(approot):
        cmd = "mkdir %s" % approot
        (return_code, output) = doCMD(cmd)
    
    vediofile = appsrc + "/video.3gp"
    vediosize = getFileSize(vediofile)
    if vediosize <= 0:
        print "-->> Lack pre-condition resource files"
        return False

    tmpreadystate = [False, False, False]

    global instaled_app_list
    while not action_status:

        freesize = getFreeDiskSize(device)
        if (freesize >= 1024) and not tmpreadystate[0]:
            # make app size: 500M
            count = int((500 - vediosize)/vediosize)
            for i in range(count):
                cmd = "cp %s %s " % (vediofile, appsrc + "/video" + str(i) +".temp.3gp")
                (return_code, output) = doCMD(cmd)
            tmpreadystate[0]  = True

        elif (freesize >= 512) and (freesize < 1024) and not tmpreadystate[1]:
            # clean appsrc
            if tmpreadystate[0]:
                cmd = "rm -rf %s/*.temp.3gp" % (appsrc)
                (return_code, output) = doCMD(cmd)
            (return_code, output) = doCMD(cmd)
            # make app size: 100M
            count = int((100 - vediosize)/vediosize)
            for i in range(count):
                cmd = "cp %s %s " % (vediofile, appsrc + "/video" + str(i) +".temp.3gp")
                (return_code, output) = doCMD(cmd)
            tmpreadystate[1]  = True

        elif (freesize < 512) and not tmpreadystate[2]:
            # clean appsrc
            cmd = "rm -rf %s/*.temp.3gp" % (appsrc)
            (return_code, output) = doCMD(cmd)
            tmpreadystate[2] = True

        appname = "helloworld%s" % int(time.time())
        if createAPK(appname):
            apkname = appname[0].upper() + appname[1:]
            apkpath = approot + "/" + appname + ".apk"
            testapp = TestApp(device, apkpath,
                                    "org.xwalk." + appname, apkname + "Activity")

            #If app exists, go to next
            if not testapp.isInstalled():
                #if app is not installed successful, delete the package, return True
                if not testapp.install():
                    action_status = True
                    deleteAPK(testapp)
                    # tmpreadystate[2] == True,
                    # means free disk is too small to install test app
                    # need to uninstall the last one to keep more free disk
                    if len(instaled_app_list) > 0 and tmpreadystate[2]:
                        testapp = instaled_app_list.pop(-1)
                        testapp.uninstall()
                        deleteAPK(testapp)
                else:
                    instaled_app_list.append(testapp)
        else:
            break

    return action_status


class TestStabilityInLowDiskFunctions(unittest.TestCase):

    def test_app_repeatedly_in_lowdisk(self):
        setUp()

        if makeLowDisk():
            testapp = TestApp(device, ConstPath + "/../testapp/lowresourcetest.apk",
                                    "org.xwalk.lowresourcetest", "LowresourcetestActivity")
            if testapp.isInstalled():
                testapp.uninstall()

            for i in range(20):
                if testapp.install() and testapp.launch():
                    switchresult = False
                    for i in range(2):
                        time.sleep(1)
                        # swtich app
                        switchresult = testapp.switch()

                    if switchresult:
                        time.sleep(1)
                        if testapp.stop() and testapp.uninstall():
                            time.sleep(1)
                        else:
                            testapp.uninstall()
                            cleanWork()
                            self.assertTrue(False)
                    else:
                        testapp.uninstall()
                        cleanWork()
                        self.assertTrue(False)
                else:
                    testapp.uninstall()
                    cleanWork()
                    self.assertTrue(False)

            testapp.uninstall()
            cleanWork()
            self.assertTrue(True)
        else:
            print "-->> Test envrionment fail to set up"
            cleanWork()
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
