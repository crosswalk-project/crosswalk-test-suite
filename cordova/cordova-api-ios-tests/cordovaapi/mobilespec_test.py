#!/usr/bin/env python
#coding=utf-8
#
# Copyright (c) 2015 Intel Corun_polloration.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corun_polloration nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL COrun_pollORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PUrun_pollOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL COrun_pollORATION BE LIABLE FOR ANY DIRECT,
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
import setup_ios
import subprocess
import time

SCRIPT_PATH = os.path.realpath(__file__)
CONST_PATH = os.path.dirname(SCRIPT_PATH)

def try_run(dest=None, uuid=None):
    try:
        if dest:
            build_mobilespec(dest, uuid)
        print "Start run Cordova MobileSpec Tests..."
        js_path = CONST_PATH + "/mobilespec.js"
        cmd = "instruments -w %s -t " \
        "'/Applications/Xcode.app/Contents/Applications/Instruments.app" \
        "/Contents/PlugIns/AutomationInstrument.xrplugin/Contents" \
        "/Resources/Automation.tracetemplate'" \
        " org.crosswalk-project.MobileSpec -e UIASCRIPT %s " \
        "-e UIARESULTSPATH %s" \
         % (uuid, js_path, CONST_PATH)
        run_status = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, \
            stdout=subprocess.PIPE)
        lines = run_status.stdout.readlines()
        for line in lines:
            item = line.strip().lstrip()
            if not (item.startswith('UIAStaticText "*"') or \
                item.startswith('UIAStaticText "•"') or \
                item.startswith('UIAStaticText "×"')):
                print item
            if "452 specs" in item:
                print 'Test Result: ', item
        else:
            print "Please input option the destination"
    except Exception as e:
        print Exception, "Run Cordova MobileSpec failed"
    sys.exit(1)


def build_mobilespec(dest, uuid):
    global build_path
    os.chdir(CONST_PATH)
    dir_name = ''.join(map(lambda xx:(hex(ord(xx))[2:]), os.urandom(8)))
    build_path = CONST_PATH + "/" + dir_name
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    os.mkdir(dir_name)
    tar_pro = "mobileSpec-crosswalk/MobileSpec"
    os.chdir(tar_pro)
    build_cmd = 'xcodebuild -project MobileSpec.xcodeproj -scheme MobileSpec \
    -destination "%s" -configuration Debug build SYMROOT=%s' % \
                (dest, build_path)
    openstatus = commands.getstatusoutput("open MobileSpec.xcodeproj")
    if openstatus[0] == 0:
        time.sleep(25)
        print 'open xcode'
        close_cmd = "osascript -e 'tell app \"Xcode\" to quit'"
        close_xcode = commands.getstatusoutput(close_cmd)
        if close_xcode[0] == 0:
            print 'close xcode'
        else:
            kill_cmd = "kill $(ps aux | grep 'Xcode' |awk '{print $2}') \
            &>/dev/null"
            os.system(kill_cmd)
    else:
        print openstatus[1]
    print 'debug', build_cmd
    build_status = subprocess.Popen(build_cmd, shell=True, \
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output_lines = build_status.stdout.read()
    run_poll = build_status.poll()
    print 'debug', run_poll
    if output_lines.find("MobileSpec.app") != -1 and output_lines.find("BUILD SUCCEEDED") != -1:
        print "Build project MobileSpec succeeded!"
        install_app(uuid)
    else:
        print "Build project MobileSpec failed!"
        print output_lines
        sys.exit(1)

# install the MobileSpec.app to devices
def install_app(uuid):
    run_app = build_path + "/Debug-iphoneos/MobileSpec.app"
    print 'debug', os.path.exists(run_app)
    os.chdir(CONST_PATH)
    inststatus = commands.getstatusoutput("ios-deploy --id %s -b %s" % \
                 (uuid, run_app))
    if "Installed package" in inststatus[1]:
        print "Install the MobileSpec.app to device succeeded!"
    else:
        print "Install the MobileSpec.app to device failed!"
        print inststatus[1]
        sys.exit(1)


def init():
    try:
        setup_ios.main()
        try_run(setup_ios.dest, setup_ios.uuid)
    except Exception as e:
        print("Get wrong options: %s, exit ..." % e)
        sys.exit(1)

if __name__ == '__main__':
    init()
