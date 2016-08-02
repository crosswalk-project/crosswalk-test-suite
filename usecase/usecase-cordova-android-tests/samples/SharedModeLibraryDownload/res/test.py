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
#         Zhu, Yongyong <yongyongx.zhu@intel.com>

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
comm.replaceUserString(
        os.path.join(current_path_tmp, app_name),
        'config.xml',
        '</widget>',
        '    <preference name="LoadUrlTimeoutValue" value="600000" />\n</widget>')

menifest_path = os.path.join(current_path_tmp, app_name, "platforms", "android")
comm.replaceUserString(
        menifest_path,
        'AndroidManifest.xml',
        'android:supportsRtl="true">',
        'android:supportsRtl="true">\n        <meta-data android:name="xwalk_apk_url" android:value="' + BUILD_PARAMETERS.url + '" />')
comm.replaceUserString(
        menifest_path,
        'AndroidManifest.xml',
        '</manifest>',
        '    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />\n</manifest>')
if comm.CROSSWALK_BRANCH == "beta":
    comm.installWebviewPlugin("shared", "org.xwalk:xwalk_shared_library_beta:%s" % comm.CROSSWALK_VERSION)
else:
    comm.installWebviewPlugin("shared", "%s" % comm.CROSSWALK_VERSION)

comm.build(app_name)
comm.run(app_name)
comm.checkBuildResult()
comm.checkRunResult(pkg_name)
