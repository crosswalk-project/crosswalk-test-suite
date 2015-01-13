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
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):
    def test_packertool_help(self):
        comm.setUp()
        cmd = "python %smake_apk.py -h" % \
              (comm.Pck_Tools)
        packstatus = commands.getstatusoutput(cmd)
        #print packstatus
        self.assertEquals(0, packstatus[0])
        cmd2 = "python %smake_apk.py --help" % \
               (comm.Pck_Tools)
        packstatus2 = commands.getstatusoutput(cmd2)
        self.assertEquals(0, packstatus2[0])

    def test_packertool_arm_x86(self):
        comm.setUp()
        appRoot = comm.ConstPath + "/../testapp/example/"
        cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, appRoot)
        comm.gen_pkg(cmd, self)

    def test_packertool_undefinedOption(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --manifest=%s --undefinedOption=undefined" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        #print cmd
        packstatus = commands.getstatusoutput(cmd)
        #print packstatus
        errorInfo = "no such option: --undefinedOption"
        self.assertIn(errorInfo, packstatus[1])

    def test_packertool_verbose(self):
        comm.setUp()
        appRoot = comm.ConstPath + "/../testapp/example/"
        cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, appRoot)
        packstatus = commands.getstatusoutput(cmd)
        cmd_ver = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html --verbose"% \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, appRoot)
        packstatus_ver = commands.getstatusoutput(cmd_ver)
        self.assertGreater(len(packstatus_ver[1]), len(packstatus[1]))

    def test_packertool_version(self):
        comm.setUp()
        os.chdir(comm.Pck_Tools)
        fp = open(comm.Pck_Tools + "VERSION")
        lines = fp.readlines()
        version = lines[0][6:].strip("\n\t") + "." + lines[1][6:].strip("\n\t") + "." + lines[2][6:].strip("\n\t") + "." + lines[3][6:].strip("\n\t")
        cmd = "python %smake_apk.py -v" % (comm.Pck_Tools)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        self.assertIn(version, packstatus[1])
        cmd2 = "python %smake_apk.py --version" % (comm.Pck_Tools)
        packstatus2 = commands.getstatusoutput(cmd2)
        self.assertEquals(0, packstatus2[0])
        self.assertIn(version, packstatus2[1])

if __name__ == '__main__':
    unittest.main()  
