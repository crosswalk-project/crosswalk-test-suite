#!/usr/bin/env python 
# coding=utf-8 
import random,os,sys,unittest,allpairs 
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
class TestCaseUnit(unittest.TestCase): 
 
  def test_pkgName_positive1(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive1", "crosswalk-app create org.xwalk.tests --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive2(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive2", "crosswalk-app create org.xwalk.t1234 --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive3(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive3", "crosswalk-app create org.example._xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive4(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive4", "crosswalk-app create org.example.xwal_ --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive5(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive5", "crosswalk-app create org.example.te_st --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive6(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive6", "crosswalk-app create org.xwalk.Tests --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive7(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive7", "crosswalk-app create or_g.example.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive8(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive8", "crosswalk-app create org000.example.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive9(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive9", "crosswalk-app create _org.example.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_positive10(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive10", "crosswalk-app create org.example123.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative11(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative11", "crosswalk-app create org.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative12(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative12", "crosswalk-app create test --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative13(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative13", "crosswalk-app create org.example.1234test --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative14(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative14", "crosswalk-app create org.example.1234 --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative15(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative15", "crosswalk-app create 123org.example.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

  def test_pkgName_negative16(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative16", "crosswalk-app create org.123example.xwalk --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip"))

if __name__ == '__main__':
    unittest.main()