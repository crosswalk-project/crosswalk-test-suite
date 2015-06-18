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
import comm
import commands


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_clean_file(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test/prj/android/src/org/xwalk/test')
        fp = open("MainActivity.java", 'r+')
        fp.read().replace("org.xwalk.test", "org.xwalk.test1")
        fp.close()
        os.chdir(comm.XwalkPath + "org.xwalk.test")
        cleancmd = comm.PackTools + "crosswalk-app clean"
        cleanstatus = commands.getstatusoutput(cleancmd)
        os.chdir('prj/android/src/org/xwalk/test')
        fp_read = open("MainActivity.java", 'r')
        textread = fp_read.read().strip("\n\t")
        comm.clear("org.xwalk.test")
        self.assertEquals(cleanstatus[0], 0)
        self.assertNotIn("org.xwalk.test1", textread)

    def test_clean_build(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd = comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        os.chdir('../')
        cleancmd = comm.PackTools + "crosswalk-app clean"
        cleanstatus = commands.getstatusoutput(cleancmd)
        os.chdir('pkg')
        apklist = os.listdir(os.getcwd())
        comm.clear("org.xwalk.test")
        self.assertEquals(cleanstatus[0], 0)
        self.assertEquals(len(apklist), 0)

if __name__ == '__main__':
    unittest.main()
