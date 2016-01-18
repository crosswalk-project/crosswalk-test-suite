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
    global device_x86, device_arm, XwalkPath, crosswalkVersion, crosswalkzip, PackTools, ARCH_ARM, ARCH_X86, cachedir, HOST_PREFIX, SHELL_FLAG, MODE, ANDROID_MODE, BIT, ANDROID_TARGETS, Skip_Emulator

    device_x86 = ""
    device_arm = ""
    cachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
    Skip_Emulator = os.environ.get('SKIP_EMULATOR')

    fp = open(ConstPath + "/../arch.txt", 'r')
    fp_arch = fp.read().strip("\n\t")
    if "," in fp_arch:
        if "a" in fp_arch and "x" in fp_arch:
            if "a" in fp_arch.split(',')[0].strip("\n\t"):
                ARCH_ARM = fp_arch.split(',')[0].strip("\n\t")
                ARCH_X86 = fp_arch.split(',')[1].strip("\n\t")
            else:
                ARCH_ARM = fp_arch.split(',')[1].strip("\n\t")
                ARCH_X86 = fp_arch.split(',')[0].strip("\n\t")
        else:
            ARCH_ARM = ""
            ARCH_X86 = ""
    elif "," not in fp_arch and "x" in fp_arch and "a" not in fp_arch:
        ARCH_ARM = ""
        ARCH_X86 = fp_arch
    elif "," not in fp_arch and "x" not in fp_arch and "a" in fp_arch:
        ARCH_ARM = fp_arch
        ARCH_X86 = ""
    else:
        ARCH_ARM = ""
        ARCH_X86 = ""
    fp.close()

    mode = open(ConstPath + "/../mode.txt", 'r')
    mode_type = mode.read().strip("\n\t")
    if mode_type == "embedded":
        MODE = ""
        ANDROID_MODE = ""
    elif mode_type == "shared":
        MODE = " --android-shared"
        ANDROID_MODE = "shared"
    else:
        MODE = " --android-lite"
        ANDROID_MODE = "lite"
    mode.close()

    host = open(ConstPath + "/../host.txt", 'r')
    if host.read().strip("\n\t") != "Windows":
        HOST_PREFIX = ""
        SHELL_FLAG = "True"
    else:
        HOST_PREFIX = "node "
        SHELL_FLAG = "False"
    host.close()

    #device = "Medfield61809467,066e11baf0ecb889"
    device = os.environ.get('DEVICE_ID')
    if not device and not Skip_Emulator:
        print ("Get DEVICE_ID env error\n")
        sys.exit(1)
    if device:
        if ARCH_ARM != "" and ARCH_X86 != "":
            if "," in device:
                if getDeviceCpuAbi(device.split(',')[0]) == "x86":
                    device_x86 = device.split(',')[0]
                else:
                    device_arm = device.split(',')[0]
                if getDeviceCpuAbi(device.split(',')[1]) == "x86":
                    device_x86 = device.split(',')[1]
                else:
                    device_arm = device.split(',')[1]
                if not device_x86 or not device_arm:
                    print ("Need x86 and arm architecture devices id\n")
                    sys.exit(1)
            else:
                print ("Need x86 and arm architecture devices id\n")
                sys.exit(1)
        elif ARCH_ARM != "" and ARCH_X86 == "":
            if getDeviceCpuAbi(device) == "arm":
                device_arm = device
            if not device_arm:
                print ("Need arm architecture devices id\n")
                sys.exit(1)
        elif ARCH_ARM == "" and ARCH_X86 != "":
            if getDeviceCpuAbi(device) == "x86":
                device_x86 = device
            if not device_x86:
                print ("Need x86 architecture devices id\n")
                sys.exit(1)

    vp = open(ConstPath + "/../version.txt", 'r')
    vp_version = vp.read().strip("\n\t")
    crosswalkVersion = vp_version.split(" ")[0]
    BIT = vp_version.split(" ")[1]
    vp.close()

    PackTools = os.environ.get('CROSSWALK_APP_SRC')
    if not PackTools:
        PackTools = ConstPath + "/../tools/crosswalk-app-tools/src/"

    XwalkPath = ConstPath + "/../tools/"
    if not PackTools and "crosswalk-app-tools" not in os.listdir(XwalkPath):
        print "Please check if the crosswalk-app-tools exists in " + ConstPath + "/../tools/"
        sys.exit(1)
    if BIT == "64":
        crosswalkzip = XwalkPath + 'crosswalk-{}-64bit.zip'.format(crosswalkVersion)
        ANDROID_TARGETS = ' --android-targets="arm64-v8a x86_64"'
    else:
        crosswalkzip = XwalkPath + 'crosswalk-{}.zip'.format(crosswalkVersion)
        ANDROID_TARGETS = ""
    if not os.path.exists(crosswalkzip):
        print "Please check if " + crosswalkzip + " exists"
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

