#!/usr/bin/env python 
# coding=utf-8 
import random,os,sys,unittest,allpairs 
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
class TestCaseUnit(unittest.TestCase): 
 
  def test_pkgName_positive1(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive1", "org.xwalk.tests"))

  def test_pkgName_positive2(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive2", "org.xwalk.t1234"))

  def test_pkgName_positive3(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive3", "org.example._xwalk"))

  def test_pkgName_positive4(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive4", "org.example.xwal_"))

  def test_pkgName_positive5(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive5", "org.example.te_st"))

  def test_pkgName_positive6(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive6", "org.xwalk.Tests"))

  def test_pkgName_positive7(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive7", "or_g.example.xwalk"))

  def test_pkgName_positive8(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive8", "org000.example.xwalk"))

  def test_pkgName_positive9(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive9", "_org.example.xwalk"))

  def test_pkgName_positive10(self):
     self.assertEqual("PASS", allpairs.tryRunApp("positive10", "org.example123.xwalk"))

  def test_pkgName_negative11(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative11", "org.xwalk"))

  def test_pkgName_negative12(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative12", "test"))

  def test_pkgName_negative13(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative13", "org.example.1234test"))

  def test_pkgName_negative14(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative14", "org.example.1234"))

  def test_pkgName_negative15(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative15", "123org.example.xwalk"))

  def test_pkgName_negative16(self):
     self.assertEqual("PASS", allpairs.tryRunApp("negative16", "org.123example.xwalk"))

if __name__ == '__main__':
    unittest.main()