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
if os.path.exists("cordova-plugin-crosswalk-webview"):
    os.system("rm -rf cordova-plugin-crosswalk-webview")
os.system("git clone https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview.git")
if os.path.exists("Language"):
    os.system("rm -rf Language")
os.system("cordova create Language com.example.language Language")
os.chdir("./Language")
os.system('sed -i "s/13+/14+/g" ../cordova-plugin-crosswalk-webview/platforms/android/xwalk.gradle')
os.system('sed -i "s/<widget/<widget android-activityName=\\"Language\\"/g" config.xml')
os.system('sed -i "s/<\/widget>/    <allow-navigation href=\\"*\\" \/>\\n<\/widget>/g" config.xml')
os.system("cordova platform add android")
os.system("cordova plugin add ../cordova-plugin-crosswalk-webview")
os.system('sed -i "s/<\/widget>/    <preference name=\\"Language\\" value=\\"false\\" \/>\\n<\/widget>/g" config.xml')
html_content = "<html>\n" \
               "    <body>\n" \
               "        <script type=\"text/javascript\" src=\"cordova.js\"></script>\n" \
               "        <script>alert(window.navigator.language);</script>\n" \
               "    </body>\n" \
               "</html>"
index_file = open("./www/index.html", "w")
index_file.write(html_content)
index_file.close()
os.system("cordova build android")
os.system("cordova run")
lsstatus = commands.getstatusoutput("ls ./platforms/android/build/outputs/apk/*.apk")
if lsstatus[0] == 0:
    print "Build Package Successfully"
else:
    print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep com.example.language")
if pmstatus[0] == 0:
    print "Package Name Consistent"
else:
    print "Package Name Inconsistent"


