import os
import commands
import sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.realpath('..'))
import comm
from optparse import OptionParser
global CROSSWALK_VERSION
global CROSSWALK_BRANCH
with open("../../tools/VERSION", "rt") as pkg_version_file:
    pkg_version_raw = pkg_version_file.read()
    pkg_version_file.close()
    pkg_version_json = json.loads(pkg_version_raw)
    CROSSWALK_VERSION = pkg_version_json["main-version"]
    CROSSWALK_BRANCH = pkg_version_json["crosswalk-branch"]

try:
    usage = "Usage: ./test.py -u [http://host/XWalkRuntimeLib.apk]"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-u",
        "--url",
        dest="url",
        help="specify the url, e.g. http://host/XWalkRuntimeLib.apk")
    global BUILD_PARAMETERS
    (BUILD_PARAMETERS, args) = opts_parser.parse_args()
except Exception as e:
    print "Got wrong options: %s, exit ..." % e
    sys.exit(1)

if not BUILD_PARAMETERS.url:
    print "Please add the -u parameter for the url of XWalkRuntimeLib.apk"
    sys.exit(1)

version_parts = CROSSWALK_VERSION.split('.')
if len(version_parts) < 4:
    print "The crosswalk version is not configured exactly!"
    sys.exit(1)

comm.installCrosswalk("shared")

library_url = BUILD_PARAMETERS.url
library_url = library_url.replace("/", "\\/")

app_name = "SharedModeLibraryDownload"
pkg_name = "com.example.sharedModeLibraryDownload"
comm.create(app_name, pkg_name, os.getcwd())

version_cmd = ""
if CROSSWALK_BRANCH == "beta":
    if BUILD_PARAMETERS.pkgmode == "shared":
        version_cmd = "--variable XWALK_VERSION=\"org.xwalk:xwalk_shared_library_beta:%s\"" % CROSSWALK_VERSION
    else:
        version_cmd = "--variable XWALK_VERSION=\"org.xwalk:xwalk_core_library_beta:%s\"" % CROSSWALK_VERSION
else:
    version_cmd = "--variable XWALK_VERSION=\"%s\"" % CROSSWALK_VERSION

add_plugin_cmd = "cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview" \
    " %s --variable XWALK_MODE=\"shared\"" % version_cmd
print add_plugin_cmd
os.system(add_plugin_cmd)
os.system('sed -i "s/android:supportsRtl=\\"true\\">/android:supportsRtl=\\"true\\">\\n        <meta-data android:name=\\"xwalk_apk_url\\" android:value=\\"' + library_url + '\\" \\/>/g" platforms/android/AndroidManifest.xml')

os.system("cordova build android")
os.system("cordova run")
lsstatus = commands.getstatusoutput("ls ./platforms/android/build/outputs/apk/*.apk")
if lsstatus[0] == 0:
    print "Build Package Successfully"
else:
    print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep com.example.sharedModeLibraryDownload")
if pmstatus[0] == 0:
    print "Package Name Consistent"
else:
    print "Package Name Inconsistent"
