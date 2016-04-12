#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Li, Hao <haox.li@intel.com>

import os
import commands
import sys
import shutil
import time
import glob
import json
from optparse import OptionParser, make_option

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_TMP = "/tmp"

def buildHelloMap(key):
    if not os.path.exists(BUILD_TMP):
        os.mkdir(BUILD_TMP)

    os.chdir(BUILD_TMP)
    build_src = BUILD_TMP +"/HelloMap"
    if os.path.exists(build_src):
        shutil.rmtree(build_src)

    os.system('cordova create HelloMap com.example.hellomap HelloMap')
    os.chdir(build_src)
    os.system('cordova platform add android')

    pkg_mode = ""
    if MODE is not None:
        pkg_mode = "--variable XWALK_MODE=\"%s\"" % MODE

    xwalk_version = ""
    if CROSSWALK_VERSION is not None and CROSSWALK_BRANCH is not None:
        if "beta" in CROSSWALK_BRANCH:
            xwalk_version = "--variable XWALK_VERSION=\"org.xwalk:xwalk_core_library_beta:%s\"" % CROSSWALK_VERSION
        else:
            xwalk_version = "--variable XWALK_VERSION=\"org.xwalk:xwalk_core_library:%s\"" % CROSSWALK_VERSION
    os.system('cordova plugin add %s/../../../tools/cordova-plugin-crosswalk-webview %s %s' % (SCRIPT_DIR, pkg_mode, xwalk_version))
    os.system('cordova plugin add cordova-plugin-googlemaps --variable API_KEY_FOR_ANDROID="%s"' % key)
    shutil.copyfile(SCRIPT_DIR + '/index.html', build_src  + '/www/index.html')
    # Update android:theme="@android:style/Theme.Black.NoTitleBar" to android:theme="@android:style/Theme.Translucent.NoTitleBar" in AndroidManifest.xml
    os.system('sed -i "s/%s/%s/g" %s' % ("@android:style\/Theme.Black.NoTitleBar", "@android:style\/Theme.Translucent.NoTitleBar", build_src + "/platforms/android/AndroidManifest.xml"))
    # Set zOrderOnTop in config.xml
    lines = open(build_src + '/config.xml', 'r').readlines()
    lines.insert(-1, '    <preference name="xwalkZOrderOnTop" value="true" />\n')
    f = open(build_src + '/config.xml', 'w')
    f.writelines(lines)
    f.close()
    # Workaround for zOrderOnTop
    googlemapjava = build_src + "/platforms/android/src/plugin/google/maps/GoogleMaps.java"
    if os.path.exists(googlemapjava):
        file = open(googlemapjava, 'r')
        lines = open(googlemapjava, 'r').readlines()
        # Add new code postion flag
        import_pos = 0
        showdialog_pos = 0
        resizemap_pos = len(lines)
        insert1_pos = 0
        insert2_pos = 0
        for (num, value) in enumerate(file):
            if value.find("import com.google.android.gms.maps.model.VisibleRegion;") != -1:
                import_pos = num
            elif value.find("private void showDialog") != -1:
                showdialog_pos = num
            elif value.find("private void resizeMap") != -1:
                resizemap_pos = num
            # Workaroundorkaround code should be added to the behind of GoogleMaps.this.onMapEvent("map_close") in showDialog()
            elif value.find("GoogleMaps.this.onMapEvent(\"map_close\");") != -1 and num > showdialog_pos and num < resizemap_pos:
                insert1_pos = num
            # Workaround code should be added to the behind of callbackContext.success(); in showDialog()
            elif value.find("callbackContext.success();") != -1 and num > showdialog_pos and num < resizemap_pos:
                insert2_pos = num
        # Add workaround code by desc
        lines.insert(insert2_pos + 1, "\n    XWalkCordovaView view = (XWalkCordovaView) webView.getView();\n")
        lines.insert(insert2_pos + 2, "    view.setZOrderOnTop(false);\n")
        lines.insert(insert1_pos + 1, "\n        XWalkCordovaView view = (XWalkCordovaView) webView.getView();\n")
        lines.insert(insert1_pos + 2, "        view.setZOrderOnTop(true);\n")
        lines.insert(import_pos + 1, "import org.crosswalk.engine.XWalkCordovaView;\n")
        file = open(googlemapjava, 'w')
        file.writelines(lines)
        file.close()

    pack_arch = ""
    if ARCH == "x86_64":
        pack_arch = "x86 --xwalk64bit"
    elif ARCH == "arm64":
        pack_arch = "arm --xwalk64bit"
    else:
        pack_arch = ARCH

    os.system('cordova build android -- --gradleArg=-PcdvBuildArch=%s' % pack_arch)
    time.sleep(5)
    files = glob.glob(os.path.join(build_src + "/platforms/android/build/outputs/apk", "*-debug.apk"))
    if len(files) == 0:
        print("No apk build in %s/platforms/android/build/outputs/apk" % build_src)
        return
    for apk in files:
        shutil.copy2(apk, SCRIPT_DIR)

def main():
    try:
        usage = "Usage: ./google-maps-plugin.py -k <key>"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-k",
            "--key",
            dest="key",
            help="Google Maps API key")
        global BUILD_PARAMETERS
        (BUILD_PARAMETERS, args) = opts_parser.parse_args()

        if not BUILD_PARAMETERS.key:
            print("Google Maps API key is missing.")
            sys.exit(1)

        global ARCH, MODE, CROSSWALK_VERSION, CROSSWALK_BRANCH
        f_arch = open(SCRIPT_DIR + "/../../../arch.txt", 'r')
        arch_tmp = f_arch.read()
        ARCH = arch_tmp.strip("\n\t").strip()
        f_mode = open(SCRIPT_DIR + "/../../../mode.txt", 'r')
        mode_tmp = f_mode.read()
        MODE = mode_tmp.strip("\n\t").strip()
        with open(SCRIPT_DIR + "/../../../VERSION") as version_file:
            version_str = version_file.read()
            version_file.close()
            version_conf = json.loads(version_str)
            CROSSWALK_VERSION = version_conf.get("main-version").strip()
            CROSSWALK_BRANCH = version_conf.get("crosswalk-branch").strip()

        buildHelloMap(BUILD_PARAMETERS.key)

    except Exception as e:
        print "Got wrong options: %s, exit ..." % e
        sys.exit(1)

if __name__ == '__main__':
    main()
