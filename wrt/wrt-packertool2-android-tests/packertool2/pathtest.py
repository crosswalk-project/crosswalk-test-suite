#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):   
    def test_path(self):
        comm.setUp()
        chmodstatus = commands.getstatusoutput("chmod +x " + comm.Pck_Tools + "make_apk.py")
        cmd = "make_apk.py --package=org.hello.world --name=world --arch=%s --mode=%s --app-url=https://crosswalk-project.org/" % \
        (comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
            inststatus = commands.getstatusoutput("adb install " + comm.AppName)
            if inststatus[0] == 0:
                print "Install APK ----------------> OK"
                print "Find Package in device ---------------->Start"
                pmstatus = commands.getstatusoutput("adb shell pm list packages |grep org.hello.world")
                if pmstatus[0] == 0:
                    print "Find Package in device ---------------->O.K"
                    print "Launch APK ---------------->Start"
                    launchstatus = commands.getstatusoutput("adb shell am start -n org.hello.world/.TestActivity")
                    if launchstatus[0] !=0:
                        print "Launch APK ---------------->Error"
                    else:
                        print "Launch APK ---------------->OK"
                        print "Stop APK ---------------->Start"
                        stopstatus = commands.getstatusoutput("adb shell am force-stop org.hello.world")
                        if stopstatus[0] == 0:
                            print "Stop APK ---------------->O.K"
                            print "Uninstall APK ---------------->Start"
                            unistatus = commands.getstatusoutput("adb uninstall org.hello.world")
                            if unistatus[0] == 0:
                                print "Uninstall APK ---------------->O.K"
                            else:
                                print "Uninstall APK ---------------->Error"
                        else:
                            print "Stop APK ---------------->Error"
                            os.system("adb uninstall org.hello.world")
                else:
                    print "Find Package in device ---------------->Error"
                    os.system("adb uninstall org.hello.world")
            else:
                print "Install APK ----------------> Error"
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)
        os.chdir("../packertools2")

if __name__ == '__main__':  
    unittest.main()  
