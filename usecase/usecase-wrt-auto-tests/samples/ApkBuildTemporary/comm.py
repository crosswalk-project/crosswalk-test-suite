#!/usr/bin/env python
#coding=utf-8
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

import os
import sys
import subprocess

reload(sys)
sys.setdefaultencoding( "utf-8" )

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
Pck_Tools = ConstPath + "/../../tools/crosswalk/"

def setUp():
    global ARCH, MODE, device, AppName

    #device = "E6OKCY318006"
    device = os.environ.get('DEVICE_ID')
    if not device:
        print (" get env error\n")
        sys.exit(1)

    fp = open(ConstPath + "/../../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
        AppName = "Example_" + ARCH + ".apk"
    else:
        MODE = "shared"
        AppName = "Example.apk"
    mode.close()

def check_dir():
    flag = False
    count = 3

    def get_tmp():
        ret = os.listdir('/tmp')
        print ret, type(ret)
        for item in ret:
            print item
            if item.startswith("Example"):
                print 'Find'
                print os.listdir(ConstPath + "/../")
                os.system("rm -rf " + ConstPath + "/*.apk &>/dev/null")
                return True
    while True:
        ret = get_tmp()
        if ret:
            return True
            break
        else:
            time.sleep(1)

def gen_pkg(cmd, self):
    p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        buff = p1.stdout.readline()
        print buff 
        check_str = "Checking system requirements..."
        if buff.startswith(check_str):
            flag = check_dir()
            self.assertTrue(flag)
            break
        elif buff.startswith("Location:"):
            print 'No find'
            self.assertTrue(False)
            os.system("rm -rf " + ConstPath + "/../*apk &>/dev/null")
            break
