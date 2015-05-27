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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import os
import sys
import commands
import shutil
import fileinput
import setup_ios

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)

def tryRun(dest=None, uuid=None):
    try:
        if dest:
            build_xwalkview(dest)
        print "Start run Cordova MobileSpec Tests..."
        runApp = BuildPath + "/Release-iphoneos/MobileSpec.app"
        jsPath = ConstPath + "/mobilespec.js"
        print 'debug', os.path.exists(runApp)
        print 'debug', os.path.exists(jsPath)
        cmd = "instruments -w %s -t '/Applications/Xcode.app/Contents/Applications/Instruments.app/Contents/PlugIns/AutomationInstrument.xrplugin/Contents/Resources/Automation.tracetemplate' %s -e UIASCRIPT %s -e UIARESULTSPATH %s" \
              % (uuid, runApp, jsPath, ConstPath)
        print 'debug3', cmd
        runstatus = commands.getoutput(cmd)
            print runstatus
    else:
        print "Please input option the destination"
    except Exception, e:
        print Exception, e
    sys.exit(1)

def build_xwalkview(dest):
    os.chdir(ConstPath)
    global BuildPath, targetPro
    BuildPath = ConstPath + "/build"
    if os.path.exists(BuildPath):
        shutil.rmtree(BuildPath)
    os.mkdir("build")
    targetPro = "mobileSpec-crosswalk/crosswalk-ios"
    buildstatus = commands.getstatusoutput("xcodebuild -project %s/XWalkView/XWalkView.xcodeproj/ SYMROOT=%s -destination '%s'" % \
                  (targetPro, BuildPath, dest))
    if buildstatus[0] == 0 and "BUILD SUCCEEDED" in buildstatus[1]:
        print "Build project XWalkView succeeded!"
        build_cordova(dest)
    else:
        print "Build project XWalkView failed!"
    print buildstatus[1]
    sys.exit(1)

def build_cordova(dest):
    global FramePath
    FramePath = BuildPath + "/Release-iphoneos/**"
    Cordovastatus = commands.getstatusoutput("xcodebuild -project %s/Cordova/Cordova.xcodeproj SYMROOT=%s \
                    -destination '%s' FRAMEWORK_SEARCH_PATHS=%s" % \
                    (targetPro, BuildPath, dest, FramePath))
    if Cordovastatus[0] == 0 and "BUILD SUCCEEDED" in Cordovastatus[1]:
        print "Build project Cordova succeeded!"
        build_mobilespec(dest)
    else:
        print "Build project Cordova failed!"
    print Cordovastatus[1]
    sys.exit(1)

def build_mobilespec(dest):
    specStatus = commands.getstatusoutput("xcodebuild -project %s/../MobileSpec/MobileSpec.xcodeproj SYMROOT=%s \
                 -destination '%s' FRAMEWORK_SEARCH_PATHS=%s" % \
         (targetPro, BuildPath, dest, FramePath))
    if specStatus[0]  == 0 and "BUILD SUCCEEDED" in specStatus[1]:
        print "Build project MobileSpec succeeded!"
    else:
        print "Build project MobileSpec failed!"
    print specStatus[1]
    sys.exit(1)

def init():
    try:
        setup_ios.main()
    tryRun(setup_ios.dest, setup_ios.uuid)
    #tryRun("platform=iOS Simulator,name=iPhone 6,OS=8.3", "FC60C16D-61DE-4DCD-A79D-B8DBAF1776B4")
    except Exception,e:
        print("Get wrong options: %s, exit ..." % e)
    sys.exit(1)

if __name__ == '__main__':
    init()
