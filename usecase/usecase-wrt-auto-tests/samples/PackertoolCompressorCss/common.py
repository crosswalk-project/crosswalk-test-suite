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

import unittest
import os
import sys
import commands
import shutil

reload(sys)
sys.setdefaultencoding( "utf-8" )

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
Pck_Tools = ConstPath + "/../../tools/crosswalk/"

def setUp():
    global ARCH, MODE, AppName


    fp = open(ConstPath + "/../../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
        AppName = "Compressor_" + ARCH + ".apk"
    else:
        MODE = "shared"
        AppName = "Compressor.apk"
    mode.close()

# test for compressor
def clear_compressor():
    if os.path.exists(ConstPath + "/res/compressor"):
       try:
          os.remove(ConstPath + "/res/" + AppName)
          shutil.rmtree(ConstPath + "/res/compressor")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/res/compressor")
          os.system(ConstPath + "/res/*.apk")

def compressor(compre, self):
    setUp()
    global compDir, oriDir
    manifestPath = ConstPath + "/res/manifest.json"
    os.chdir(ConstPath + "/res")
    cmd = "python %smake_apk.py --package=org.xwalk.compressor --arch=%s --mode=%s --manifest=%s --project-dir=compressor" % \
            (Pck_Tools, ARCH, MODE, manifestPath)
    packstatus = commands.getstatusoutput(cmd + compre)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    compDir = ConstPath + "/res/compressor/Compressor/assets/www/resource/"
    oriDir = ConstPath + "/res/resource/"
    self.assertIn("script.js", os.listdir(compDir))
    self.assertIn("style.css", os.listdir(compDir))

