#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
#         Zhong, Qiu <zhongx.qiu@intel.com>

import os
import glob
import json
import shutil
import utils
import varshop


def newIoTManifest(manifest_path, app_name, index_file = 'index.html'):
    '''
    Generate the manifest JSON format file which only contains two fields:
    {
        "name": "",
        "start_url": ""
    }
    '''
    manifest = {}
    try:
        with open(manifest_path, 'w') as fp:
            manifest['name'] = app_name
            manifest['start_url'] = index_file

            json.dump(manifest, fp, indent = 4)
    except Exception:
        return False

    return True


def packIoT(build_json = None, app_src = None, app_dest = None, app_name = None):
    '''
    Build IoT packages, simply compress the necessary files.
    '''
    manifest_path = os.path.join(app_src, 'manifest.json')

    if not os.path.exists(manifest_path):
        if not newIoTManifest(manifest_path, app_name):
            return False

    if "sub-app" in app_src:
        sub_app_name = os.path.basename(app_src)
        dest_dir = os.path.join(app_dest, 'sub-app', sub_app_name)
    else:
        dest_dir = os.path.join(app_dest, app_name)

    shutil.copytree(app_src, dest_dir)

    return True
