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
#         Wang. Hongjuan <hongjuanx.wang@intel.com>

import xml.etree.ElementTree as ET
import unittest
import os
import comm
import commands
import shutil
import glob

def init(xmlpath):
    channel = os.environ.get('CHANNEL')
    if not channel:
        print (" get channel error\n")
        sys.exit(1)

    if not comm.xwalk_version:
        print (" get crosswalk version error\n")
        sys.exit(1)

    tree = ET.parse(xmlpath)
    for elem in tree.iter(tag='property'):
        xwalk_version_name = elem.attrib.get('name')
        if xwalk_version_name == 'crosswalk-version':
            crosswalk_version = comm.xwalk_version
            if "64" in comm.ARCH:
                crosswalk_version = comm.xwalk_version + "-64bit"
            #elem.set(str(elem.attrib.items()[1][0]),'15.44.375.0')
            elem.set(str(elem.attrib.items()[1][0]), crosswalk_version)
            for node in tree.iter(tag='get'):
                #src_val = https://download.01.org/crosswalk/releases/crosswalk/android/canary/18.46.452.0/crosswalk-18.46.452.0-64bit.zip
                src_val = "https://download.01.org/crosswalk/releases/crosswalk/android/%s/%s/crosswalk-%s.zip" \
                          % (channel, comm.xwalk_version, crosswalk_version)
                print node.attrib.items()[1][0]
                node.set(str(node.attrib.items()[1][0]), src_val)
                print src_val
                tree.write(xmlpath, "utf-8", "xml")

class TestSampleAppFunctions(unittest.TestCase):

    def test_pack(self):
        comm.setUp()
        comm.check_appname()
        sample_src = "extensions-android"
        app_root = comm.sample_src_pref + sample_src
        xmlpath = app_root + '/xwalk-echo-extension-src/build.xml'
        init(xmlpath)
        cmd = "%s/build.sh -v %s -a %s - m %s" % (app_root, comm.xwalk_version, comm.ARCH, comm.MODE)
        target_apk_path = comm.const_path + "/../testapp/"
        os.chdir(target_apk_path)
        print "Generate APK %s ----------------> START" % comm.app_name
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        self.assertIn("build successful", packstatus[1].lower())
        print "\nGenerate APK %s ----------------> OK\n" % comm.app_name

        apk_build_flag = False
        apks = glob.glob(os.path.join(app_root, "*.apk"))
        if len(apks) > 0:
            apk_build_flag = True
            for apk in apks:
               shutil.move(apk, target_apk_path)
        else:
            print 'Not found apk'

        self.assertTrue(apk_build_flag)

if __name__ == '__main__':
    unittest.main()
