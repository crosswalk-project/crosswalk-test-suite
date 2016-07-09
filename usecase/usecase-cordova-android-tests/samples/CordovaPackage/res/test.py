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
#         Li, Hao <haox.li@intel.com>

import os
import commands
import sys
import json
sys.path.append(os.getcwd())
sys.path.append(os.path.realpath('..'))
import comm
import xml.dom.minidom
from optparse import OptionParser


PKG_MODES = ["shared", "embedded"]
PKG_ARCH = ["x86", "x86_64", "arm", "arm64"]

comm.setUp()
try:
    usage = "Usage: ./test.py -m [embedded|shared] -a [x86|x86_64|arm|arm64]"
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
        help="specify the apk mode, e.g. shared, embedded")
    global BUILD_PARAMETERS
    (BUILD_PARAMETERS, args) = opts_parser.parse_args()
except Exception as e:
    print "Got wrong options: %s, exit ..." % e
    sys.exit(1)
if not BUILD_PARAMETERS.pkgmode:
    print "Please add the -m parameter for the pkgmode"
    sys.exit(1)
elif BUILD_PARAMETERS.pkgmode and not BUILD_PARAMETERS.pkgmode in PKG_MODES:
    print "Wrong pkg mode, only support: %s, exit ..." % PKG_MODES
    sys.exit(1)
if BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCH:
    print "Wrong pkg arch, only support: %s, exit ..." % PKG_ARCH
    sys.exit(1)

comm.installCrosswalk(BUILD_PARAMETERS.pkgmode, BUILD_PARAMETERS.pkgarch)
app_name = "CordovaPackage"
pkg_name = "com.example.cordovaPackage2"

current_path_tmp = os.getcwd()
project_path = os.path.join(current_path_tmp, app_name)
if os.path.exists(project_path):
    comm.doRemove([project_path])

os.system("cordova create %s %s %s" % (app_name, pkg_name, app_name))
os.chdir(project_path)
os.system("cordova platform add android")


pkg_mode_tmp = "shared"
if BUILD_PARAMETERS.pkgmode == "embedded":
    pkg_mode_tmp = "core"

xwalk_version = "%s" % comm.CROSSWALK_VERSION
if comm.CROSSWALK_BRANCH == "beta":
    xwalk_version = "org.xwalk:xwalk_%s_library_beta:%s" % (pkg_mode_tmp, comm.CROSSWALK_VERSION)


os.system("cordova plugin add %s --variable XWALK_VERSION='%s' --variable XWALK_MODE='%s'" % (comm.plugin_tool, xwalk_version, BUILD_PARAMETERS.pkgmode))

# open config.xml
dom = xml.dom.minidom.parse("config.xml")
root = dom.documentElement
preferences = root.getElementsByTagName('preference')
# check the xwalk version set correctly by "--variable XWALK_VERSION"
# check the xwalk mode set correctly by "--variable XWALK_MODE"
for node in preferences:
    if node.nodeName == "xwalkVersion":
        if node.nodeValue != xwalk_version:
            print "Incorrect xwalk version in config.xml: %s, exit ..." % node.nodeValue
            sys.exit(1)
    if node.nodeName == "xwalkMode":
        if node.nodeValue != BUILD_PARAMETERS.pkgmode:
            print "Incorrect xwalk mode in config.xml: %s, exit ..." % node.nodeValue
            sys.exit(1)


pack_arch_opt = ""
if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgmode == "embedded":
    pack_arch_type = BUILD_PARAMETERS.pkgarch
    if BUILD_PARAMETERS.pkgarch == "x86":
        pack_arch_type = "x86"
    elif BUILD_PARAMETERS.pkgarch == "x86_64":
        pack_arch_type = "x86 --xwalk64bit"
    elif BUILD_PARAMETERS.pkgarch == "arm":
        pack_arch_type = "armv7"
    elif BUILD_PARAMETERS.pkgarch == "arm64":
        pack_arch_type = "armv7 --xwalk64bit"
    pack_arch_opt = "-- --gradleArg=-PcdvBuildArch=%s" % pack_arch_type


os.system("cordova build android %s" % pack_arch_opt)
os.system("cordova run android %s" % pack_arch_opt)

comm.checkApkExist("./platforms/android/build/outputs/apk/*.apk")
comm.checkApkRun(pkg_name)

