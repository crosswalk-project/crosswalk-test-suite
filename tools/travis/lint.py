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
#         Xu, Kang <kangx.xu@intel.com>

import sys
import os
import re
import os.path
import commands

Lint_Root = os.path.dirname(os.path.abspath(__file__))
Repo_Root = os.path.dirname(os.path.dirname(Lint_Root))
ERRORS = []

def outputErrors():
    for errortype, errorfile in ERRORS:
        print "%s: %s" % (errortype, errorfile)

def git(cmd):
    output = commands.getstatusoutput(cmd)
    if output[0] != 0:
        raise Exception("Fail to execute cmd:%s" % cmd)
    return output[-1]

def filterUpdatedFiles(gitoutput):
    updatedFiles = []
    for line in gitoutput.split("\n"):
        status = line.split("\t")
        if status[0].strip() != "D":
          updatedFiles.append(status[-1])
    return updatedFiles

def checkTailSpace(filepath):
    with open(filepath) as f:
        for line in f:
            if re.compile("^$").search(line):
                continue

            if re.compile(" $").search(line):
                bname = os.path.basename(filepath)
                error = ["TAILING WHILTESPACE", bname]
                ERRORS.append(error)
                return

def checkFileNameSpace(filepath):
    bname = os.path.basename(filepath)
    if re.compile(" ").search(bname):
        print bname
        error = ["FILENAME WHILTESPACE", bname]
        ERRORS.append(error)
        return

def main():
    lints = [checkTailSpace, checkFileNameSpace]
    gitOutput = git("git diff --name-status HEAD~1")
    for path in filterUpdatedFiles(gitOutput):
        filePath = os.path.join(Repo_Root, path)
        if os.path.isfile(filePath):
            for lint in lints:
                lint(filePath)

if __name__ == "__main__":
    main()
    if len(ERRORS) != 0:
        outputErrors()
        sys.exit(1)
