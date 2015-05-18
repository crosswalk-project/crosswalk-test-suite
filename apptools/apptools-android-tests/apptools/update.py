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
import urllib2

class TestCrosswalkApptoolsFunctions(unittest.TestCase):
    def test_update_no_argument(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update"
        currentVersion = comm.update(self, updatecmd)
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
        comm.clear("org.xwalk.test")
        self.assertEquals(currentVersion, version)

    def test_update_beta(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update beta"
        currentVersion = comm.update(self, updatecmd)
        crosswalklist = urllib2.urlopen('https://download.01.org/crosswalk/releases/crosswalk/android/beta/').read()
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
        comm.clear("org.xwalk.test")
        self.assertEquals(currentVersion, version)

    def test_update_canary(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update canary"
        currentVersion = comm.update(self, updatecmd)
        crosswalklist = urllib2.urlopen('https://download.01.org/crosswalk/releases/crosswalk/android/canary/').read()
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
        comm.clear("org.xwalk.test")
        self.assertEquals(currentVersion, version)

    def test_update_stable(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update stable"
        currentVersion = comm.update(self, updatecmd)
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
        comm.clear("org.xwalk.test")
        self.assertEquals(currentVersion, version)

    def test_update_invalid_channel(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update channel"
        updatestatus = commands.getstatusoutput(updatecmd)
        comm.clear("org.xwalk.test")
        self.assertIn("ERROR:", updatestatus[1])

    def test_update_version(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update 13.42.319.7"
        comm.update(self, updatecmd)
        comm.clear("org.xwalk.test")

    def test_update_currentVersion(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update 13.42.319.7"
        comm.update(self, updatecmd)
        newupdatecmd =  comm.PackTools + "crosswalk-app update 13.42.319.7"
        updatestatus = commands.getstatusoutput(newupdatecmd)
        self.assertIn("Using cached", updatestatus[1])
        comm.clear("org.xwalk.test")

    def test_update_lowerVersion(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update 13.42.319.7"
        comm.update(self, updatecmd)
        newupdatecmd =  comm.PackTools + "crosswalk-app update 11.40.277.1"
        comm.update(self, newupdatecmd)
        comm.clear("org.xwalk.test")

    def test_update_invalid_version(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update 0.0.0.0"
        updatestatus = commands.getstatusoutput(updatecmd)
        comm.clear("org.xwalk.test")
        self.assertIn("ERROR:", updatestatus[1])

    def test_update_toplevel_dir(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test/pkg')
        updatecmd =  comm.PackTools + "crosswalk-app update"
        updatestatus = commands.getstatusoutput(updatecmd)
        print updatestatus[1]
        comm.clear("org.xwalk.test")
        self.assertNotEquals(updatestatus[0], 0)

if __name__ == '__main__':
    unittest.main()
