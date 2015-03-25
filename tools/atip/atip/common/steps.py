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
#         Fan, Yugang <yugang.fan@intel.com>

import time
from behave import step
from atip.web import web


@step(u'I wait for {timeout:d} seconds')
def wait_for_timeout(context, timeout):
    time.sleep(timeout)

@step(u'launch "{app_name}"')
def launch_app_by_name(context, app_name):
    web.launch_webapp_by_name(context, app_name)

@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}"')
def launch_app_by_names(context, app_name, apk_pkg_name, apk_activity_name):
    web.launch_webapp_by_name(context, app_name, apk_pkg_name, apk_activity_name)

@step(u'switch to "{app_name}"')
def switch_to_app_name(context, app_name):
    if app_name in context.apps:
        context.app = context.apps[app_name]
        assert True
    else:
        assert False

@step(u'pic "{pic1}" and pic "{pic2}" should be more than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.app.check_pic_same(pic1, pic2, similarity)

@step(u'pic "{pic1}" and pic "{pic2}" should be less than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.app.check_pic_different(pic1, pic2, similarity)
