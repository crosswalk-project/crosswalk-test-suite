#!/usr/bin/env python
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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>
#         Yun, Liu<yunx.liu@intel.com>

import os
import sys
import stat
import shutil
import urllib2
import subprocess
import time
import re
from bs4 import BeautifulSoup

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
DEFAULT_CMD_TIMEOUT = 600


def setUp():
    global device, XwalkPath, crosswalkVersion, PackTools, ARCH, cachedir, HOST_PREFIX, SHELL_FLAG, MODE

    #device = "MedfieldC35A9F49"
    device = os.environ.get('DEVICE_ID')
    cachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
    if not device:
        print ("Get env error\n")
        sys.exit(1)

    fp = open(ConstPath + "/../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = ""
    else:
        MODE = " --android-shared"
    mode.close()

    host = open(ConstPath + "/../host.txt", 'r')
    if host.read().strip("\n\t") != "Android":
        HOST_PREFIX = "node "
        SHELL_FLAG = "False"
    else:
        HOST_PREFIX = ""
        SHELL_FLAG = "True"
    host.close()

    vp = open(ConstPath + "/../version.txt", 'r')
    crosswalkVersion = vp.read().strip("\n\t")
    vp.close()

    PackTools = ConstPath + "/../tools/crosswalk-app-tools/src/"

    XwalkPath = ConstPath + "/../tools/"
    if "crosswalk-app-tools" not in os.listdir(XwalkPath):
        print "Please check if the crosswalk-app-tools exists in " + ConstPath + "/../tools/"
        sys.exit(1)
    elif "crosswalk-app-tools" in os.listdir(XwalkPath) and len(os.listdir(XwalkPath)) < 2:
        print "Please check if the Crosswalk Binary exists in " + ConstPath + "/../tools/"
        sys.exit(1)

def getstatusoutput(cmd, time_out=DEFAULT_CMD_TIMEOUT):
    pre_time = time.time()
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=SHELL_FLAG)
    while True:
        output_line = cmd_proc.stdout.read()
        cmd_return_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_return_code is None:
            if elapsed_time >= time_out:
                killProcesses(ppid=cmd_proc.pid)
                return False
        elif output_line == '' and cmd_return_code is not None:
            break
        sys.stdout.write(output_line)
        sys.stdout.flush()
        output.append(output_line)
    return (cmd_return_code, output)

def clear(pkg):
    os.chdir(XwalkPath)
    if os.path.exists(ConstPath + "/../tools/" + pkg):
        if os.path.exists(ConstPath + "/../tools/" + pkg + "/prj"):
            shutil.rmtree(pkg + "/prj")
        shutil.rmtree(pkg)


def create(self):
    clear("org.xwalk.test")
    setUp()
    os.chdir(XwalkPath)
    cmd = HOST_PREFIX + PackTools + \
        "crosswalk-app create org.xwalk.test" + MODE + " --android-crosswalk=" + \
        crosswalkVersion
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    self.assertIn("org.xwalk.test", os.listdir(os.getcwd()))


def build(self, cmd):
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    apks = os.listdir(os.getcwd())
    apkLength = 0
    if MODE == "":
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
                appVersion = apks[i].split('-')[1]
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
                appVersion = apks[i].split('-')[1]
        self.assertEquals(apkLength, 2)
    else:
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "shared" in apks[i]:
                apkLength = apkLength + 1
                appVersion = apks[i].split('-')[1]
        self.assertEquals(apkLength, 1)
    return appVersion


def update(self, cmd):
    (return_update_code, update_output) = getstatusoutput(cmd)
    self.assertEquals(return_update_code, 0)
    self.assertNotIn("ERROR:", update_output[0])
    version = update_output[0].split(" * " + os.linesep)[-1].split(' ')[-1][1:-2]
    if not cachedir:
        namelist = os.listdir(os.getcwd())
    else:
        newcachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
        os.chdir(newcachedir)
        namelist = os.listdir(os.getcwd())
        os.chdir(XwalkPath + 'org.xwalk.test')
    crosswalk = 'crosswalk-{}.zip'.format(version)
    self.assertIn(crosswalk, namelist)
    return version


def run(self):
    setUp()
    apks = os.listdir(os.getcwd())
    for apk in apks:
        if ARCH in apk or "shared" in apk:
            return_inst_code = os.system('adb -s ' + device + ' install -r ' + apk)
            (return_pm_code, pmstatus) = getstatusoutput(
                'adb -s ' +
                device +
                ' shell pm list package')
            (return_laun_code, launstatus) = getstatusoutput(
                'adb -s ' +
                device +
                ' shell am start -n org.xwalk.test/.MainActivity')
            return_stop_code = os.system(
                'adb -s ' +
                device +
                ' shell am force-stop org.xwalk.test')
            uninstatus = os.popen('adb -s ' + device + ' uninstall org.xwalk.test').read()
            os.system('adb kill-server')
            self.assertEquals(return_inst_code, 0)
            self.assertIn("org.xwalk.test", pmstatus[0])
            self.assertEquals(return_laun_code, 0)
            self.assertNotEquals("Error", launstatus[0])
            self.assertEquals(return_stop_code, 0)
            self.assertNotEquals("Success", uninstatus)


def channel(self, channel):
    createcmd = HOST_PREFIX + PackTools + \
        "crosswalk-app create org.xwalk.test" + MODE + " --android-crosswalk=" + channel
    (return_create_code, output) = getstatusoutput(createcmd)
    htmlDoc = urllib2.urlopen(
        'https://download.01.org/crosswalk/releases/crosswalk/android/' +
        channel +
        '/').read()
    soup = BeautifulSoup(htmlDoc)
    alist = soup.find_all('a')
    version = ''
    for  index in range(-1, -len(alist)-1, -1):
        aEle = alist[index]
        version = aEle['href'].strip('/')
        if re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', version):
            break
    print "-----------" + version
    crosswalk = 'crosswalk-{}.zip'.format(version)
    namelist = os.listdir(os.getcwd())
    clear("org.xwalk.test")
    self.assertEquals(return_create_code, 0)
    self.assertIn(channel, output[0])
    self.assertIn(crosswalk, namelist)
