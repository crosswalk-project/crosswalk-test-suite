#!/bin/bash
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
#         Fan, Yugang <yugang.fan@intel.com>

if [[ $# == 0 ]]; then
    unset TEST_PLATFORM
    unset DEVICE_ID
    unset CONNECT_TYPE
    unset TIZEN_USER
    unset LAUNCHER
    unset WEBDRIVER_VARS
elif [[ $1 == "xw_android_xwalk" ]]; then
    export TEST_PLATFORM="android"
    export DEVICE_ID=""
    export CONNECT_TYPE="adb"
    export TIZEN_USER=""
    export LAUNCHER="XWalkLauncher"
    export WEBDRIVER_VARS="{\"webdriver_url\":\"http://127.0.0.1:9515\", \"desired_capabilities\": {\"xwalkOptions\": {\"androidPackage\": \"TEST_PKG_NAME\", \"androidActivity\": \"TEST_ACTIVITY_NAME\"}}, \"test_prefix\": \"file:///android_asset/www/\"}"
elif [[ $1 == "xw_android_cordova" ]]; then
    export TEST_PLATFORM="android"
    export DEVICE_ID=""
    export CONNECT_TYPE="adb"
    export TIZEN_USER=""
    export LAUNCHER="CordovaLauncher"
    export WEBDRIVER_VARS="{\"webdriver_url\":\"http://127.0.0.1:9515\", \"desired_capabilities\": {\"xwalkOptions\": {\"androidPackage\": \"TEST_PKG_NAME\", \"androidActivity\": \"TEST_ACTIVITY_NAME\"}}, \"test_prefix\": \"file:///android_asset/www/\"}"
elif [[ $1 == "xw_tizen" ]]; then
    export TEST_PLATFORM="tizen"
    export DEVICE_ID=""
    export CONNECT_TYPE="sdb"
    export TIZEN_USER=""
    export LAUNCHER=""
    export WEBDRIVER_VARS="{\"webdriver_url\":\"http://127.0.0.1:9515\", \"desired_capabilities\": {\"xwalkOptions\": {\"tizenAppId\": \"TEST_APP_ID\", \"tizenDebuggerAddress\": \"http://127.0.0.1:9333\"}}, \"test_prefix\": \"file:///opt/TESTER-HOME-DIR/apps_rw/xwalk/applications/TEST_APP_ID/\"}"
elif [[ $1 == "chrome_ubuntu" ]]; then
    export TEST_PLATFORM="chrome_ubuntu"
    export DEVICE_ID=""
    export CONNECT_TYPE=""
    export TIZEN_USER=""
    export LAUNCHER=""
    export WEBDRIVER_VARS="{\"webdriver_url\":\"http://127.0.0.1:9515\", \"desired_capabilities\": {\"chrome.binary\": \"/usr/bin/chromium-browser\"}, \"test_prefix\": \"file:///\"}"
fi
