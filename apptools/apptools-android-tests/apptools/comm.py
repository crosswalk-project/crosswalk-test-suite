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
import commands
import shutil
import urllib2

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)


def setUp():
    global device, XwalkPath, crosswalkVersion, PackTools, ARCH, cachedir

    #device = "E6OKCY411012"
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

    vp = open(ConstPath + "/../version.txt", 'r')
    crosswalkVersion = vp.read().strip("\n\t")
    vp.close()

    PackTools = ConstPath +  "/../tools/crosswalk-app-tools/src/"

    XwalkPath = ConstPath + "/../tools/"
    if "crosswalk-app-tools" not in os.listdir(XwalkPath):
        print "Please check if the crosswalk-app-tools exists in " + ConstPath + "/../tools/"
        sys.exit(1)
    elif "crosswalk-app-tools" in os.listdir(XwalkPath) and len(os.listdir(XwalkPath)) < 2:
        print "Please check if the Crosswalk Binary exists in " + ConstPath + "/../tools/"
        sys.exit(1)

def clear(pkg):
    if os.path.exists(ConstPath + "/../tools/" + pkg):
        try:
            shutil.rmtree(XwalkPath + pkg)
        except Exception,e:
            os.system("rm -rf " + XwalkPath + pkg + " &>/dev/null")

def create(self):
    clear("org.xwalk.test")
    setUp()
    os.chdir(XwalkPath)
    cmd = PackTools + "crosswalk-app create org.xwalk.test --android-crosswalk=" + crosswalkVersion
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(packstatus[0], 0)
    self.assertIn("org.xwalk.test", os.listdir(os.getcwd()))

def build(self, cmd):
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(buildstatus[0], 0)
    self.assertIn("pkg", os.listdir(XwalkPath + "org.xwalk.test"))
    os.chdir('pkg')
    apks = os.listdir(os.getcwd())
    self.assertNotEquals(len(apks), 0)
    for i in range(len(apks)):
        self.assertTrue(apks[i].endswith(".apk"))
        if "x86" in apks[i]:
            self.assertIn("x86", apks[i])
            if i < len(os.listdir(os.getcwd())):
                self.assertIn("arm", apks[i-1])
            else:
                self.assertIn("arm", apks[i+1])
        elif "arm" in apks[i]:
            self.assertIn("arm", apks[i])
            if i < len(os.listdir(os.getcwd())):
                self.assertIn("x86", apks[i-1])
            else:
                self.assertIn("x86", apks[i+1])

def update(self, cmd):
    updatestatus = commands.getstatusoutput(cmd)
    self.assertEquals(updatestatus[0], 0)
    self.assertNotIn("ERROR:", updatestatus[1])
    version = updatestatus[1].split('\n')[-1].split(' ')[-1][1:-1]
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
        if ARCH in apk:
            inststatus = commands.getstatusoutput('adb -s ' + device + ' install -r ' + os.getcwd() + '/' + apk)
            #print inststatus
            self.assertEquals(inststatus[0], 0)
            self.assertIn("Success", inststatus[1])
            pmstatus = commands.getstatusoutput('adb -s ' + device + ' shell pm list package |grep org.xwalk.test')
            self.assertEquals(pmstatus[0], 0)
            launstatus = commands.getstatusoutput('adb -s ' + device + ' shell am start -n org.xwalk.test/.TestActivity')
            self.assertEquals(launstatus[0], 0)
            stopstatus = commands.getstatusoutput('adb -s ' + device + ' shell am force-stop org.xwalk.test')
            self.assertEquals(stopstatus[0], 0)
            uninstatus = commands.getstatusoutput('adb -s ' + device + ' uninstall org.xwalk.test')
            self.assertEquals(uninstatus[0], 0)

def channel(self, channel):
    createcmd = PackTools + "crosswalk-app create org.xwalk.test --android-crosswalk=" + channel
    packstatus = commands.getstatusoutput(createcmd)
    self.assertEquals(packstatus[0], 0)
    self.assertIn(channel, packstatus[1])
    crosswalklist = urllib2.urlopen('https://download.01.org/crosswalk/releases/crosswalk/android/' + channel + '/').read()
    fp = open('test', 'w')
    fp.write(crosswalklist)
    fp.close()
    line = commands.getstatusoutput("cat test|sed -n  '/src\=\"\/icons\/folder.gif\"/=' |sed -n '$p'")[1].strip()
    cmd = "cat test |sed -n '%dp' |awk -F 'href=' '{print $2}' |awk -F '\"|/' '{print $2}'" % int(line)
    version = commands.getstatusoutput(cmd)[1]
    if not '.' in version:
        line = commands.getstatusoutput("tac test|sed -n  '/src\=\"\/icons\/folder.gif\"/=' |sed -n '2p'")[1].strip()
        cmd = "tac test |sed -n '%dp' |awk -F 'href=' '{print $2}' |awk -F '\"|/' '{print $2}'" % int(line)
        version = commands.getstatusoutput(cmd)[1]
    commands.getstatusoutput("rm -rf test")
    crosswalk = 'crosswalk-{}.zip'.format(version)
    namelist = os.listdir(os.getcwd())
    self.assertIn(crosswalk, namelist)
