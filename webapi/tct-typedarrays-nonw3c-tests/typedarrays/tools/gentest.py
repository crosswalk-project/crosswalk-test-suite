#!/usr/bin/env python

# Copyright (c) 2013 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
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
#         Xie,Yunxiao <yunxiaox.xie@intel.com>

# This script is used to automatically generate test cases.
# Run "python gentest.py".

import os
import yaml
import codecs

def removeTestCase(dir):
    if os.path.isdir(dir):
        paths = os.listdir(dir)
        for path in paths:
            filePath = os.path.join(dir, path)
            if os.path.isfile(filePath) and filePath.endswith('html'):
                try:
                    os.remove(filePath)
                except os.error:
                    autoRun.exception("remove %s error." % filePath)

# load templates and data
datas = yaml.load(open('data.yaml'))
template = open('template.html').read()
template_dataview = open('template-dataview.html').read()

# remove all test cases
parentDir = os.path.split(os.getcwd())[0]
removeTestCase(parentDir)

# generate all test cases
for data in datas:
    file = codecs.open(parentDir + os.path.sep + data['id'] + '.html', 'w', 'utf-8')
    if data['id'][:8] == "DataView":
        file.write(template_dataview % data)
    else:
        file.write(template % data)

