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
if os.path.exists("cordova-plugin-crosswalk-webview"):
    os.system("rm -rf cordova-plugin-crosswalk-webview")
os.system("git clone https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview.git")
if os.path.exists("SharedModeLibraryDownload"):
    os.system("rm -rf SharedModeLibraryDownload")
os.system("cordova create SharedModeLibraryDownload com.example.sharedModeLibraryDownload SharedModeLibraryDownload")
os.chdir("./SharedModeLibraryDownload")
os.system('sed -i "s/<widget/<widget android-activityName=\\"SharedModeLibraryDownload\\"/g" config.xml')
os.system('sed -i "s/<\/widget>/    <allow-navigation href=\\"*\\" \/>\\n<\/widget>/g" config.xml')
os.system("cordova platform add android")
os.system("cordova plugin add ../cordova-plugin-crosswalk-webview")
os.system('sed -i "s/<preference name=\\"lib_mode\\" value=\\"embedd\\"/<preference name=\\"lib_mode\\" value=\\"shared\\"/g" config.xml')
os.system('sed -i "s/<application/<application android:name=\\"org.xwalk.core.XWalkApplication\\"/g" platforms/android/AndroidManifest.xml')
os.system('sed -i "s/android:supportsRtl=\\"true\\">/android:supportsRtl=\\"true\\">\\n        <meta-data android:name=\\"xwalk_apk_url\\" android:value=\\"' + library_url + '\\" \\/>/g" platforms/android/AndroidManifest.xml')
os.system('sed -i "s/        loadUrl/    }\\n\\n    @Override\\n    protected void onXWalkReady() {\\n        super.init();\\n        loadUrl/g" platforms/android/src/com/example/sharedModeLibraryDownload/SharedModeLibraryDownload.java')
os.system('sed -i "s/public class CordovaActivity extends Activity {/import org.xwalk.core.XWalkActivity;\\npublic abstract class CordovaActivity extends XWalkActivity implements CordovaInterface {/g" platforms/android/CordovaLib/src/org/apache/cordova/CordovaActivity.java')

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
