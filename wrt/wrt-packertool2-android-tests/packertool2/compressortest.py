#!/usr/bin/env python

import unittest
import os, sys, commands, filecmp
import comm

class TestPackertoolsFunctions(unittest.TestCase):
  def test_compressor_minify(self):
      comm.clear_compressor()
      compre = " --compressor"
      comm.compressor(compre, self)
      self.assertFalse(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertFalse(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compscript = os.path.getsize(comm.compDir + "script.js")
      oriscript = os.path.getsize(comm.oriDir + "script.js")
      compstyle = os.path.getsize(comm.compDir + "style.css")
      oristyle = os.path.getsize(comm.oriDir + "style.css")
      self.assertTrue((oriscript > compscript))
      self.assertTrue((oristyle > compstyle))
      comm.clear_compressor()

  def test_compressor_minifycss(self):
      comm.clear_compressor()
      compre = " --compressor=css"
      comm.compressor(compre, self)
      self.assertTrue(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertFalse(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compstyle = os.path.getsize(comm.compDir + "style.css")
      oristyle = os.path.getsize(comm.oriDir + "style.css")
      self.assertTrue((oristyle > compstyle))
      comm.clear_compressor()

  def test_compressor_minifyjs(self):
      comm.clear_compressor()
      compre = " --compressor=js"
      comm.compressor(compre, self)
      self.assertFalse(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertTrue(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compscript = os.path.getsize(comm.compDir + "script.js")
      oriscript = os.path.getsize(comm.oriDir + "script.js")
      self.assertTrue((oriscript > compscript))
      comm.clear_compressor()

  def test_compressor_nominify(self):
      comm.clear_compressor()
      compre = ""
      comm.compressor(compre, self)
      self.assertTrue(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertTrue(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      comm.clear_compressor()

if __name__ == '__main__':  
    unittest.main()
