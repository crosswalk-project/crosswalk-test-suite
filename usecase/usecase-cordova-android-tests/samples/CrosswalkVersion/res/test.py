import os
import commands
import sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.realpath('..'))
import comm
from optparse import OptionParser
PKG_MODES = ["shared", "embedded"]
PKG_ARCHS = ["x86", "arm"]

comm.setUp()
try:
    usage = "Usage: ./test.py -m shared -a x86"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-m",
        "--mode",
        dest="pkgmode",
        help="specify the apk mode, not for cordova version 4.0, e.g. shared, embedded")
    opts_parser.add_option(
        "-a",
        "--arch",
        dest="pkgarch",
        help="specify the apk arch, e.g. x86, arm")
    global BUILD_PARAMETERS
    (BUILD_PARAMETERS, args) = opts_parser.parse_args()
except Exception as e:
    print "Got wrong options: %s, exit ..." % e
    sys.exit(1)


if not BUILD_PARAMETERS.pkgmode:
    print "Please add the -m parameter for the pkgmode"
    sys.exit(1)
elif BUILD_PARAMETERS.pkgmode and not BUILD_PARAMETERS.pkgmode in PKG_MODES:
    print "Wrong pkg-mode, only support: %s, exit ..." % PKG_MODES
    sys.exit(1)

if not BUILD_PARAMETERS.pkgarch:
    print "Please add the -a parameter for the pkgarch"
    sys.exit(1)
elif BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
    print "Wrong pkg-arch, only support: %s, exit ..." % PKG_ARCHS
    sys.exit(1)

if os.path.exists("CrosswalkVersion"):
    os.system("rm -rf CrosswalkVersion")
os.system("cordova create CrosswalkVersion com.example.crosswalkVersion1 CrosswalkVersion")
os.chdir("./CrosswalkVersion")

os.system('sed -i "s/<widget/<widget android-activityName=\\"CrosswalkVersion\\"/g" config.xml')
os.system('sed -i "s/<\/widget>/    <allow-navigation href=\\"*\\" \/>\\n<\/widget>/g" config.xml')
os.system("cordova platform add android")
os.system('cp ../index.html www/index.html')
main_version = comm.CROSSWALK_VERSION.split('.')[0]

latestVersion = ''
if comm.CROSSWALK_BRANCH == "stable" or comm.CROSSWALK_BRANCH == "beta":
    latestVersion = comm.getLatestCrosswalkVersion(comm.CROSSWALK_BRANCH)

if comm.CROSSWALK_BRANCH == "beta":
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % latestVersion)

    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"org.xwalk:xwalk_core_library_beta:%s+\"" % (BUILD_PARAMETERS.pkgmode, main_version))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_beta_1.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_beta_1.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"org.xwalk:xwalk_core_library_beta:%s+\\" \/>/g" config.xml' % main_version)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_beta_2.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_beta_2.apk')

    os.system('cp ../index.html www/index.html')
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % comm.CROSSWALK_VERSION)

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"org.xwalk:xwalk_core_library_beta:%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_beta_3.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_beta_3.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"org.xwalk:xwalk_core_library_beta:%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_beta_4.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_beta_4.apk')

    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_beta_1.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_beta_2.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_beta_3.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_beta_4.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"

elif comm.CROSSWALK_BRANCH == "stable":
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % latestVersion)

    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"%s+\"" % (BUILD_PARAMETERS.pkgmode, main_version))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_1.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_1.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"%s\"" % (BUILD_PARAMETERS.pkgmode, main_version))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_2.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_2.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"xwalk_core_library:%s+\"" % (BUILD_PARAMETERS.pkgmode, main_version))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_3.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_3.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"org.xwalk:xwalk_core_library:%s+\"" % (BUILD_PARAMETERS.pkgmode, main_version))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_4.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_4.apk')


    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"%s+\\" \/>/g" config.xml' % main_version)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_5.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_5.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"%s\\" \/>/g" config.xml' % main_version)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_6.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_6.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"xwalk_core_library:%s+\\" \/>/g" config.xml' % main_version)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_7.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_7.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"org.xwalk:xwalk_core_library:%s+\\" \/>/g" config.xml' % main_version)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_8.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_8.apk')

    os.system('cp ../index.html www/index.html')
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % comm.CROSSWALK_VERSION)

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_9.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_9.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"xwalk_core_library:%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_10.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_10.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"org.xwalk:xwalk_core_library:%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_11.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_11.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_12.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_12.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"xwalk_core_library:%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_13.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_13.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"org.xwalk:xwalk_core_library:%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_stable_14.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_stable_14.apk')

    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_1.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_2.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_3.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_4.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_5.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_6.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_7.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_8.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_9.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_10.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_11.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_12.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_13.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_stable_14.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"

elif comm.CROSSWALK_BRANCH == "canary":
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % comm.CROSSWALK_VERSION)

    comm.installCrosswalk(BUILD_PARAMETERS.pkgmode)
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_1.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_1.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"xwalk_core_library:%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_2.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_2.apk')

    os.system("cordova plugin remove cordova-plugin-crosswalk-webview")
    os.system("cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview --variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"org.xwalk:xwalk_core_library:%s\"" % (BUILD_PARAMETERS.pkgmode, comm.CROSSWALK_VERSION))
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_3.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_3.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_4.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_4.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"xwalk_core_library:%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_5.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_5.apk')

    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\" value=\\"org.xwalk:xwalk_core_library:%s\\" \/>/g" config.xml' % comm.CROSSWALK_VERSION)
    os.system("cordova build android")
    if BUILD_PARAMETERS.pkgarch == "x86":
        os.system('cp platforms/android/build/outputs/apk/android-x86-debug.apk ../CrosswalkVersion_canary_6.apk')
    else:
        os.system('cp platforms/android/build/outputs/apk/android-armv7-debug.apk ../CrosswalkVersion_canary_6.apk')

    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_1.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_2.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_3.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_4.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_5.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
    lsstatus = commands.getstatusoutput("ls ../CrosswalkVersion_canary_6.apk")
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"
else:
    print "CROSSWALK_BRANCH in VERSION file is unavailable"



