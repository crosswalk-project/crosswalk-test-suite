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
import urllib2
import json
import sys
sys.path.append("../")
import comm


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_build_debug(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.clear("org.xwalk.test")

    def test_build_release_sdk(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.PackTools + "crosswalk-app build release --ios-sdk iphoneos"
        comm.build(self, buildcmd)
        comm.clear("org.xwalk.test")

    def test_build_release_sign(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.PackTools + 'crosswalk-app build release --ios-sign "iPhone Developer: M VINCENT DAUBRY (J9TS3TJRYX)"'
        comm.build(self, buildcmd)
        comm.clear("org.xwalk.test")

    def test_build_release_provison(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.PackTools + 'crosswalk-app build release --ios-provison "ios"'
        comm.build(self, buildcmd)
        comm.clear("org.xwalk.test")

    def test_create_with_platform_ios(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.PackTools + "crosswalk-app create org.xwalk.test --platform=ios"
        packstatus = commands.getstatusoutput(cmd)
        os.chdir('org.xwalk.test')
        buildcmd = comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)

    def test_list_target_platforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.PackTools + "crosswalk-app platforms"
        status = os.popen(cmd).readlines()
        self.assertEquals("ios", status[0].strip(" *\n"))
        self.assertEquals("android", status[1].strip(" *\n"))

    def test_version_normal(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.PackTools + "crosswalk-app version"
        versionstatus = commands.getstatusoutput(cmd)
        with open(comm.PackTools + "../package.json") as json_file:
            data = json.load(json_file)
        self.assertEquals(
            data['version'].strip("\n\t"),
            versionstatus[1].strip("\n\t"))

if __name__ == '__main__':
    unittest.main()
