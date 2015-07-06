import os
import commands
import sys
from optparse import OptionParser
PKG_MODES = ["shared", "embedded"]

try:
    usage = "Usage: ./test.py -m shared"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-m",
        "--mode",
        dest="pkgmode",
        help="specify the apk mode, not for cordova version 4.0, e.g. shared, embedded")
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
if os.path.exists("cordova-android"):
    os.system("rm -rf cordova-android")
os.system("git clone https://github.com/apache/cordova-android.git")
if os.path.exists("cordova-plugin-crosswalk-webview"):
    os.system("rm -rf cordova-plugin-crosswalk-webview")
os.system("git clone https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview.git")
if os.path.exists("cordovaPackage"):
    os.system("rm -rf cordovaPackage")
os.system("cordova-android/bin/create cordovaPackage com.example.cordovaPackage2 CordovaPackage")
os.chdir("./cordovaPackage")
os.system('sed -i "s/13+/14+/g" ../cordova-plugin-crosswalk-webview/src/android/xwalk.gradle')
os.system("plugman install --platform android --plugin ../cordova-plugin-crosswalk-webview/ --project .")
if BUILD_PARAMETERS.pkgmode == "shared":
    os.system('sed -i "s/<preference name=\\"lib_mode\\" value=\\"embedd\\"/<preference name=\\"lib_mode\\" value=\\"shared\\"/g" res/xml/config.xml')
    os.system('sed -i "s/<application/<application android:name=\\"org.xwalk.core.XWalkApplication\\"/g" AndroidManifest.xml')
    os.system('sed -i "s/        loadUrl/    }\\n\\n    @Override\\n    protected void onXWalkReady() {\\n        super.init();\\n        loadUrl/g" src/com/example/cordovaPackage2/MainActivity.java')
    os.system('sed -i "s/public class CordovaActivity extends Activity {/import org.xwalk.core.XWalkActivity;\\npublic abstract class CordovaActivity extends XWalkActivity implements CordovaInterface {/g" CordovaLib/src/org/apache/cordova/CordovaActivity.java')

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
