import os
import commands
import sys
import json
from optparse import OptionParser
PKG_MODES = ["shared", "embedded"]
global CROSSWALK_VERSION
with open("../../tools/VERSION", "rt") as pkg_version_file:
    pkg_version_raw = pkg_version_file.read()
    pkg_version_file.close()
    pkg_version_json = json.loads(pkg_version_raw)
    CROSSWALK_VERSION = pkg_version_json["main-version"]

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

version_parts = CROSSWALK_VERSION.split('.')
if len(version_parts) < 4:
    print "The crosswalk version is not configured exactly!"
    sys.exit(1)
versionType = version_parts[3]
if versionType == '0':
    username = commands.getoutput("echo $USER")
    if BUILD_PARAMETERS.pkgmode == "shared":
        repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
            "xwalk_shared_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
            "xwalk_shared_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
    else:
        repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)

    if not os.path.exists(repository_aar_path) or not os.path.exists(repository_pom_path):
        if BUILD_PARAMETERS.pkgmode == "shared":
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-shared-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_shared_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-shared-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
        else:
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_core_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
        os.system(wget_cmd)
        os.system(install_cmd)

if os.path.exists("cordova-android"):
    os.system("rm -rf cordova-android")
os.system("git clone https://github.com/apache/cordova-android.git")
if os.path.exists("cordovaPackage"):
    os.system("rm -rf cordovaPackage")
os.system("cordova-android/bin/create cordovaPackage com.example.cordovaPackage2 CordovaPackage")
os.chdir("./cordovaPackage")
os.system("plugman install --platform android --plugin ../../../tools/cordova-plugin-crosswalk-webview/ --project .")
os.system('sed -i "s/<preference default=\\".*\\" name=\\"XWALK_VERSION\\"/<preference default=\\"%s\\" name=\\"XWALK_VERSION\\"/g" res/xml/config.xml' % CROSSWALK_VERSION)
if BUILD_PARAMETERS.pkgmode == "shared":
    os.system('sed -i "s/<preference default=\\"embedded\\" name=\\"XWALK_MODE\\"/<preference default=\\"shared\\" name=\\"XWALK_MODE\\"/g" res/xml/config.xml')
os.system("./cordova/build")
os.system("./cordova/run")
lsstatus = commands.getstatusoutput("ls ./build/outputs/apk/*.apk")
if lsstatus[0] == 0:
    print "Build Package Successfully"
else:
    print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep com.example.cordovaPackage2")
if pmstatus[0] == 0:
    print "Package Name Consistent"
else:
    print "Package Name Inconsistent"
