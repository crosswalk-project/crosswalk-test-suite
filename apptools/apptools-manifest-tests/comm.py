#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
#         Yun, Liu<yunx.liu@intel.com>

import os
import sys
import stat
import shutil
import urllib2
import subprocess
import time
import json

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
DEFAULT_CMD_TIMEOUT = 600


def setUp():
    global device_x86, device_arm, crosswalkVersion, ARCH_ARM, ARCH_X86, PLATFORMS, HOST_PREFIX, SHELL_FLAG, MODE, ANDROID_MODE, BIT, TARGETS, apptools, apktype

    ARCH_ARM = ""
    ARCH_X86 = ""
    BIT = "32"
    device_x86 = ""
    device_arm = ""
    TARGETS = ""

    host = open(ConstPath + "/platforms.txt", 'r')
    PLATFORMS = host.read().strip("\n\t")
    if PLATFORMS != "windows":
        HOST_PREFIX = ""
        SHELL_FLAG = "True"
    else:
        HOST_PREFIX = "node "
        SHELL_FLAG = "False"
    host.close()

    if HOST_PREFIX != "":
        apptools = "%crosswalk-pkg%"
    else:
        apptools = "crosswalk-pkg"
    if os.system(HOST_PREFIX + apptools) != 0:
        print "crosswalk-pkg is not work, Please set the env"
        sys.exit(1)

    if PLATFORMS == "android":
        apktype = ".apk"
    elif PLATFORMS == "ios":
        apktype = ".ipa"
    elif PLATFORMS == "deb":
        apktype = ".deb"
    else:
        apktype = ".msi"

    if PLATFORMS == "android":
        fp = open(ConstPath + "/arch.txt", 'r')
        fp_arch = fp.read().strip("\n\t")
        if "x86" in fp_arch:
            ARCH_X86 = "x86"
        if "arm" in fp_arch:
            ARCH_ARM = "arm"
        if "64" in fp_arch:
            BIT = "64"
        fp.close()

        if BIT == "32":
            if ARCH_X86 == "x86" and ARCH_ARM == "":
                TARGETS = "x86"
            elif ARCH_ARM == "arm" and ARCH_X86 == "":
                TARGETS = "armeabi-v7a"
            elif ARCH_ARM == "arm" and ARCH_X86 == "x86":
                TARGETS = "armeabi-v7a x86"
        else:
            if ARCH_X86 == "x86" and ARCH_ARM == "":
                TARGETS = "x86_64"
            elif ARCH_ARM == "arm" and ARCH_X86 == "":
                TARGETS = "arm64-v8a"
            elif ARCH_ARM == "arm" and ARCH_X86 == "x86":
                TARGETS = "arm64-v8a x86_64"

        mode = open(ConstPath + "/mode.txt", 'r')
        mode_type = mode.read().strip("\n\t")
        if mode_type == "embedded":
            MODE = ""
            ANDROID_MODE = "embedded"
        elif mode_type == "shared":
            MODE = " --android-shared"
            ANDROID_MODE = "shared"
        else:
            MODE = " --android-lite"
            ANDROID_MODE = "lite"
        mode.close()

    device = ""
    if PLATFORMS == "android":
        #device = "Medfield61809467,066e11baf0ecb889"
        device = os.environ.get('DEVICE_ID')
        if not device:
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

    if PLATFORMS == "android" or PLATFORMS == "windows":
        if not os.path.exists(ConstPath + "/VERSION"):
            version_path = ConstPath + "/../../VERSION"
        else:
            version_path = ConstPath + "/VERSION"
        with open(version_path) as json_file:
            data = json.load(json_file)
        crosswalkVersion = data['main-version'].strip(os.linesep)

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

def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)

def doCopy(src_item=None, dest_item=None):
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        return False
    return True
