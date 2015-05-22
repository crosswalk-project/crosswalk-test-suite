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

import unittest
import os
import commands
import comm

class TestCrosswalkApptoolsFunctions(unittest.TestCase):
    def test_check_log(self):
        comm.setUp()
        comm.cleanTempData(comm.TEST_PROJECT_COMM)
        os.chdir(comm.TEMP_DATA_PATH)
        createcmd = "crosswalk-app create " + comm.TEST_PROJECT_COMM
        createstatus = commands.getstatusoutput(createcmd)
        create_common = open(comm.TEMP_DATA_PATH + "/../tools/" + comm.TEST_PROJECT_COMM + "/log/common.log", 'r')
        create_android = open(comm.TEMP_DATA_PATH + "/../tools/" + comm.TEST_PROJECT_COMM + "/log/deb.log", 'r')
        create_common_log = create_common.read().strip("\n\t")
        create_android_log = create_android.read().strip("\n\t")
        os.chdir(comm.TEST_PROJECT_COMM)
        buildcmd =  "crosswalk-app build"
        buildstatus = commands.getstatusoutput(buildcmd)
        build_common = open(comm.TEMP_DATA_PATH + "/../tools/" + comm.TEST_PROJECT_COMM + "/log/common.log", 'r')
        build_android = open(comm.TEMP_DATA_PATH + "/../tools/" + comm.TEST_PROJECT_COMM + "/log/deb.log", 'r')
        build_common_log = build_common.read().strip("\n\t")
        build_android_log = build_android.read().strip("\n\t")
        comm.cleanTempData(comm.TEST_PROJECT_COMM)
        self.assertIn(createstatus[1].split('\n')[0], create_common_log)
        self.assertIn("Created project directory", create_android_log)
        self.assertIn(buildstatus[1].split('\n')[0], build_common_log)
        self.assertIn("build", build_android_log)

if __name__ == '__main__':
    unittest.main()
