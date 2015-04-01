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

import os
import sys
import json
from atip import environment as atipenv
try:
    from urllib2 import URLError
except ImportError:
    from urllib.error import URLError

webdriver_json_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "webdriver.json")


def clean_context(context):
    for app in context.apps.values():
        try:
            app.quit()
        except URLError:
            pass

    context.app = None
    context.apps = {}


def load_default_config():
    webdriver_json = None
    try:
        platform_name = os.environ['TEST_PLATFORM']
        device = os.environ['DEVICE_ID']
        comm_mode = os.environ['CONNECT_TYPE']
        app_launcher = os.environ['LAUNCHER']
        webdriver_envs = json.loads(os.environ['WEBDRIVER_VARS'])
        webdriver_json = {}
        platform = {}
        platform.update({"name": platform_name})
        platform.update({"comm-mode": comm_mode})
        platform.update({"device": device})
        webdriver_json.update({"platform": platform})
        if platform_name == "TIZEN":
            tizen_user = os.environ['TIZEN_USER']
            webdriver_json.update({"tizen_user": tizen_user})
        webdriver_json.update({"app_launcher": app_launcher})
        webdriver_json.update(
            {"desired-capabilities": webdriver_envs["desired_capabilities"]})
        webdriver_json.update({"driver-url": webdriver_envs["webdriver_url"]})
        if "test_prefix" in webdriver_envs:
            webdriver_json.update(
                {"url-prefix": webdriver_envs["test_prefix"]})
        else:
            webdriver_json.update({"url-prefix": ""})
    except Exception as e:
        print "Failed to get test envs: %s, switch to webdriver.json" % e
        try:
            with open(webdriver_json_path, "rt") as webdriver_json_file:
                webdriver_json_raw = webdriver_json_file.read()
                webdriver_json_file.close()
                webdriver_json = json.loads(webdriver_json_raw)
        except Exception as e:
            print "Failed to read webdriver json: %s" % e
            return None

    return webdriver_json


def before_all(context):
    atipenv.before_all(context)
    context.app = None
    context.apps = {}
    context.web_config = load_default_config()
    if not context.web_config:
        sys.exit(1)


def after_all(context):
    atipenv.after_all(context)
    clean_context(context)


def before_feature(context, feature):
    atipenv.before_feature(context, feature)


def after_feature(context, feature):
    atipenv.after_feature(context, feature)
    clean_context(context)


def before_scenario(context, scenario):
    atipenv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    atipenv.after_scenario(context, scenario)
    clean_context(context)
