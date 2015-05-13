#!/usr/bin/env python 
# coding=utf-8 
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

import random,os,sys,unittest,allpairs 
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
class TestCaseUnit(unittest.TestCase): 
 
  def test_pkgName_positive1(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive1", "crosswalk-app create org.xwalk.tests --android-crosswalk="))

  def test_pkgName_positive2(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive2", "crosswalk-app create org.xwalk.t1234 --android-crosswalk="))

  def test_pkgName_positive3(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive3", "crosswalk-app create org.example.xwal_ --android-crosswalk="))

  def test_pkgName_positive4(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive4", "crosswalk-app create org.example.te_st --android-crosswalk="))

  def test_pkgName_positive5(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive5", "crosswalk-app create or_g.example.xwalk --android-crosswalk="))

  def test_pkgName_positive6(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive6", "crosswalk-app create org000.example.xwalk --android-crosswalk="))

  def test_pkgName_positive7(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive7", "crosswalk-app create org.example123.xwalk --android-crosswalk="))

  def test_pkgName_negative8(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative8", "crosswalk-app create org.xwalk --android-crosswalk="))

  def test_pkgName_negative9(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative9", "crosswalk-app create test --android-crosswalk="))

  def test_pkgName_negative10(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative10", "crosswalk-app create org.example.1234test --android-crosswalk="))

  def test_pkgName_negative11(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative11", "crosswalk-app create org.example.1234 --android-crosswalk="))

  def test_pkgName_negative12(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative12", "crosswalk-app create 123org.example.xwalk --android-crosswalk="))

  def test_pkgName_negative13(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative13", "crosswalk-app create org.123example.xwalk --android-crosswalk="))

  def test_pkgName_negative14(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative14", "crosswalk-app create org.example._xwalk --android-crosswalk="))

  def test_pkgName_negative15(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative15", "crosswalk-app create org.xwalk.Tests --android-crosswalk="))

  def test_pkgName_negative16(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative16", "crosswalk-app create _org.example.xwalk --android-crosswalk="))

if __name__ == '__main__':
    unittest.main()