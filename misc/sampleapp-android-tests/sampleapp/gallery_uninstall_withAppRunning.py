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
#         Li, Cici<cici.x.li@intel.com>

import unittest
import os, sys, commands
import comm
import time

class TestSampleAppFunctions(unittest.TestCase):
    def test_uninstall_withAppRunning(self):
        comm.setUp()
        app_name = "Gallery"
        cmdfind = "adb -s " + comm.device + " shell pm list packages |grep org.xwalk.%s" % (app_name.lower())
        #print "cmdfind: ", cmdfind
        pmstatus = commands.getstatusoutput(cmdfind)
        #print "pmstatus: ", pmstatus

        if pmstatus[0] != 0:
            print "Uninstall APK ----------------> %s App haven't installed, need to install it!" % app_name
            os.chdir(comm.const_path + "/../testapp/")
            apk_file = commands.getstatusoutput("ls | grep %s" % app_name)[1]
            cmdinst = "adb -s " + comm.device + " install -r " + apk_file
            comm.app_install(cmdinst, cmdfind, self)

        # Make sure the app is running
        cmd = "adb -s " + comm.device + " shell am start -n org.xwalk.%s/.%sActivity" % \
        (app_name.lower(), app_name)
        comm.app_launch(cmd, self)
        time.sleep(2)

        # Uninstall the app
        cmduninst = "adb -s " + comm.device + " uninstall org.xwalk.%s" % (app_name.lower()) 
        comm.app_uninstall(cmduninst, self)

if __name__ == '__main__':  
    unittest.main()
