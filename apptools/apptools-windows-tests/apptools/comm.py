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
    global XwalkPath, windowsCrosswalk, PackTools, HOST_PREFIX, SHELL_FLAG, cachedir, crosswalkversion

    cachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
    HOST_PREFIX = "node "
    SHELL_FLAG = "False"

    PackTools = os.environ.get('CROSSWALK_APP_SRC')
    if not PackTools:
        PackTools = ConstPath + "/../tools/crosswalk-app-tools/src/"

    XwalkPath = ConstPath + "/../tools/"
    if not PackTools and "crosswalk-app-tools" not in os.listdir(XwalkPath):
        print "Please check if the crosswalk-app-tools exists in " + ConstPath + "/../tools/"
        sys.exit(1)
    if not cachedir:        
        for i in range(len(os.listdir(XwalkPath))):
            if os.listdir(XwalkPath)[i].startswith("crosswalk") and os.listdir(XwalkPath)[i].endswith(".zip"):
                windowsCrosswalk = os.listdir(XwalkPath)[i]
    else:
        for i in range(len(os.listdir(cachedir))):
            if os.listdir(XwalkPath)[i].startswith("crosswalk") and os.listdir(cachedir)[i].endswith(".zip"):
                windowsCrosswalk = os.listdir(cachedir)[i]
    crosswalkversion = windowsCrosswalk[windowsCrosswalk.index("-") + 1:windowsCrosswalk.index(".zip")].strip()
    if not windowsCrosswalk:
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
        "crosswalk-app create org.xwalk.test --platform=windows --windows-crosswalk=" + \
        XwalkPath + windowsCrosswalk
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    self.assertIn("org.xwalk.test", os.listdir(os.getcwd()))


def build(self, cmd):
    return_code = os.system(cmd)
    self.assertEquals(return_code, 0)
    apks = os.listdir(os.getcwd())
    apkLength = 0
    for i in range(len(apks)):
        if apks[i].endswith(".msi"):
            apkLength = apkLength + 1
            appVersion = apks[i].split('-')[1][:apks[i].split('-')[1].index(".msi")].strip()
    self.assertEquals(apkLength, 1)
    return appVersion


def update(self, cmd):
    (return_update_code, update_output) = getstatusoutput(cmd)
    self.assertEquals(return_update_code, 0)
    self.assertNotIn("ERROR:", update_output[0])


def check_crosswalk_version(self, channel):
    htmlDoc = urllib2.urlopen(
        'https://download.01.org/crosswalk/releases/crosswalk/windows/' +
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
    return version
