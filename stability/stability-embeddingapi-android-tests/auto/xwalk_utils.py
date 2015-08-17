#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
#         Yunlong, Yang<yunlongx.yang@intel.com>


import commands
import time


def checkStorageFlag(device, timeout):
    storagefile = '/storage/sdcard1/onPageLoadStoppedFlag'
    not_exist_flag = 'No such file or directory'
    exist_flag = ''
    pre_time = time.time()
    while True:
        existstatus = commands.getstatusoutput(
            'adb -s ' +
            device + 
            ' shell cat ' + storagefile)
        elapsed_time = time.time() - pre_time
        if existstatus[0] == 0:
            if exist_flag == existstatus[1]:
                break
            elif elapsed_time >= timeout:
                print 'Timeout to exec CMD!'
                return False                
            elif not_exist_flag in existstatus[1]:
                pass
            else:
                print 'Unknown result status!'
        else:
            print 'Fail to exec CMD!'
            return False
    return True
