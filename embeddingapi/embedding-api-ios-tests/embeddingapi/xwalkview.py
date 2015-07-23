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
import shutil
import commands
import setup_ios

SCRIPT_PATH = os.path.realpath(__file__)
CONST_PATH = os.path.dirname(SCRIPT_PATH)


def run(dest=None):
    try:
        if dest:
            os.chdir(CONST_PATH + "/ios-extensions-crosswalk/crosswalk-ios/XwalkView/")
            runcmd = "xcodebuild test -project " \
            "XWalkView.xcodeproj/ -scheme XWalkViewTests " \
            "-destination '%s'" % dest
            runstatus = commands.getstatusoutput(runcmd)
            print runstatus[1]
            if runstatus[0] == 0:
                print "Test done"
            else:
                print "Test failed"
        else:
            print "Please input option the destination"
    except Exception as e:
        print Exception, "Run the unit test XWalkView error: ", e
        sys.exit(1)


def init():
    try:
        setup_ios.main()
        try:
            shutil.rmtree(CONST_PATH + "/mobileSpec-crosswalk")
        except:
            os.system(
                "rm -rf " +
                CONST_PATH +
                "/mobileSpec-crosswalk &>/dev/null")
        run(setup_ios.dest)

    except Exception as e:
        print("Get wrong options: %s, exit ..." % e)
        sys.exit(1)

if __name__ == '__main__':
    init()
