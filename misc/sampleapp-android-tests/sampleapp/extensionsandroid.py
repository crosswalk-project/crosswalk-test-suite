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
#         Li, Hao<haox.li@intel.com>

import unittest
import os
import sys
import commands
import comm
import shutil
import glob
import xml.etree.ElementTree as ET
from TestApp import *

app_name = "Sample"
package_name = "org.crosswalkproject." + app_name.lower()
active_name = app_name + "Activity"
sample_src = comm.sample_src_pref + "extensions-android/"
xwalk_version = os.environ.get('XWALK_VERSION')
testapp = None

comm.setUp()

def init(xmlpath):
    channel = os.environ.get('CHANNEL')
    if not channel:
        print (" get channel error\n")
        sys.exit(1)

    if not xwalk_version:
        print (" get crosswalk version error\n")
        sys.exit(1)

    tree = ET.parse(xmlpath)
    for elem in tree.iter(tag='property'):
        xwalk_version_name = elem.attrib.get('name')
        if xwalk_version_name == 'crosswalk-version':
            crosswalk_version = xwalk_version
            if "64" in comm.ARCH:
                crosswalk_version = xwalk_version + "-64bit"
            #elem.set(str(elem.attrib.items()[1][0]),'15.44.375.0')
            elem.set(str(elem.attrib.items()[1][0]), crosswalk_version)
            for node in tree.iter(tag='get'):
                #src_val = https://download.01.org/crosswalk/releases/crosswalk/android/canary/18.46.452.0/crosswalk-18.46.452.0-64bit.zip
                src_val = "https://download.01.org/crosswalk/releases/crosswalk/android/%s/%s/crosswalk-%s.zip" \
                          % (channel, xwalk_version, crosswalk_version)
                print node.attrib.items()[1][0]
                node.set(str(node.attrib.items()[1][0]), src_val)
                print src_val
                tree.write(xmlpath, "utf-8", "xml")

def check_appname():
    global app_name
    #xwalk_version = '8.38.208.0'
    if int(xwalk_version.split('.')[0]) < 9:
        app_name = 'xwalk_echo_app'
    else:
        app_name = 'Sample'


class ExtensionsAndroid(unittest.TestCase):

    def test_1_pack(self):
        check_appname()
        xmlpath = sample_src + 'xwalk-echo-extension-src/build.xml'
        init(xmlpath)
        cmd = "%s/build.sh %s %s" % (sample_src, comm.MODE, comm.ARCH)
        os.chdir(comm.build_app_dest)
        print "Generate APK %s ----------------> START" % app_name
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        self.assertIn("build successful", packstatus[1].lower())
        print "\nGenerate APK %s ----------------> OK\n" % app_name

        apk_path = sample_src + "xwalk-echo-extension-src/lib/"
        apk_build_flag = False
        for index, name in enumerate(os.listdir(apk_path)):
            if os.path.isdir(apk_path + "/" + name):
                apk_path += name
                for apk_index, apkname in enumerate(os.listdir(apk_path)):
                    if apk_index <= len(os.listdir(apk_path)) and \
                    apkname.endswith(".apk") and apkname.startswith(app_name):
                        print 'Found apk %s' % apkname
                        apk_build_flag = True
                        os.chdir(apk_path)
                        shutil.move(apkname, comm.build_app_dest)
                    elif apkname.find(".apk") != -1:
                        print 'Continue'
            elif index > len(os.listdir(apk_path)) and \
            os.path.isdir(apk_path + "/" + name) == False:
                print 'Not found Crosswalk Runtime Binary'

        self.assertTrue(apk_build_flag)


    def test_2_install(self):
        apk_file = commands.getstatusoutput("ls %s| grep %s" % (comm.build_app_dest, app_name))[1]
        if apk_file.endswith(".apk"):
            global testapp
            testapp = TestApp(comm.device, comm.build_app_dest + apk_file, package_name, active_name)
            if testapp.isInstalled():
                testapp.uninstall()
            self.assertTrue(testapp.install())
        else:
            print("-->> No packed %s apk in %s" % (app_name, comm.build_app_dest))
            self.assertTrue(False)

    def test_3_launch(self):
        if testapp is not None:
            self.assertTrue(testapp.launch())
        else:
            print("-->> Fail to pack %s apk" % app_name)
            self.assertTrue(False)

    def test_4_switch(self):
        if testapp is not None:
            self.assertTrue(testapp.switch())
        else:
            print("-->> Fail to pack %s apk" % app_name)
            self.assertTrue(False)

    def test_5_stop(self):
        if testapp is not None:
            self.assertTrue(testapp.stop())
        else:
            print("-->> Fail to pack %s apk" % app_name)
            self.assertTrue(False)

    def test_6_uninstall(self):
        if testapp is not None:
            self.assertTrue(testapp.uninstall())
        else:
            print("-->> Fail to pack %s apk" % app_name)
            self.assertTrue(False)

    def test_7_uninstall_when_app_running(self):
        if testapp is not None:
            if not testapp.isInstalled():
                testapp.install()
            if not testapp.isRunning():
                testapp.launch()
            self.assertTrue(testapp.uninstall())
        else:
            print("-->> Fail to pack %s apk" % app_name)
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
