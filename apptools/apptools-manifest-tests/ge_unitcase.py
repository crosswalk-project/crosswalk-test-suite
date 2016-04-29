#!/usr/bin/env python
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

import sys, os, os.path, shutil
import comm

def geUnitcase():
    try:
        comm.setUp()
        print "Generate tests.py ---------------->Start"
        if os.path.exists(comm.ConstPath + "/tests.py"):
            os.remove(comm.ConstPath + "/tests.py")
        testfile = open("tests.py" ,'a+')
        testfile.write("#!/usr/bin/env python\n# coding=utf-8\n#\n# Copyright (c) 2016 Intel Corporation.\n#\n# Redistribution and use in source and binary forms, with or without\n# modification, are permitted provided that the following conditions are met:\n#\n# * Redistributions of works must retain the original copyright notice, this\n#   list of conditions and the following disclaimer.\n# * Redistributions in binary form must reproduce the original copyright\n#   notice, this list of conditions and the following disclaimer in the\n#   documentation and/or other materials provided with the distribution.\n# * Neither the name of Intel Corporation nor the names of its contributors\n#   may be used to endorse or promote products derived from this work without\n#   specific prior written permission.\n#\n# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION \"AS IS\"\n# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,\n# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,\n# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY\n# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING\n# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,\n# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n#\n# Authors:\n#         Yun, Liu<yunx.liu@intel.com>\n\nimport random,os,sys,unittest,run_app,codecs,shutil,comm\nreload(sys)\nsys.setdefaultencoding(\"utf-8\")\n\nif os.path.exists(comm.ConstPath + \"/apks\"):\n    shutil.rmtree(comm.ConstPath + \"/apks\")\nos.mkdir(comm.ConstPath + \"/apks\")\nif os.path.exists(comm.ConstPath + \"/testapp\"):\n    shutil.rmtree(comm.ConstPath + \"/testapp\")\nos.mkdir(comm.ConstPath + \"/testapp\")\n\nclass TestCaseUnit(unittest.TestCase):\n ")
        casePath = comm.ConstPath + "/tcs/"
        newcl = []
        cl = os.listdir(casePath)
        for i in cl:
            newcl.append(i)
            newcl.sort()
        for item in newcl:
            casenum = item[:-9].strip()
            flag = item[-8:]
            caseDir = "/opt/apptools-manifest-tests/apks/" + item
            casenum = "\n  def test_" + flag + "_" + casenum +"(self):\n     self.assertEqual(\"PASS\", run_app.tryRunApp(\"" + item +"\", \"" + caseDir+ "\"))"+ "\n"
            testfile.write(casenum)
            testfile.flush()
        testfile.write("\nif __name__ == '__main__':\n    unittest.main()")
        testfile.close()
        if comm.PLATFORMS != "windows":
            os.system("chmod +x tests.py")
        print "Generate tests.py ---------------->OK"
    except Exception,e:
        print Exception,"Generate tests.py error:",e
        sys.exit(1)

if __name__ == "__main__":
    geUnitcase()
