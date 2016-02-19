import os
import commands
import sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.realpath('..'))
import comm
from optparse import OptionParser
PKG_MODES = ["shared", "embedded"]

comm.setUp()
try:
    usage = "Usage: ./test.py -m shared"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-m",
        "--mode",
        dest="pkgmode",
        help="specify the apk mode, e.g. shared, embedded")
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

comm.installCrosswalk(BUILD_PARAMETERS.pkgmode)
app_name = "CordovaPackage"
pkg_name = "com.example.cordovaPackage2"

current_path_tmp = os.getcwd()
cordova_android_path = os.path.join(current_path_tmp, "cordova-android")
if os.path.exists(cordova_android_path):
    comm.doRemove([cordova_android_path])
os.system("git clone https://github.com/apache/cordova-android.git")

project_path = os.path.join(current_path_tmp, app_name)
if os.path.exists(project_path):
    comm.doRemove([project_path])

os.system("cordova-android/bin/create %s %s %s" % (app_name, pkg_name, app_name))
os.chdir(project_path)
os.system("plugman install --platform android --plugin ../../../tools/cordova-plugin-crosswalk-webview/ --project .")

pkg_mode_tmp = "shared"
if BUILD_PARAMETERS.pkgmode == "embedded":
    pkg_mode_tmp = "core"

xwalk_version = "%s" % comm.CROSSWALK_VERSION
if comm.CROSSWALK_BRANCH == "beta":
    xwalk_version = "org.xwalk:xwalk_%s_library_beta:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION)

os.system('sed -i "s/<preference default=\\".*\\" name=\\"xwalkVersion\\"/<preference default=\\"%s\\" name=\\"xwalkVersion\\"/g" res/xml/config.xml' % xwalk_version)

if BUILD_PARAMETERS.pkgmode == "shared":
    os.system('sed -i "s/<preference default=\\"embedded\\" name=\\"xwalkMode\\"/<preference default=\\"shared\\" name=\\"xwalkMode\\"/g" res/xml/config.xml')
 
os.system("./cordova/build")
os.system("./cordova/run")

comm.checkApkExist("./build/outputs/apk/*.apk")
comm.checkApkRun(pkg_name)

