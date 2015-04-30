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
import fileinput
import traceback
from shutil import copytree
from optparse import OptionParser

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)

def cloneCode(tag=None):
    try:
        os.chdir(ConstPath)
        msstatus = commands.getstatusoutput("git clone https://git.coding.net/jondong/mobileSpec-crosswalk.git")
        print "Cloning into mobileSpec..."
        if msstatus[0] == 0:
            print "Clone into mobileSpec done!"
            os.chdir(ConstPath + "/mobileSpec-crosswalk")
            if len(os.listdir(ConstPath + "/mobileSpec-crosswalk/crosswalk-ios/")) == 0:
                codestatus = commands.getstatusoutput("git clone https://github.com/crosswalk-project/crosswalk-ios.git")
                print "Cloning into crosswalk-ios..."
                if codestatus[0] == 0:
                    print "Clone into crosswalk-ios done!"
                else:
                    print "Clone into crosswalk-ios failed!"
            os.chdir('crosswalk-ios')
            tpstatus = commands.getstatusoutput("git submodule update --init --recursive")
            print "Cloning into submodule repos..."
            if tpstatus[0] != 0:
                tar = os.getcwd() + '/.git/config'
                for line in fileinput.input('.git/config',inplace=1):
                    print line.rstrip().replace('git:', 'https:')
                rtpstatus = commands.getstatusoutput("git submodule update --init --recursive")
                icen = os.listdir(os.getcwd() + "/third-party/Icenium/")
                cord = os.listdir(os.getcwd() + "/third-party/cordova-ios/")
                #print rtpstatus
                if rtpstatus[0] != 0:
                    print "Clone submodule repos failed!"
                elif len(icen) > 0 and len(cord) > 0 :
                    print "Clone into submodule repos done!"
                    if tag:
                        tagstatus = commands.getstatusoutput("git checkout %s" % tag)
                        print "Checking out %s" % tag
                        if tagstatus[0] == 0:
                            print "The branch is %s" % tag
                        else:
                            print "Please check if the tag is exist"
                            print tagstatus[1]
                    else:
                        print "The project crosswalk-ios default branch is master"
                    print "Copying the project crosswalk-ios to the same path with mobileSpec-crosswalk"
                    os.chdir(ConstPath)
                    try:
                        shutil.copytree(ConstPath + "/mobileSpec-crosswalk/crosswalk-ios", ConstPath + "/crosswalk-ios")
                    except:
                        print traceback.print_exc()
                    if os.path.exists(ConstPath + "/crosswalk-ios"):
                        print "Copy the project crosswalk-ios done!"
                    else:
                        print "Copy the project crosswalk-ios failed!"
                else:
                    print "Clone submodule repos failed!"
            else:
                print "Clone into submodule repos done!"
    except Exception,e:
        print Exception, "Clone into crosswalk-ios failed!"
        sys.exit(1)

def main():
    try:
        global dest
        usage = 'Usage: ./%prog -d "platform=iOS Simulator,name=iPhone 6,OS=8.3"'
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-t",
            "--tag",
            dest = "tag",
            help = "specify the tag that you want to checkout, default branch is master"
        )
        opts_parser.add_option(
            "-d",
            "--dest",
            dest = "destination",
            help = 'specify the destination that you want to use,' \
                   'the options should be within double quotations,' \
                   'e.g. "platform=iOS Simulator;name=iPhone 6;OS=8.3",' \
                   '"platform=iOS;name=iPad Air"'
        )
        if len(sys.argv) == 1:
            sys.argv.append("-h")

        (PARAMETERS, args) = opts_parser.parse_args()
        cloneCode(PARAMETERS.tag)
        dest = PARAMETERS.destination
        #print 'dest', dest
	
    except Exception,e:
        print("Get wrong options: %s, exit ..." % e)
        sys.exit(1)

if __name__ == '__main__':
    main()
