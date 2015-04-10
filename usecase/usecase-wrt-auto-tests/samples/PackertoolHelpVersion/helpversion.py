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
import sys
import commands

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
Pck_Tools = ConstPath + "/../../tools/crosswalk/"

def setUp():
    global ARCH, MODE

    fp = open(ConstPath + "/../../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
    else:
        MODE = "shared"
    mode.close()

class TestPackertoolsFunctions(unittest.TestCase):

    def test_packertool_help(self):
        setUp()
        cmd = "python %smake_apk.py -h" % \
              (Pck_Tools)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        cmd2 = "python %smake_apk.py --help" % \
               (Pck_Tools)
        packstatus2 = commands.getstatusoutput(cmd2)
        self.assertEquals(0, packstatus2[0])


    def test_packertool_version(self):
        setUp()
        os.chdir(Pck_Tools)
        fp = open(Pck_Tools + "VERSION")
        lines = fp.readlines()
        version = lines[0][6:].strip("\n\t") + "." + lines[1][6:].strip("\n\t") + "." + lines[2][6:].strip("\n\t") + "." + lines[3][6:].strip("\n\t")
        cmd = "python %smake_apk.py -v" % (Pck_Tools)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        self.assertIn(version, packstatus[1])
        cmd2 = "python %smake_apk.py --version" % (Pck_Tools)
        packstatus2 = commands.getstatusoutput(cmd2)
        self.assertEquals(0, packstatus2[0])
        self.assertIn(version, packstatus2[1])

if __name__ == '__main__':
    unittest.main()  
