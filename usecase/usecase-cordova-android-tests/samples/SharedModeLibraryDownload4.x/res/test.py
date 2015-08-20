import os
import commands
import sys
import json
from optparse import OptionParser
global CROSSWALK_VERSION
with open("../../tools/VERSION", "rt") as pkg_version_file:
    pkg_version_raw = pkg_version_file.read()
    pkg_version_file.close()
    pkg_version_json = json.loads(pkg_version_raw)
    CROSSWALK_VERSION = pkg_version_json["main-version"]

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
versionType = version_parts[3]
if versionType == '0':
    username = commands.getoutput("echo $USER")
    repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
            "xwalk_shared_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
    repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
            "xwalk_shared_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)

    if not os.path.exists(repository_aar_path) or not os.path.exists(repository_pom_path):
        wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-shared-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
        install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_shared_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-shared-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
        os.system(wget_cmd)
        os.system(install_cmd)

library_url = BUILD_PARAMETERS.url
library_url = library_url.replace("/", "\\/")
if os.path.exists("SharedModeLibraryDownload"):
    os.system("rm -rf SharedModeLibraryDownload")
os.system("cordova create SharedModeLibraryDownload com.example.sharedModeLibraryDownload SharedModeLibraryDownload")
os.chdir("./SharedModeLibraryDownload")
os.system('sed -i "s/<widget/<widget android-activityName=\\"SharedModeLibraryDownload\\"/g" config.xml')
os.system('sed -i "s/<\/widget>/    <allow-navigation href=\\"*\\" \/>\\n<\/widget>/g" config.xml')
os.system("cordova platform add android")
add_plugin_cmd = "cordova plugin add ../../../tools/cordova-plugin-crosswalk-webview" \
    " --variable XWALK_VERSION=\"%s\" --variable XWALK_MODE=\"shared\"" % CROSSWALK_VERSION
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
