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

import sys, os, os.path, shutil, time
import comm, traceback, glob, json

def tryRunApp(num, caseDir):
    try:
        global result
        comm.setUp()
        if os.path.exists(comm.ConstPath + "/testapp/"):
            apk_list = glob.glob(comm.ConstPath + "/testapp/*" + comm.apktype)
        for item in apk_list:
            os.remove(item)
        os.chdir(comm.ConstPath + "/testapp/")
        appPath = comm.ConstPath + "/tcs/" + num
        flag = num[-8:].strip()
        if comm.PLATFORMS == "android":
            build_cmd = " --crosswalk=" + comm.crosswalkVersion + ' --targets="' + comm.TARGETS + '" '
        elif comm.PLATFORMS == "windows":
            build_cmd = " --crosswalk=" + comm.crosswalkVersion + " "
        else:
            build_cmd = " "
        cmd = comm.HOST_PREFIX + comm.apptools + " --platforms=" + comm.PLATFORMS + build_cmd + appPath
        (status, info) = comm.getstatusoutput(cmd)
        if flag == "negative":
            if status == 0:
                print "Generate APK ---------------->O.K"
                result = "FAIL"
                return result
            else:
                print "Generate APK ---------------->Error"
                result = "PASS"
                return result
        else:
            if status != 0:
                print "Generate APK ---------------->Error"
                result = "FAIL"
                return result
            else:
                print "Generate APK ---------------->O.K"
                if os.path.exists(comm.ConstPath + "/testapp/"):
                    apkpath = comm.ConstPath + "/testapp/*" + comm.apktype
                targetDir = comm.ConstPath + "/apks/" + num
                if not os.path.exists(targetDir):
                    os.mkdir(targetDir)
                apk_list = glob.glob(apkpath)
                apkLength = 0
                for item in apk_list:
                    if comm.PLATFORMS == "android":
                        if "x86" in item or "shared" in item:
                            if comm.BIT == "64" and "64" in item:
                                apkLength = apkLength + 1
                            elif comm.BIT == "32":
                                apkLength = apkLength + 1
                        if "arm" in item or "shared" in item:
                            if comm.BIT == "64" and "64" in item:
                                apkLength = apkLength + 1
                            elif comm.BIT == "32":
                                apkLength = apkLength + 1
                    name = item.rsplit(os.sep)[-1]
                    shutil.copyfile(item, targetDir + "/" + name)
                if comm.PLATFORMS == "android" and comm.ARCH_ARM != "" and comm.ARCH_X86 != "" and comm.ANDROID_MODE != "shared":
                    if apkLength != 2:
                        result = "FAIL"
                    else:
                        result = "PASS"
                else:
                    apkLength = len(apk_list)
                    if apkLength != 1:
                        result = "FAIL"
                    else:
                        result = "PASS"
                if result == "PASS":
                    apkDir = comm.ConstPath + "/apks/"
                    apk_list = os.listdir(apkDir + num)
                    for apk in apk_list:
                        if comm.PLATFORMS == "android":
                            if "release" not in apk and comm.ARCH_ARM != "" and ("arm" in apk or "shared" in apk):
                                print "##########"
                                print num
                                print "##########"
                                print "Install APK ---------------->Start"
                                return_inst_code_arm = os.system("adb -s " + comm.device_arm + " install -r " + apkDir + num + "/" + apk)
                                if return_inst_code_arm == 0:
                                    print "Install APK ---------------->O.K"
                                    (return_pm_code_arm, pmstatus_arm) = comm.getstatusoutput("adb -s " + comm.device_arm + " shell pm list packages |grep org.xwalk.tests")
                                    if return_pm_code_arm == 0:
                                        print "Find Package in device ---------------->O.K"
                                        (return_laun_code_arm, launstatus_arm) = comm.getstatusoutput("adb -s " + comm.device_arm + " shell am start -n org.xwalk.tests/.TestActivity")
                                        if return_laun_code_arm != 0 and launstatus_arm[0] != "Error":
                                            print "Launch APK ---------------->Error"
                                            os.system("adb -s " + comm.device_arm + " uninstall org.xwalk.tests")
                                            result = "FAIL"
                                            return result
                                        else:
                                            print "Launch APK ---------------->O.K"
                                            return_stop_code_arm = os.system("adb -s " + comm.device_arm + " shell am force-stop org.xwalk.tests")
                                            if return_stop_code_arm == 0:
                                                print "Stop APK ---------------->O.K"
                                                uninstatus_arm = os.popen("adb -s " + comm.device_arm + " uninstall org.xwalk.tests").read()
                                                if uninstatus_arm != "Success":
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
                                                os.system("adb -s " + comm.device_arm + " uninstall org.xwalk.tests")
                                                return result
                                    else:
                                        print "Find Package in device ---------------->Error"
                                        os.system("adb -s " + comm.device_arm + " uninstall org.xwalk.tests")
                                        result = "FAIL"
                                        return result
                                else:
                                    print "Install APK ---------------->Error"
                                    result = "FAIL"
                                    return result
                            if "release" not in apk and comm.ARCH_X86 != "" and ("x86" in apk or "shared" in apk):
                                print "##########"
                                print num
                                print "##########"
                                print "Install APK ---------------->Start"
                                return_inst_code_x86 = os.system("adb -s " + comm.device_x86 + " install -r " + apkDir + num + "/" + apk)
                                if return_inst_code_x86 == 0:
                                    print "Install APK ---------------->O.K"
                                    (return_pm_code_x86, pmstatus_x86) = comm.getstatusoutput("adb -s " + comm.device_x86 + " shell pm list packages |grep org.xwalk.tests")
                                    if return_pm_code_x86 == 0:
                                        print "Find Package in device ---------------->O.K"
                                        (return_laun_code_x86, launstatus_x86) = comm.getstatusoutput("adb -s " + comm.device_x86 + " shell am start -n org.xwalk.tests/.TestActivity")
                                        if return_laun_code_x86 != 0 and launstatus_x86[0] != "Error":
                                            print "Launch APK ---------------->Error"
                                            os.system("adb -s " + comm.device_x86 + " uninstall org.xwalk.tests")
                                            result = "FAIL"
                                            return result
                                        else:
                                            print "Launch APK ---------------->O.K"
                                            return_stop_code_x86 = os.system("adb -s " + comm.device_x86 + " shell am force-stop org.xwalk.tests")
                                            if return_stop_code_x86 == 0:
                                                print "Stop APK ---------------->O.K"
                                                uninstatus_x86 = os.popen("adb -s " + comm.device_x86 + " uninstall org.xwalk.tests").read()
                                                if uninstatus_x86 != "Success":
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
                                                os.system("adb -s " + comm.device_x86 + " uninstall org.xwalk.tests")
                                                return result
                                    else:
                                        print "Find Package in device ---------------->Error"
                                        os.system("adb -s " + comm.device_x86 + " uninstall org.xwalk.tests")
                                        result = "FAIL"
                                        return result
                                else:
                                    print "Install APK ---------------->Error"
                                    result = "FAIL"
                                    return result
                        elif comm.PLATFORMS == "deb":
                            project_name = apk.split("_")[0]
                            print "Begin install deb file ", project_name
                            (inststatus, instoutput) = comm.getstatusoutput("sudo dpkg -i " + apk)
                            if inststatus == 0:
                                print "Begin search deb file ", project_name
                                try:
                                    (launstatus, launoutput) = comm.getstatusoutput("dpkg -l " + project_name)
                                    if launstatus == 0:
                                        print "Begin launch deb file ", project_name
                                        os.system(project_name + " & sleep 5")
                                        # wait 3 second, then check application is running
                                        time.sleep(3)
                                        (checkstatus, checkoutput) = comm.getstatusoutput("ps -ef | grep " + project_name + " | grep -v \"grep\" | wc -l")
                                        if checkstatus == 0:
                                            # kill application
                                            (killstatus, killoutput) = comm.getstatusoutput("ps aux | grep xwalk | grep " + project_name + " | grep -v \"grep\"")
                                            for ps in killoutput[0].split("\n"):
                                                for pid in ps.split(" "):
                                                    if pid.isdigit():
                                                        os.kill(int(pid), 9)
                                                        break
                                            if killstatus == 0:
                                                print "Begin uninstall deb file ", project_name
                                                (uninstatus, uninoutput) = comm.getstatusoutput("sudo dpkg -P " + project_name)
                                                if uninstatus == 0:
                                                    result = "PASS"
                                                    return result
                                                else:
                                                    result = "FAIL"
                                                    return result
                                            else:
                                                os.system("sudo dpkg -P " + project_name)
                                                result = "FAIL"
                                                return result
                                        else:
                                            os.system("sudo dpkg -P " + project_name)
                                            result = "FAIL"
                                            return result
                                    else:
                                        os.system("sudo dpkg -P " + project_name)
                                        result = "FAIL"
                                        return result
                                except Exception,e:
                                    print Exception,":",e
                                    print "Try run webapp ---------------->Error"
                                    os.system("sudo dpkg -P " + project_name)
                                    with open(appPath + "/manifest.json") as json_file:
                                        data = json.load(json_file)
                                    result = "FAIL"
                                    if data['start_url'].strip(os.linesep) == " ":
                                        result = "PASS"
                                    return result
                            else:
                                result = "FAIL"
                                return result
                return result
    except Exception,e:
        print Exception,":",e
        print "Try run webapp ---------------->Error"
        sys.exit(1)
