#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2016 Intel Corporation.
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

import random,os,sys,unittest,run_app,codecs,shutil,comm
reload(sys)
sys.setdefaultencoding("utf-8")

if os.path.exists(comm.ConstPath + "/apks"):
    shutil.rmtree(comm.ConstPath + "/apks")
os.mkdir(comm.ConstPath + "/apks")
if os.path.exists(comm.ConstPath + "/testapp"):
    shutil.rmtree(comm.ConstPath + "/testapp")
os.mkdir(comm.ConstPath + "/testapp")

class TestCaseUnit(unittest.TestCase):
 
  def test_positive_manifest1(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest1-positive", "/opt/apptools-manifest-tests/apks/manifest1-positive"))

  def test_positive_manifest10(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest10-positive", "/opt/apptools-manifest-tests/apks/manifest10-positive"))

  def test_positive_manifest11(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest11-positive", "/opt/apptools-manifest-tests/apks/manifest11-positive"))

  def test_positive_manifest12(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest12-positive", "/opt/apptools-manifest-tests/apks/manifest12-positive"))

  def test_positive_manifest13(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest13-positive", "/opt/apptools-manifest-tests/apks/manifest13-positive"))

  def test_positive_manifest14(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest14-positive", "/opt/apptools-manifest-tests/apks/manifest14-positive"))

  def test_positive_manifest15(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest15-positive", "/opt/apptools-manifest-tests/apks/manifest15-positive"))

  def test_positive_manifest16(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest16-positive", "/opt/apptools-manifest-tests/apks/manifest16-positive"))

  def test_positive_manifest17(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest17-positive", "/opt/apptools-manifest-tests/apks/manifest17-positive"))

  def test_positive_manifest18(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest18-positive", "/opt/apptools-manifest-tests/apks/manifest18-positive"))

  def test_positive_manifest19(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest19-positive", "/opt/apptools-manifest-tests/apks/manifest19-positive"))

  def test_positive_manifest2(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest2-positive", "/opt/apptools-manifest-tests/apks/manifest2-positive"))

  def test_negative_manifest20(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest20-negative", "/opt/apptools-manifest-tests/apks/manifest20-negative"))

  def test_negative_manifest21(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest21-negative", "/opt/apptools-manifest-tests/apks/manifest21-negative"))

  def test_negative_manifest22(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest22-negative", "/opt/apptools-manifest-tests/apks/manifest22-negative"))

  def test_negative_manifest23(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest23-negative", "/opt/apptools-manifest-tests/apks/manifest23-negative"))

  def test_negative_manifest24(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest24-negative", "/opt/apptools-manifest-tests/apks/manifest24-negative"))

  def test_negative_manifest25(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest25-negative", "/opt/apptools-manifest-tests/apks/manifest25-negative"))

  def test_negative_manifest26(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest26-negative", "/opt/apptools-manifest-tests/apks/manifest26-negative"))

  def test_positive_manifest3(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest3-positive", "/opt/apptools-manifest-tests/apks/manifest3-positive"))

  def test_positive_manifest4(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest4-positive", "/opt/apptools-manifest-tests/apks/manifest4-positive"))

  def test_positive_manifest5(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest5-positive", "/opt/apptools-manifest-tests/apks/manifest5-positive"))

  def test_positive_manifest6(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest6-positive", "/opt/apptools-manifest-tests/apks/manifest6-positive"))

  def test_positive_manifest7(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest7-positive", "/opt/apptools-manifest-tests/apks/manifest7-positive"))

  def test_positive_manifest8(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest8-positive", "/opt/apptools-manifest-tests/apks/manifest8-positive"))

  def test_positive_manifest9(self):
     self.assertEqual("PASS", run_app.tryRunApp("manifest9-positive", "/opt/apptools-manifest-tests/apks/manifest9-positive"))

if __name__ == '__main__':
    unittest.main()