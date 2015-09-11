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

import sys
import os
import time
from behave import step
from atip.web import web
reload(sys)
sys.setdefaultencoding('utf-8')

def get_test_platform(context):
    if context.bdd_config:
        if "platform" in context.bdd_config and "name" in context.bdd_config["platform"]:
            test_platform = context.bdd_config["platform"]["name"]
            if test_platform:
                return test_platform
    return None


@step(u'I wait for {timeout:d} seconds')
def wait_for_timeout(context, timeout):
    time.sleep(timeout)


@step(u'pic "{pic1}" and pic "{pic2}" should be more than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.web.check_pic_same(pic1, pic2, similarity)


@step(u'pic "{pic1}" and pic "{pic2}" should be less than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.web.check_pic_different(pic1, pic2, similarity)


@step(u'launch "{app_name}"')
def launch_app_by_name(context, app_name):
    if get_test_platform(context) in ("android", "deepin"):
        web.launch_webapp_by_name(context, app_name)


@step(u'I turn on screen')
def turn_on_screen(context):
    if get_test_platform(context) == "android":
        context.android.turnOnScreen()


@step(u'I turn off screen')
def turn_off_screen(context):
    if get_test_platform(context) == "android":
        context.android.turnOffScreen()

# The possible orientation is:
# natural or n
# left or l
# right or r
# upsidedown or u (notes: "upsidedown" can not be set until Android 4.3.)
@step(u'I set orientation "{orientation}"')
def set_orientation(context, orientation):
    if get_test_platform(context) == "android":
        context.android.setDeviceOrientation(orientation)


# take screenshot and save to local file "home.png", can not work until Android 4.2.
@step(u'I take screenshot as "{name}"')
def take_screenshot(context, name):
    if get_test_platform(context) == "android":
        context.android.takeScreenshot(name)


# open notification, can not work until Android 4.3.
@step(u'I open notification')
def open_notification(context):
    if get_test_platform(context) == "android":
        assert context.android.openNotification()


# open quick settings, can not work until Android 4.3.
@step(u'I open quick settings')
def open_quick_settings(context):
    if get_test_platform(context) == "android":
        assert context.android.openQuickSettings()


# frequently-used key: home, back, left, right, up, down, center, menu, search, enter,
# delete(or del), recent(recent apps), volume_up, volume_down, volume_mute, camera, power
@step(u'I press "{key}" hardware key')
def press_key(context, key):
    if get_test_platform(context) == "android":
        context.android.pressKeyBy(key)


# open android system wifi
@step(u'I open wifi')
def open_wifi(context):
    if get_test_platform(context) == "android":
        assert context.android.wifiOperate(True)


# close android system wifi
@step(u'I close wifi')
def close_wifi(context):
    if get_test_platform(context) == "android":
        assert context.android.wifiOperate(False)


# open android system airplane mode
@step(u'I open airplane mode')
def open_airplane_mode(context):
    if get_test_platform(context) == "android":
        assert context.android.airplaneModeOperate(True)


# close android system airplane mode
@step(u'I close airplane mode')
def close_airplane_mode(context):
    if get_test_platform(context) == "android":
        assert context.android.airplaneModeOperate(False)


# open android system GPS
@step(u'I open GPS')
def open_gps(context):
    if get_test_platform(context) == "android":
        assert context.android.gpsOperate(True)


# close android system GPS
@step(u'I close GPS')
def close_gps(context):
    if get_test_platform(context) == "android":
        assert context.android.gpsOperate(False)


# execute android adb command
@step(u'I execute command "{command_line}"')
def execute_command(context, command_line):
    (return_code, output) = context.android.doCMD(command_line)
    if return_code == 0:
        assert True
    else:
        assert False


# save execute android adb command result
@step(u'I save command "{command_line}" result "{result_key}"')
def execute_command_with_result(context, command_line, result_key):
    if get_test_platform(context) == "android":
        (return_code, output) = context.android.doCMD(command_line)
        if return_code == 0:
            assert context.android.save2InfoTemp(output, result_key)
        else:
            assert False


# check android adb command result
@step(u'The value "{expected_value}" should be in result "{result_key}"')
def compare_command_result(context, expected_value, result_key):
    if get_test_platform(context) == "android":
        cmd_result = context.android.get2InfoTemp(result_key)
        assert expected_value in "".join(cmd_result)

# install android app by commend line
@step(u'install "{app_path}"')
def install_app_by_cmd(context, app_path):
    app_path = context.bdd_config["test-url"] + "/" + app_path
    if app_path.endswith(".apk") and os.path.exists(app_path):
        device_id = ""
        if "platform" in context.bdd_config and "device" in context.bdd_config["platform"]:
            device_id = context.bdd_config["platform"]["device"]
        assert context.web.install_app_by_cmd(device_id, app_path)

# uninstall android app by commend line
@step(u'uninstall "{package_name}"')
def uninstall_app_by_cmd(context, package_name):
    device_id = ""
    if "platform" in context.bdd_config and "device" in context.bdd_config["platform"]:
        device_id = context.bdd_config["platform"]["device"]
    print "device_id: %s" % device_id
    assert context.web.uninstall_app_by_cmd(device_id, package_name)
