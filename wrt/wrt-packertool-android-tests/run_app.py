#!/usr/bin/env python
import sys, os, os.path, shutil
import commands
 
SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH="x86"
pgNum=0

def tryRunApp(num, caseDir):
    try:
        global result, ARCH, pgNum

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

        pg = open(ConstPath + "/report/pgName.txt")
        lines = resultfile.readlines()
        pglines = pg.readlines()
        for j in range(len(pglines)):
            pgName = pglines[j][15:].strip()
            pgNum = pglines[j][:15].rstrip('-o')

            for line in lines:
                if line.startswith(num) and 'positive' in line and 'PASS' in line and num in pgNum:

                    print "##########"
                    print num
                    print "##########"
                    print "Install APK ---------------->Start"
                    androidName = pgName.split(".")[-1].split("_")
                    acivityName = ''.join([i.capitalize() for i in androidName if i])
                    instatus = commands.getstatusoutput("adb -s " + device + " install -r " + apkDir + "/apks/" + ARCH + "/" + num + "/" + "*.apk")
                    if instatus[0] == 0:
                        print "Install APK ---------------->O.K"
                        pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep " + pgName)
                        if pmstatus[0] == 0:
                            print "Find Package in device ---------------->O.K"
                            launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n " + pgName + "/." + acivityName +"Activity")
                            if launchstatus[0] != 0:
                                print "Launch APK ---------------->Error"
                                os.system("adb -s " + device + " uninstall " + pgName)
                                result = "FAIL"
                                return result
                            else:
                                print "Launch APK ---------------->O.K"
                                stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop " + pgName)
                                if stopstatus[0] == 0:
                                    print "Stop APK ---------------->O.K"
                                    unistatus = commands.getstatusoutput("adb -s " + device + " uninstall " + pgName)
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
                                    os.system("adb -s " + device + " uninstall " + pgName)
                                    return result
                        else:
                            print "Find Package in device ---------------->Error"
                            os.system("adb -s " + device + " uninstall " + pgName)
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

