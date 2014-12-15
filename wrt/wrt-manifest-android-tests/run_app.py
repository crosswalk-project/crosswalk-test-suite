#!/usr/bin/env python
import sys, os, os.path, shutil
import commands
 
SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH="x86"

def tryRunApp(num, caseDir):
    try:
        global result, ARCH

        apkDir = os.environ.get('APK_DIR')
        if apkDir != "" and os.path.exists(apkDir + "/apks"):
            apkDir = apkDir
        elif apkDir != "":
            caseDir = ConstPath + "/apks"
            shutil.move(caseDir, apkDir)

        device = os.environ.get('DEVICE_ID')

        if not device:
            print (" get env error\n")
            sys.exit(1)

        resultfile = open(ConstPath + "/report/packRes.txt")
        fp = open(ConstPath + "/arch.txt")
        if fp.read().strip("\n\t") != "x86":
            ARCH = "arm"
        fp.close()
        lines = resultfile.readlines()
        for line in lines:
            if line.startswith(num) and 'positive' in line and 'PASS' in line:

                print "##########"
                print num
                print "##########"
                print "Install APK ---------------->Start"
                instatus = commands.getstatusoutput("adb -s " + device + " install -r " + apkDir + "/apks/" + ARCH + "/" + num + "/" + "*.apk")
                if instatus[0] == 0:
                    print "Install APK ---------------->O.K"
                    pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep org.xwalk.test")
                    if pmstatus[0] == 0:
                        print "Find Package in device ---------------->O.K"
                        launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n org.xwalk.test/.TestActivity")
                        if launchstatus[0] != 0:
                            print "Launch APK ---------------->Error"
                            os.system("adb -s " + device + " uninstall org.xwalk.test")
                            result = "FAIL"
                            return result
                        else:
                            print "Launch APK ---------------->O.K"
                            stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop org.xwalk.test")
                            if stopstatus[0] == 0:
                                print "Stop APK ---------------->O.K"
                                unistatus = commands.getstatusoutput("adb -s " + device + " uninstall org.xwalk.test")
                                if unistatus[0] == 0:
                                    print "Uninstall APK ---------------->O.K"
                                    result = "PASS"
                                    return result
                                else:
                                    print "Uninstall APK ---------------->Error"
                                    result = "FAIL"
                                    return result
                            else:
                                print "Stop APK ---------------->Error"
                                result = "FAIL"
                                os.system("adb -s " + device + " uninstall org.xwalk.test")
                                return result
                    else:
                        print "Find Package in device ---------------->Error"
                        os.system("adb -s " + device + " uninstall org.xwalk.test")
                        result = "FAIL"
                        return result
                else:
                    print "Install APK ---------------->Error"
                    result = "FAIL"
                    return result
            elif line.startswith(num) and 'negative' in line and 'PASS' in line:
                print "Run negative test ---------------->OK"
                result = "PASS"
                return result
    except Exception,e:
        print Exception,":",e
        print "Try run webapp ---------------->Error"
        sys.exit(1)
