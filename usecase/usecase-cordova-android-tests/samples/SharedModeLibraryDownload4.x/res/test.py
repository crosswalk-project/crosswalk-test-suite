import os
import commands
import sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.realpath('..'))
import comm
from optparse import OptionParser

comm.setUp()
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


comm.installCrosswalk("shared")

app_name = "SharedModeLibraryDownload"
pkg_name = "com.example.sharedModeLibraryDownload"
current_path_tmp = os.getcwd()
comm.create(app_name, pkg_name, current_path_tmp)

menifest_path = os.path.join(current_path_tmp, app_name, "platforms", "android")
comm.replaceUserString(
        menifest_path,
        'AndroidManifest.xml',
        'android:supportsRtl="true">',
        'android:supportsRtl="true">\n        <meta-data android:name="xwalk_apk_url" android:value="' + BUILD_PARAMETERS.url + '" />')
if comm.CROSSWALK_BRANCH == "beta":
    comm.installWebviewPlugin("shared", "org.xwalk:xwalk_shared_library_beta:%s" % comm.CROSSWALK_VERSION)
else:
    comm.installWebviewPlugin("shared", "%s" % comm.CROSSWALK_VERSION)

comm.build(app_name)
comm.run(app_name)
comm.checkBuildResult()
comm.checkRunResult(pkg_name)




