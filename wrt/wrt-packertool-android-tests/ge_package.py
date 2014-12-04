#!/usr/bin/env python
import sys, os, os.path, time, shutil
import commands, glob, traceback

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
ARCH = "x86"

def caseExecute():
    try:
        global ARCH
        
        #genarate package and execute
        packageInfo = open(ConstPath + "/report/packageInfo.txt", 'a+')
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
            
            
            
        print "Genarate APK ---------------->Start"
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
            packageInfo.write(i+ "\n")
            packageInfo.write("Build start time: " + caseStart + "\n")
            dirInfo = open(ConstPath + "/report/targetDir.txt")
            dirInfo = dirInfo.readlines()
            cmdInfo = open(casePath + i + "/cmd.txt")
            command = cmdInfo.read()
            print "Packer Tool Command:"
            print command

            if os.path.exists(ConstPath + "/tools/crosswalk/"):
                apk_list = glob.glob(ConstPath + "/tools/crosswalk/*.apk")
            else:
                apk_list = glob.glob(ConstPath + "/../../tools/crosswalk/*.apk")
            for item in apk_list:
                os.remove(item)
            packstatus = commands.getstatusoutput(command)
            if flag == "negative":
                if packstatus[0] == 0:
                    print "Genarate APK ---------------->O.K"
                    packageInfo.write("Generate apk succeed\n")
                    result = "FAIL"
                else:
                    print "Genarate APK ---------------->Error"
                    packageInfo.write("Generate apk failed\n")
                    result = "PASS"
            else:
                if packstatus[0] != 0:
                    print "Genarate APK ---------------->Error"
                    packageInfo.write("Generate apk failed\n" + packstatus[1] + "\n")
                    result = "FAIL"
                else:
                    print "Genarate APK ---------------->O.K"
                    packageInfo.write("Generate apk succeed\n")
                    if os.path.exists(ConstPath + "/tools/crosswalk/"):
                        apkpath = ConstPath + "/tools/crosswalk/*.apk"
                    else:
                        apkpath = ConstPath + "/../../tools/crosswalk/*.apk"
                    targetDir = ConstPath + "/apks/" + ARCH + "/" + i
                    if not os.path.exists(targetDir):
                        os.mkdir(targetDir)
                    apk_list = glob.glob(apkpath)
                    try:
                        if "target-dir" in command:
                            for tar in dirInfo:
                                tarNum = tar[:13].strip()
                                tarDir = tar[13:].strip()
                                
                                if i in tarNum:
                                    if not tarDir.startswith("/") or tarDir.startswith("./"):
                                        if os.path.exists(ConstPath + "/tools/crosswalk/"):
                                            os.chdir(ConstPath + "/tools/crosswalk/" + tarDir)
                                        else:
                                            os.chdir(ConstPath + "/../../tools/crosswalk/" + tarDir)
                                    else:
                                        os.chdir(tarDir)
                                    apkPath = os.getcwd() + "/*.apk"
                                    apk_list = glob.glob(apkPath)
                                    for item in apk_list:
                                        name = item.rsplit(os.sep)[-1]
                                        shutil.copyfile(item, targetDir + "/" + name)
                                        if os.path.exists(ConstPath + "/tools/crosswalk/"):
                                            os.chdir(ConstPath + "/tools/crosswalk/")
                                        else:
                                            os.chdir(ConstPath + "/../../tools/crosswalk/")  
                        else:
                            for item in apk_list:
                                name = item.rsplit(os.sep)[-1]
                                shutil.copyfile(item, targetDir + "/" + name)
                    except IOError, e:
                        traceback.print_exc()
                        sys.exit(1)
                    else:
                        result = "PASS"
                        packageInfo.write(result + "\n")
            caseEnd = time.strftime("%Y-%m-%d %H:%M:%S")
            packageInfo.write("Build end time: " + caseEnd + "\n\n")
            packageInfo.flush()
            print "Package Result: ",result
            pr = open(ConstPath + "/report/packRes.txt", 'a+')
            tt = i + "\t" + flag + "\t" + result + "\n"
            pr.write(tt)
            pr.close()
        packageInfo.close()
        print "Excute cases ------------------------->O.K"
    except Exception,e:
        print Exception,":",e
        print "Execute case ---------------->Error"
        sys.exit(1)

if __name__=="__main__":
    caseExecute()
