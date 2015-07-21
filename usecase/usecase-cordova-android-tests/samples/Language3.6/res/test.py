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
if os.path.exists("Language"):
    os.system("rm -rf Language")
if BUILD_PARAMETERS.pkgmode == "shared":
    os.system("./bin/create Language com.example.language1 Language --xwalk-shared-library")
else:
    os.system("./bin/create Language com.example.language1 Language")
os.chdir("./Language")
html_content = "<html>\n" \
               "    <body>\n" \
               "        <script type=\"text/javascript\" src=\"cordova.js\"></script>\n" \
               "        <script>alert(window.navigator.language);</script>\n" \
               "    </body>\n" \
               "</html>"
index_file = open("./assets/www/index.html", "w")
index_file.write(html_content)
index_file.close()
os.system("./cordova/build")
os.system("./cordova/run")
lsstatus = commands.getstatusoutput("ls ./out/Language*.apk")
if lsstatus[0] == 0:
    print "Build Package Successfully"
else:
    print "Build Package Error"
pmstatus = commands.getstatusoutput("adb shell pm list packages |grep com.example.language1")
if pmstatus[0] == 0:
    print "Package Name Consistent"
else:
    print "Package Name Inconsistent"
