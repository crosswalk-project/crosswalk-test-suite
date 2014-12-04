#!/usr/bin/env python
import sys, os, os.path, shutil, time
import commands, traceback, glob

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH = "x86"

def genPackage():
    try:
        global result, ARCH
        fp = open(ConstPath + "/arch.txt")
        if fp.read().strip("\n\t") != "x86":
            ARCH = "arm"
        fp.close()

        #genarate package and execute
        manifestLog = open(ConstPath + "/report/packageInfo.txt", 'a+')
        if os.path.exists(ConstPath + "/tools/crosswalk/"):
            os.chdir(ConstPath + "/tools/crosswalk/")
        else:
            os.chdir(ConstPath + "/../../tools/crosswalk/")
        if os.path.exists(ConstPath + "/apks") and len(os.listdir(ConstPath + "/apks")) != 0:
            if ARCH in os.listdir(ConstPath + "/apks"):
                shutil.rmtree(ConstPath + "/apks/" + ARCH)
                os.mkdir(ConstPath + "/apks/" + ARCH)
            else:
                os.mkdir(ConstPath + "/apks/" + ARCH)
        else:
            os.mkdir(ConstPath + "/apks")
            os.mkdir(ConstPath + "/apks/" + ARCH)

        print "Generate APK ---------------->Start"
        toolstatus = commands.getstatusoutput("python make_apk.py")[0]
        if toolstatus != 0:
            print "Crosswalk Binary is not ready, Please attention"
            sys.exit(1)

        casePath = ConstPath + "/tcs/"
        for i in os.listdir(casePath):
            print "##########"
            print i
            print "##########"
            flag = i[-8:].strip()
            caseStart = time.strftime("%Y-%m-%d %H:%M:%S")
            manifestLog.write(i+ "\n")
            manifestLog.write("Build start time: " + caseStart + "\n")
            manifestPath = casePath + i + "/manifest.json"

            if os.path.exists(ConstPath + "/tools/crosswalk/"):
                apk_list = glob.glob(ConstPath + "/tools/crosswalk/*.apk")
            else:
                apk_list = glob.glob(ConstPath + "/../../tools/crosswalk/*.apk")
            for item in apk_list:
                os.remove(item)

            cmd ="python make_apk.py --package=org.xwalk.test --arch=" + ARCH + " --manifest="
            status, info = commands.getstatusoutput(cmd + manifestPath)
            if flag == "negative":
                if status == 0:
                    print "Generate APK ---------------->O.K"
                    result = "FAIL"
                    manifestLog.write(result + "\n") 
                else:
                    print "Generate APK ---------------->Error"
                    result = "PASS"
                    manifestLog.write(result + "\n")
            else:
                if status != 0:
                    print "Generate APK ---------------->Error"
                    result = "FAIL"
                    manifestLog.write(result + "\n" + info + "\n")
                else:
                    print "Generate APK ---------------->O.K"
                    if os.path.exists(ConstPath + "/tools/crosswalk/"):
                        apkpath = ConstPath + "/tools/crosswalk/*.apk"
                    else:
                        apkpath = ConstPath + "/../../tools/crosswalk/*.apk"
                    targetDir = ConstPath + "/apks/" + ARCH + "/" + i
                    if not os.path.exists(targetDir):
                        os.mkdir(targetDir)
                    apk_list = glob.glob(apkpath)
                    try:
                        for item in apk_list:
                            name = item.rsplit(os.sep)[-1]
                            shutil.copyfile(item, targetDir + "/" + name)
                    except IOError, e:
                        traceback.print_exc()
                        sys.exit(1)
                    else:
                        result = "PASS"
                        manifestLog.write(result + "\n")
            caseEnd = time.strftime("%Y-%m-%d %H:%M:%S")
            manifestLog.write("Build end time: " + caseEnd + "\n\n")
            manifestLog.flush()
            print "Package Result :" + result
            fp = open(ConstPath + "/report/packRes.txt", 'a+')
            tt = i + "\t" + flag + "\t" + result + "\n"
            fp.write(tt)
            fp.close()
        manifestLog.close()
    except Exception,e:
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

if __name__ == "__main__":
    genPackage()
