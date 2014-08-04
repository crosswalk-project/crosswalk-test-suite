#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
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
#         Hao, Yunfei <yunfeix.hao@intel.com>

import time
import os
print 'Content-Type: text/html\n\n'
while True:
    i = raw_input()
    if i is None:
        break
    if str(i).strip()=='':
        break
    n = 1
    if os.path.isfile('/tmp/csp-report.log'):
        file_object_num = open('/tmp/csp-report.log','r')
        for line in file_object_num:
            if str(line).find("Time:") >= 0:
                n = n+1
        file_object_num.close( )
    file_object = open('/tmp/csp-report.log', 'a')
    file_object.write('\n %d   Time:' %n)
    file_object.write( time.strftime(' %Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    file_object.write('\n')
    file_object.write('     Data:')
    file_object.write(i)
    file_object.write('\n')
    file_object.close( )
    print i
