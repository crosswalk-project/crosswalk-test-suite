#!/usr/bin/env python
import sys, os, os.path

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH="x86"

def geUnitcase():
    try:
        global ARCH
        fp = open(ConstPath + "/arch.txt")
        if fp.read().strip("\n\t") != "x86":
            ARCH = "arm"
        fp.close()
        print "Generate tests.py ---------------->Start"
        if os.path.exists(ConstPath + "/tests.py"):
            os.remove(ConstPath + "/tests.py")
        testfile = open("tests.py" ,'a+')
        testfile.write("#!/usr/bin/env python \n# coding=utf-8 \nimport random,os,sys,unittest,run_app,codecs \nreload(sys) \nsys.setdefaultencoding( \"utf-8\" ) \nclass TestCaseUnit(unittest.TestCase): \n ")
        casePath = ConstPath + "/tcs/"+ ARCH + "/"
        newcl = []
        cl = os.listdir(casePath)
        for i in cl:
            newcl.append(i)
            newcl.sort()
        for item in newcl:
            casenum = item[:-9].strip()
            flag = item[-8:]
            caseDir = "/opt/wrt-packertool-android-tests/apks/" + ARCH + "/" + item
            casenum = "\n  def test_" + flag + "_" + casenum +"(self):\n     self.assertEqual(\"PASS\", run_app.tryRunApp(\"" + item +"\", \"" + caseDir+ "\"))"+ "\n"
            testfile.write(casenum)
            testfile.flush()
        testfile.write("\nif __name__ == '__main__':\n    unittest.main()")
        testfile.close()
        os.system("chmod +x tests.py")
        print "Generate tests.py ---------------->OK"
    except Exception,e:
        print Exception,"Generate tests.py error:",e
        sys.exit(1)

if __name__ == "__main__":
    geUnitcase()
