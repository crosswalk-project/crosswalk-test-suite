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
import shutil
import urllib2

class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_normal_with_downloadCrosswalk(self):
        comm.setUp()
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        createcmd = comm.PackTools + "crosswalk-app create org.xwalk.test"
        packstatus = commands.getstatusoutput(createcmd)
        crosswalklist = urllib2.urlopen('https://download.01.org/crosswalk/releases/crosswalk/android/stable/').read()
        fp = open('test', 'w')
        fp.write(crosswalklist)
        fp.close()
        line = commands.getstatusoutput("cat test|sed -n  '/src\=\"\/icons\/folder.gif\"/=' |sed -n '$p'")[1].strip()
        cmd = "cat test |sed -n '%dp' |awk -F 'href=' '{print $2}' |awk -F '\"|/' '{print $2}'" % int(line)
        version = commands.getstatusoutput(cmd)[1]
        if not '.' in version:
            line = commands.getstatusoutput("tac test|sed -n  '/src\=\"\/icons\/folder.gif\"/=' |sed -n '2p'")[1].strip()
            cmd = "tac test |sed -n '%dp' |awk -F 'href=' '{print $2}' |awk -F '\"|/' '{print $2}'" % int(line)
            version = commands.getstatusoutput(cmd)[1]
        commands.getstatusoutput("rm -rf test")
        crosswalk = 'crosswalk-{}.zip'.format(version)
        namelist = os.listdir(os.getcwd())
        self.assertIn(crosswalk, namelist)
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)

if __name__ == '__main__':
    unittest.main()
