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

import unittest
import os
import commands
import comm

class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_no_sdk(self):
        comm.setUp()
        comm.clear("org.xwalk.test")
        android_home = commands.getoutput("(dirname $(dirname $(dirname $(which android))))")
        android_home1 = android_home + "/sdk"
        android_home2 = android_home + "/sdkk"
        allpath = commands.getoutput("echo $PATH")
        paths = allpath.split(":")
        for i in range(len(paths)):
            if android_home1 in paths[i]:
                paths[i] = paths[i].replace(android_home1, android_home2)
                new_path = ":".join(paths).strip()
        #print 'new_path', new_path
        os.environ['PATH'] = new_path
        #new = commands.getoutput("echo $PATH")
        #print new
        os.chdir(comm.XwalkPath)
        cmd = comm.PackTools + "crosswalk-app create org.xwalk.test --android-crosswalk=" + comm.crosswalkVersion
        packstatus = commands.getstatusoutput(cmd)
        os.environ['PATH'] = allpath
        #print packstatus
        self.assertIn("ERROR", packstatus[1])
        comm.clear("org.xwalk.test")

if __name__ == '__main__':
    unittest.main()
