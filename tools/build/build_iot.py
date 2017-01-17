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


def newIoTPackageJSON(package_json_path, app_name, index_file = 'index.html'):
    '''
    Generate the package JSON format file which only contains two fields:
    {
        "name": "",
        "main": ""
    }
    '''
    manifest = {}
    try:
        with open(package_json_path, 'w') as fp:
            manifest['name'] = app_name
            manifest['main'] = index_file

            json.dump(manifest, fp, indent = 4)
    except Exception:
        return False

    return True


def newIoTPackageJSONFromManifest(manifest_path, package_json_path):
    '''
    Generate a package.json from manifest.json and only keeps two fields:
    {
        "name": "",
        "main": ""
    }
    '''
    try:
        with open(manifest_path) as fp:
            data = json.load(fp, encoding = 'utf-8')

        package_json = {}
        package_json['name'] = data['name']
        package_json['main'] = data['start_url']
        with open(package_json_path, 'w') as f:
            json.dump(package_json, f, indent = 4)
    except Exception as e:
        return False

    return True


def packIoT(build_json = None, app_src = None, app_dest = None, app_name = None):
    '''
    Build NW.js packages:
    If the package.json not found, new one from the manifest.json.
    Otherwise, skip it.
    '''

    package_json_path = os.path.join(app_src, 'package.json')
    manifest_json_path = os.path.join(app_src, 'manifest.json')

    if not os.path.exists(package_json_path):
        if not newIoTPackageJSON(package_json_path, app_name):
            return False

    if os.path.exists(manifest_json_path):
        os.remove(manifest_json_path)

    if "sub-app" in app_src:
        sub_app_name = os.path.basename(app_src)
        dest_dir = os.path.join(app_dest, 'sub-app', sub_app_name)
    else:
        dest_dir = os.path.join(app_dest, app_name)

    shutil.copytree(app_src, dest_dir)

    return True
