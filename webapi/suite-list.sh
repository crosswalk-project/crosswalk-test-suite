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
#         Jiehua.Xiong <jiehuax.xiong@intel.com>

LIST=`find -maxdepth 1 -type d`

APKBLACK="webapi-style-css3-tests
webapi-ambientlight-w3c-tests
webapi-imports-w3c-tests
webapi-htmltemplates-html5-tests
webapi-shadowdom-w3c-tests
webapi-taskscheduler-sysapps-tests
ivi-tests
webapi-dlna-xwalk-tests
tizen-tests
tct-wgtapi
tct-widget
tct-testconfig
tct-getcapabilities
tct-manual-w3c-tests"

XPKBLACK="webapi-contactsmanager-sysapps-tests
webapi-style-css3-tests
webapi-ambientlight-w3c-tests
webapi-imports-w3c-tests
webapi-htmltemplates-html5-tests
webapi-presentation-xwalk-tests
webapi-shadowdom-w3c-tests
webapi-taskscheduler-sysapps-tests
webapi-simd-nonw3c-tests
webapi-dlna-ivi-tests
webapi-locale-ivi-tests
webapi-messageport-ivi-tests
webapi-notification-ivi-tests
webapi-speechapi-ivi-tests
webapi-vehicleinfo-ivi-tests
webapi-nativefileapi-xwalk-tests
webapi-embeddingapi-xwalk-tests
tct-alarm-tizen-tests
tct-appcontrol-tizen-tests
tct-calendar-tizen-tests
tct-callhistory-tizen-tests
tct-contact-tizen-tests
tct-content-tizen-tests
tct-datacontrol-tizen-tests
tct-datasync-tizen-tests
tct-download-tizen-tests
tct-livebox-tizen-tests
tct-messaging
tct-nfc-tizen-tests
tct-package-tizen-tests
tct-privilege-tizen-tests
tct-push-tizen-tests
tct-secureelement-tizen-tests
tct-time-tizen-tests
tct-websetting-tizen-tests
tct-wgtapi
tct-widget
tct-manual-w3c-tests"

WGTBLACK="webapi-
tct-wgtapi
tct-widget
tct-manual-w3c-tests"

for list in $LIST;do
    suite_name=`echo $list |awk -F "/" '{print $NF}'`
    grep \<testcase $list/tests.xml > /dev/null 2>&1
    if [ $? -eq 1 ];then
        LIST=`echo "$LIST" | sed "/$suite_name/d"`
    fi
done

XPKSUITE=$LIST
APKSUITE=$LIST
WGTSUITE=$LIST

for xpkblack in $XPKBLACK;do
    XPKSUITE=`echo "$XPKSUITE" | sed "/$xpkblack/d"`
done

for apkblack in $APKBLACK;do
    APKSUITE=`echo "$APKSUITE" | sed "/$apkblack/d"`
done

for wgtblack in $WGTBLACK;do
    WGTSUITE=`echo "$WGTSUITE" | sed "/$wgtblack/d"`
done