def getDeviceCpuAbi(device):
    cmd = 'adb -s ' + device + ' shell getprop'
    (return_code, output) = getstatusoutput(cmd)
    for line in output[0].split('/n'):
        if "[ro.product.cpu.abi]" in line and "x86" in line:
            return "x86"
        else:
            return "arm"

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
        crosswalkzip
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    self.assertIn("org.xwalk.test", os.listdir(os.getcwd()))


def build(self, cmd):
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    apks = os.listdir(os.getcwd())
    apkLength = 0
    if MODE != " --android-shared":
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                if BIT == "64":
                    self.assertIn("64", apks[i])
                apkLength = apkLength + 1
                appVersion = apks[i].split('-')[1]
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                if BIT == "64":
                    self.assertIn("64", apks[i])
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


def run(self):
    setUp()
    if device_arm or device_x86:
        apks = os.listdir(os.getcwd())
        for apk in apks:
            if ARCH_ARM != "" and ("arm" in apk or "shared" in apk):
                return_inst_code_arm = os.system('adb -s ' + device_arm + ' install -r ' + apk)
                (return_pm_code_arm, pmstatus_arm) = getstatusoutput(
                    'adb -s ' +
                    device_arm +
                    ' shell pm list package')
                (return_laun_code_arm, launstatus_arm) = getstatusoutput(
                    'adb -s ' +
                    device_arm +
                    ' shell am start -n org.xwalk.test/.TestActivity')
                return_stop_code_arm = os.system(
                    'adb -s ' +
                    device_arm +
                    ' shell am force-stop org.xwalk.test')
                uninstatus_arm = os.popen('adb -s ' + device_arm + ' uninstall org.xwalk.test').read()
                self.assertEquals(return_inst_code_arm, 0)
                self.assertIn("org.xwalk.test", pmstatus_arm[0])
                self.assertEquals(return_laun_code_arm, 0)
                self.assertNotEquals("Error", launstatus_arm[0])
                self.assertEquals(return_stop_code_arm, 0)
                self.assertNotEquals("Success", uninstatus_arm)
            if ARCH_X86 != "" and ("x86" in apk or "shared" in apk):
                return_inst_code_x86 = os.system('adb -s ' + device_x86 + ' install -r ' + apk)
                (return_pm_code_x86, pmstatus_x86) = getstatusoutput(
                    'adb -s ' +
                    device_x86 +
                    ' shell pm list package')
                (return_laun_code_x86, launstatus_x86) = getstatusoutput(
                    'adb -s ' +
                    device_x86 +
                    ' shell am start -n org.xwalk.test/.TestActivity')
                return_stop_code_x86 = os.system(
                    'adb -s ' +
                    device_x86 +
                    ' shell am force-stop org.xwalk.test')
                uninstatus_x86 = os.popen('adb -s ' + device_x86 + ' uninstall org.xwalk.test').read()
                self.assertEquals(return_inst_code_x86, 0)
                self.assertIn("org.xwalk.test", pmstatus_x86[0])
                self.assertEquals(return_laun_code_x86, 0)
                self.assertNotEquals("Error", launstatus_x86[0])
                self.assertEquals(return_stop_code_x86, 0)
                self.assertNotEquals("Success", uninstatus_x86)


def channel(self, channel):
    createcmd = HOST_PREFIX + PackTools + \
        "crosswalk-app create org.xwalk.test" + MODE + " --android-crosswalk=" + channel + ANDROID_TARGETS
    (return_create_code, output) = getstatusoutput(createcmd)
    version = check_crosswalk_version(self, channel)
    clear("org.xwalk.test")
    self.assertEquals(return_create_code, 0)
    self.assertIn(channel, output[0])
    self.assertIn(version, output[0])


def check_crosswalk_version(self, channel):
    if MODE != " --android-lite":
        htmlDoc = urllib2.urlopen(
            'https://download.01.org/crosswalk/releases/crosswalk/android/' +
            channel +
            '/').read()
    else:
        htmlDoc = urllib2.urlopen(
            'https://download.01.org/crosswalk/releases/crosswalk-lite/android/' +
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
    if not cachedir:
        namelist = os.listdir(os.getcwd())
    else:
        newcachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
        os.chdir(newcachedir)
        namelist = os.listdir(os.getcwd())
        os.chdir(XwalkPath + 'org.xwalk.test')
    self.assertIn(crosswalk, namelist)
    return version
