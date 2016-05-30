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
#         Zhong, Qiu <zhongx.qiu@intel.com>

import os
import glob
import utils
import varshop

DEFAULT_CMD_TIMEOUT = 600


def packIOS(build_json = None, app_src = None, app_dest = None, app_name = None):
    '''
    Build iOS ipa via crosswalk-app, currently crosswalk-pkg for iOS does not
    support yet.
    '''
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")

    package_id = 'org.xwalk.{app_name}'.format(
                            app_name = app_name.replace('-', ''))
    create_cmd = 'crosswalk-app create {package_id} --platform=ios'.format(
                                        package_id = package_id)

    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    if not utils.doCMD(create_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    move_app_cmd =  'mv -fv {app_src}/* ' \
                    '{BUILD_ROOT}/{package_id}/app/'.format(
                        app_src = app_src,
                        BUILD_ROOT = BUILD_ROOT,
                        package_id = package_id)
    if not utils.doCMD(move_app_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    os.chdir(package_id)
    create_cmd = 'crosswalk-app build'
    if not utils.doCMD(create_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    ipa_files = glob.glob(os.path.join(BUILD_ROOT, package_id, "*.ipa"))
    if ipa_files:
        rename_app_name = app_name.replace('-', '_')
        if not utils.doCopy(ipa_files[0],
                            os.path.join(
                                app_dest,
                                "{app_name}.ipa".format(
                                    app_name = rename_app_name)
                            )):
            os.chdir(orig_dir)
            return False
    else:
        LOG.error("Fail to find the ipa file")
        os.chdir(orig_dir)
        return False

    return True
