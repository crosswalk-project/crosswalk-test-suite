import os
import commands
import sys
from optparse import OptionParser

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
library_url = BUILD_PARAMETERS.url
library_url = library_url.replace("/", "\\/")
if os.path.exists("SharedModeLibraryDownload"):
    os.system("rm -rf SharedModeLibraryDownload")
os.system("./bin/create SharedModeLibraryDownload com.example.sharedModeLibraryDownload1 SharedModeLibraryDownload --xwalk-apk-url=" + BUILD_PARAMETERS.url + " --xwalk-shared-library")
os.chdir("./SharedModeLibraryDownload")
os.system("./cordova/build")
os.system("./cordova/run")
lsstatus = commands.getstatusoutput("ls ./out/SharedModeLibraryDownload*.apk")
if lsstatus[0] == 0:
    print "Build Package Successfully"
else:
    print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep com.example.sharedModeLibraryDownload1")
if pmstatus[0] == 0:
    print "Package Name Consistent"
else:
    print "Package Name Inconsistent"
