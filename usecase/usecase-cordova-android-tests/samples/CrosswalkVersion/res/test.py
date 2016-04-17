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
PKG_MODES = ["shared", "embedded"]
PKG_ARCHS = ["x86", "arm", "x86_64", "arm64"]

comm.setUp()
try:
    usage = "Usage: ./test.py -m shared -a x86"
    opts_parser = OptionParser(usage=usage)
    opts_parser.add_option(
        "-m",
        "--mode",
        dest="pkgmode",
        help="specify the apk mode, e.g. shared, embedded")
    opts_parser.add_option(
        "-a",
        "--arch",
        dest="pkgarch",
        help="specify the apk arch, e.g. x86, arm, x86_64, arm64")
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

if not BUILD_PARAMETERS.pkgarch:
    print "Please add the -a parameter for the pkgarch"
    sys.exit(1)
elif BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
    print "Wrong pkg-arch, only support: %s, exit ..." % PKG_ARCHS
    sys.exit(1)

app_name = "CrosswalkVersion"
pkg_name = "com.example.crosswalkVersion1"
current_path_tmp = os.getcwd()
project_path = os.path.join(current_path_tmp, app_name)
comm.create(app_name, pkg_name, current_path_tmp)

main_version = comm.CROSSWALK_VERSION.split('.')[0]

latestVersion = ''
if comm.CROSSWALK_BRANCH == "stable" or comm.CROSSWALK_BRANCH == "beta":
    latestVersion = comm.getLatestCrosswalkVersion(comm.CROSSWALK_BRANCH, main_version)

pkg_mode_tmp = "shared"
apk_name_arch = "-"
pack_arch_tmp = "arm"
if BUILD_PARAMETERS.pkgmode == "embedded":
    pkg_mode_tmp = "core"
    apk_name_arch = "-armv7-"
    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch != "arm":
        apk_name_arch = "-%s-" % BUILD_PARAMETERS.pkgarch
        if BUILD_PARAMETERS.pkgarch == "x86":
            pack_arch_tmp = "x86"
        elif BUILD_PARAMETERS.pkgarch == "x86_64":
            pack_arch_tmp = "x86 --xwalk64bit"
        elif BUILD_PARAMETERS.pkgarch == "arm64":
            pack_arch_tmp = "arm --xwalk64bit"

VERSION_TYPES = []
EXCEPTED_VERSIONS = []
if comm.CROSSWALK_BRANCH == "beta":
    VERSION_TYPES = ["org.xwalk:xwalk_%s_library_beta:%s+" % (pkg_mode_tmp, main_version), \
        "org.xwalk:xwalk_%s_library_beta:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION)]
    EXCEPTED_VERSIONS = [latestVersion, comm.CROSSWALK_VERSION]

elif comm.CROSSWALK_BRANCH == "stable":
    VERSION_TYPES = ["org.xwalk:xwalk_%s_library:%s+" % (pkg_mode_tmp, main_version), \
            "xwalk_%s_library:%s+" % (pkg_mode_tmp, main_version),
            "%s+" % (main_version),
            "%s" % (main_version),
            "org.xwalk:xwalk_%s_library:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION),
            "xwalk_%s_library:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION),
            "%s" % (comm.CROSSWALK_VERSION)]
    EXCEPTED_VERSIONS = [latestVersion, latestVersion, latestVersion, latestVersion, \
            comm.CROSSWALK_VERSION, comm.CROSSWALK_VERSION, comm.CROSSWALK_VERSION]

elif comm.CROSSWALK_BRANCH == "canary":
    VERSION_TYPES = ["org.xwalk:xwalk_%s_library:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION),
            "xwalk_%s_library:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION),
            "%s" % (comm.CROSSWALK_VERSION)]
    EXCEPTED_VERSIONS = [comm.CROSSWALK_VERSION, comm.CROSSWALK_VERSION, comm.CROSSWALK_VERSION]
    comm.installCrosswalk(BUILD_PARAMETERS.pkgmode, BUILD_PARAMETERS.pkgarch)
else:
    print "CROSSWALK_BRANCH in VERSION file is unavailable"
    sys.exit(1)

count = 1
index = 0
for version_tmp in VERSION_TYPES:
    os.system('cp ../index.html www/index.html')
    os.system('sed -i "s/{expectedVersion}/%s/g" www/index.html' % EXCEPTED_VERSIONS[index])
    comm.replaceUserString(
            project_path,
            'www/index.html',
            '{expectedVersion}',
            EXCEPTED_VERSIONS[index])
    print version_tmp
    print EXCEPTED_VERSIONS[index]
    comm.installWebviewPlugin(BUILD_PARAMETERS.pkgmode, version_tmp)
    comm.build(app_name, pack_arch_tmp)

    apk_source = os.path.join(project_path, "platforms", "android", 
            "build", "outputs", "apk", "android%sdebug.apk" % apk_name_arch)
    apk_dest = os.path.join(current_path_tmp, "CrosswalkVersion_%s_%d.apk" % (comm.CROSSWALK_BRANCH, count))
    if not comm.doCopy(apk_source, apk_dest):
        sys.exit(1)

    count = count + 1
    comm.removeWebviewPlugin()

    comm.installWebviewPlugin(BUILD_PARAMETERS.pkgmode)
    os.system('sed -i "s/<preference name=\\"xwalkVersion\\" value=\\".*/<preference name=\\"xwalkVersion\\"' \
            ' value=\\"%s\\" \/>/g" config.xml' % version_tmp)
    comm.build(app_name, pack_arch_tmp)
    apk_dest = os.path.join(current_path_tmp, "CrosswalkVersion_%s_%d.apk" % (comm.CROSSWALK_BRANCH, count))
    if not comm.doCopy(apk_source, apk_dest):
        sys.exit(1)

    count = count + 1
    comm.removeWebviewPlugin()
    index = index + 1

for i in range(count - 1):
    comm.checkApkExist("../CrosswalkVersion_%s_%d.apk" % (comm.CROSSWALK_BRANCH, (i + 1)))


