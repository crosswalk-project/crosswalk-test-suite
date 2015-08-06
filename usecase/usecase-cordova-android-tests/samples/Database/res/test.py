import os
import commands
if os.path.exists("database"):
    os.system("rm -rf database")
os.system("cordova create database org.xwalk.database database")
os.chdir("./database")
os.system("cordova platform add android")
os.system("cp -r ../database_source/* www/")
os.system("cordova build android")
lsstatus = commands.getstatusoutput("ls ./platforms/android/build/outputs/apk/android-debug.apk &>/dev/null")
if lsstatus[0] == 0:
    os.system("cp ./platforms/android/build/outputs/apk/android-debug.apk ../../../database_upstream.apk")
    print "Build Package Successfully"
else:
    print "Build Package Error"
