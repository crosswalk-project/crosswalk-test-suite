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
import json
from TestApp import *

app_name = "Hexgl"
package_name = "org.xwalk." + app_name.lower()
active_name = app_name + "Activity"
sample_src = comm.sample_src_pref + "HexGL/"
testapp = None

comm.setUp()

class Hexgl(unittest.TestCase):

    def test_1_pack(self):
        #clean up old apk
        commands.getstatusoutput("rm %s%s*" % (comm.build_app_dest, app_name))

        cmd = "python %smake_apk.py --package=%s --name=%s --app-root=%s --app-local-path=%s --arch=%s --mode=%s --enable-remote-debugging" % \
            (comm.pack_tools,
             package_name,
             app_name,
             sample_src,
             comm.index_path,
             comm.ARCH,
             comm.MODE)
        comm.pack(cmd, app_name, self)

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
