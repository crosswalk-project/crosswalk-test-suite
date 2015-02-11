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
#         Cici,Li<cici.x.li@intel.com>

import unittest
import os, sys, commands, shutil
reload(sys)
sys.setdefaultencoding( "utf-8" )

script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
sample_src_pref = "/tmp/crosswalk-demos/"
pack_tools = const_path + "/../tools/crosswalk/"
index_path = "index.html"

def setUp():
    global ARCH, MODE, device

    device = os.environ.get('DEVICE_ID')

    if not device:
        print (" get env error\n")
        sys.exit(1)

    fp = open(const_path + "/../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(const_path + "/../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
    else:
        MODE = "shared"
    mode.close()

def pack(cmd, appname, self):
    setUp()
    os.chdir(const_path + "/../testapp/")
    print "Generate APK %s ----------------> START" % appname
    print cmd 
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    print "\nGenerate APK %s ----------------> OK\n" % appname
    result = commands.getstatusoutput("ls")
    self.assertIn(appname, result[1])
    os.chdir("../..")

def app_install(cmd, cmdfind, self):
    print "Install APK ----------------> START" 
    inststatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    pmstatus = commands.getstatusoutput(cmdfind)
    self.assertEquals(0, pmstatus[0])
    print "Find Package in device ----------------> OK"
    
def app_launch(cmd, self):
    print "Launch APK ----------------> START" 
    launchstatus = commands.getstatusoutput(cmd)
    self.assertNotIn("error",launchstatus[1].lower())
    print "Launch APK ----------------> OK"

def app_stop(cmd, self):
    print "Stop APK ----------------> START" 
    stopstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, stopstatus[0])
    print "Stop APK ----------------> OK"

def app_uninstall(cmd, self):
    print "Uninstall APK ----------------> START" 
    unistatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, unistatus[0])
    print "Uninstall APK ----------------> OK"

def others():
    if os.path.exists(pack_tools + "/" + AppName):
        os.remove(pack_tools + "/" + AppName)
    if os.path.exists(const_path + "/../" + AppName):
        os.remove(const_path + "/../" + AppName)


