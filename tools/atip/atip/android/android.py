# Copyright (c) 2015 Intel Corporation.
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
#         Yang, Yunlong <yunlongx.yang@intel.com>

import os
import sys
import json
from atip.common import common
from uiautomator import *
reload(sys)
sys.setdefaultencoding('utf-8')
DEFAULT_PARAMETER_KEYS = ["text", "textContains", "description", "descriptionContains",
                "resourceId", "resourceIdMatches"]
OBJECT_INFO_KEYS = ["contentDescription", "checked", "scrollable", "text", "packageName",
                "selected", "enabled", "className"]

class Android(common.APP):

    def __init__(self, app_config, app_name,
                 apk_pkg_name, apk_activity_name):
        self.app_name = app_name
        if "platform" in app_config and "device" in app_config["platform"]:
            self.device_id = app_config["platform"]["device"]
        else:
            self.device_id = ""
        self.package_name = apk_pkg_name
        self.activity_name = apk_activity_name
        if not self.device_id:
            devices = self.devices()
            if devices:
                if len(devices) == 1:
                    self.device_id = list(devices.keys())[0]
                else:
                    print("more than one device connected.")
                    sys.exit(1)
            else:
                print("no device found.")
                sys.exit(1)
        self.adb = "adb -s %s shell" % self.device_id
        self.d = Device(self.device_id)
        self.AutomatorDeviceObject = self.d(text="PaTaTotOmAtO")
        self.info_temp = {}
        self.process_args = {"func_name": None, "func_args": []}


    def launch_app(self):
        cmd = self.adb + \
                " am start -n " + \
                self.package_name + "/" + \
                self.package_name + "." + \
                self.activity_name
        self.d.screen.on()
        self.d.press.home()
        self.d.orientation = "n"
        try:
            (return_code, output) = self.doCMD(cmd)
            if return_code == 0:
                pass
            else:
                print("\n".join(output))
                return False
        except Exception as e:
            return False
        return self.checkCurrentApp()


    def quit(self):
        check_cmd = self.adb + \
                " ps | grep " + \
                self.package_name
        stop_cmd = self.adb + \
                " am force-stop " + \
                self.package_name
        (return_code, output) = self.doCMD(check_cmd)
        if return_code == 0 and output:
            self.doCMD(stop_cmd)
            if self.doCMD(check_cmd)[1] != []:
                print("Please check your cmd: %s" % stop_cmd)


    def wifiOperate(self, turnon):
        self.doCMD(self.adb + " am force-stop com.android.settings")
        wifi_name_list = [u'Wi\u2011Fi', u'WLAN']
        settings_cmd = self.adb + \
                    " am start -n " + \
                    "com.android.settings/.Settings"
        try:
            (return_code, output) = self.doCMD(settings_cmd)
            if return_code == 0:
                pass
            else:
                print("\n".join(output))
                return False
        except Exception as e:
            return False
        if self.d.info["currentPackageName"] == "com.android.settings":
            object_exists = False
            for wifi_name in wifi_name_list:
                try:
                    wifi = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                            .child_by_text(wifi_name, className="android.widget.LinearLayout") \
                            .child(className="android.widget.Switch")
                    if wifi.exists:
                        object_exists = True
                        break
                except Exception as e:
                    pass
            if object_exists:
                wifi_state = self.getObjectInfo(wifi, "checked")
                if turnon:
                    if wifi_state:
                        pass
                    else:
                        self.clickObject(wifi)
                else:
                    if not wifi_state:
                        pass
                    else:
                        self.clickObject(wifi)
                return True
        return False


    def airplaneModeOperate(self, turnon):
        self.doCMD(self.adb + " am force-stop com.android.settings")
        airplane_name_top = [u'Airplane mode',]
        settings_cmd = self.adb + \
                    " am start -n " + \
                    "com.android.settings/.Settings"
        try:
            (return_code, output) = self.doCMD(settings_cmd)
            if return_code == 0:
                pass
            else:
                print("\n".join(output))
                return False
        except Exception as e:
            return False
        if self.d.info["currentPackageName"] == "com.android.settings":
            object_exists = False
            for airplane_name in airplane_name_top:
                try:
                    airplane = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                            .child_by_text(airplane_name, className="android.widget.LinearLayout") \
                            .child(className="android.widget.Switch")
                    if airplane.exists:
                        object_exists = True
                        break
                except Exception as e:
                    pass
            if object_exists:
                airplane_state = self.getObjectInfo(airplane, "checked")
                if turnon:
                    if airplane_state:
                        pass
                    else:
                        self.clickObject(airplane)
                else:
                    if not airplane_state:
                        pass
                    else:
                        self.clickObject(airplane)
                return True
            return self.airplaneModeMore(turnon)
        return False


    def airplaneModeMore(self, turnon):
        airplane_name_more = [u'Airplane mode',]
        object_exists = False
        try:
            more = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                        .child_by_text(u'More\u2026', className="android.widget.LinearLayout")
            if more.exists:
                object_exists = True
        except Exception as e:
            pass
        if object_exists:
            self.clickObject(more)
            object_exists = False
            for airplane_name in airplane_name_more:
                try:
                    airplane = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                            .child_by_text(airplane_name, className="android.widget.LinearLayout") \
                            .child(className="android.widget.CheckBox")
                    if airplane.exists:
                        object_exists = True
                        break
                except Exception as e:
                    pass
            if object_exists:
                airplane_state = self.getObjectInfo(airplane, "checked")
                if turnon:
                    if airplane_state:
                        pass
                    else:
                        self.clickObject(airplane)
                else:
                    if not airplane_state:
                        pass
                    else:
                        self.clickObject(airplane)
                return True
        return False


    def checkCurrentApp(self):
        currentPackageName = self.d.info["currentPackageName"]
        if currentPackageName == self.package_name:
            return True
        return False


    def registerWatcher(self, watcherName, whenText1, clickText, whenText2=None):
        if watcherName in self.d.watchers:
            self.d.watcher(watcherName).remove()
        if whenText2:
            self.d.watcher(watcherName).when(text=whenText1).when(whenText2) \
                                        .click(text=clickText)
        else:
            self.d.watcher(watcherName).when(text=whenText1) \
                                        .click(text=clickText)


    def removeAllWatchers(self):
        self.d.watchers.remove()


    def resetAllWatchers(self):
        self.d.watchers.reset()


    def runAllWatchers(self):
        self.d.watchers.run()


    def turnOnScreen(self):
        self.d.wakeup()


    def turnOffScreen(self):
        self.d.sleep()


    def pressKeyBy(self, device_key):
        self.d.press(device_key)


    def setDeviceOrientation(self, orientation):
        if orientation == None or orientation == "":
            orientation = self.d.orientation
        self.d.orientation = orientation


    def freezeDeviceRotation(self):
        self.d.freeze_rotation()


    def unFreezeDeviceRotation(self):
        self.d.freeze_rotation(False)


    def takeScreenshot(self, name):
        self.d.screenshot(name)


    def openNotification(self):
        return self.d.open.notification()


    def openQuickSettings(self):
        return self.d.open.quick_settings()


    def waitObjectShow(self, ob, timeout=1000):
        return ob.wait.exists(timeout=timeout)


    def waitObjectGone(self, ob, timeout=1000):
        return ob.wait.gone(timeout=timeout)


    def selcetObjectBy(self, key ,value, class_name):
        if key == "text":
            return self.d(text=value, className=class_name)
        elif key == "textContains":
            return self.d(textContains=value, className=class_name)
        elif key == "description":
            return self.d(description=value, className=class_name)
        elif key == "descriptionContains":
            return self.d(descriptionContains=value, className=class_name)
        elif key == "resourceId":
            return self.d(resourceId=value, className=class_name)
        elif key == "resourceIdMatches":
            return self.d(resourceIdMatches=value, className=class_name)
        else:
            return self.AutomatorDeviceObject


    def selectAnyObjectBy(self, value, class_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, value, class_name)
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectTvObjectBy(self, text_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, text_name, "android.widget.TextView")
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectBtnObjectBy(self, button_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, button_name, "android.widget.Button")
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectEdtObjectBy(self, edittext_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, edittext_name, "android.widget.EditText")
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectImageViewObjectBy(self, imageview_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, imageview_name, "android.widget.ImageView")
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectImageBtnObjectBy(self, imagebtn_name):
        for key in DEFAULT_PARAMETER_KEYS:
            ob = self.selcetObjectBy(key, imagebtn_name, "android.widget.ImageButton")
            if self.waitObjectShow(ob):
                return ob
        return self.AutomatorDeviceObject


    def selectViewObjectBy(self, view_desc):
        for key in ["description", "descriptionContains"]:
            ob = self.selcetObjectBy(key, view_desc, "android.view.View")
            if self.waitObjectShow(ob, 3000):
                return ob
        return self.AutomatorDeviceObject


    def selectWebObjectBy(self, web_desc):
        for key in ["description", "descriptionContains"]:
            ob = self.selcetObjectBy(key, web_desc, "android.webkit.WebView")
            if self.waitObjectShow(ob, 3000):
                return ob
        return self.AutomatorDeviceObject


    def getObjectInfo(self, ob, str_key="text"):
        if ob.exists and str_key in OBJECT_INFO_KEYS:
            return ob.info[str_key]
        return None


    def save2InfoTemp(self, msg, key):
        if msg == None:
            return False
        self.info_temp[key] = msg
        return True


    def get2InfoTemp(self, key):
        if key in self.info_temp.keys():
            return self.info_temp[key]
        return None


    def clickObject(self, ob):
        if ob.exists:
            ob.click()
            return True
        return False


    def setEditText(self, ob, text):
        if ob.exists:
            ob.set_text(text)
            return True
        return False


    def selectRelativeObjectBy(self, ob, direction, **kw):
        if direction == "left":
            return ob.left(**kw)
        elif direction == "right":
            return ob.right(**kw)
        elif direction == "up":
            return ob.up(**kw)
        elif direction == "down":
            return ob.down(**kw)


    def getRelativeObjectBy(self, ob, direction, class_name, value_name=None):
        if ob.exists:
            if value_name == None:
                return self.selectRelativeObjectBy(ob, direction, className=class_name)
            for key in DEFAULT_PARAMETER_KEYS:
                param_kw = {}
                param_kw.update({'className': class_name})
                param_kw.update({key: value_name})
                relative_ob = self.selectRelativeObjectBy(ob, direction, **param_kw)
                if relative_ob and relative_ob.exists:
                    return relative_ob
        return self.AutomatorDeviceObject


    def flingBy(self, orientation, direction):
        if orientation == "horiz" and direction == "forward":
            return self.d(scrollable=True).fling.horiz.forward()
        elif orientation == "horiz" and direction == "backward":
            return self.d(scrollable=True).fling.horiz.backward()
        elif orientation == "vert" and direction == "forward":
            return self.d(scrollable=True).fling.vert.forward()
        elif orientation == "vert" and direction == "backward":
            return self.d(scrollable=True).fling.vert.backward()
        return False


    def flingToEnd(self):
        # fling to end vertically
        return self.d(scrollable=True).fling.toEnd()


    def scrollForward(self, steps=10):
        # scroll forward(default) vertically(default)
        return self.d(scrollable=True).scroll(steps=steps)


    def scrollToEnd(self):
        # scroll to end vertically
        return self.d(scrollable=True).scroll.toEnd()


    def scrollTo(self, text_name):
        # scroll forward vertically until specific ui object appears
        return self.d(scrollable=True).scroll.to(text=text_name)


    def swipeTo(self, ob, direction):
        if ob.exists:
            if direction == "left":
                return ob.swipe.left()
            elif direction == "right":
                return ob.swipe.right()
            elif direction == "up":
                return ob.swipe.up()
            elif direction == "down":
                return ob.swipe.down()
        return False


def launch_app_by_name(
        context, app_name, apk_pkg_name=None, apk_activity_name=None):
    if not context.bdd_config:
        assert False

    if app_name in context.apps:
        context.apps[app_name].quit()
    context.apps.update(
        {app_name: Android(context.bdd_config, app_name, apk_pkg_name, apk_activity_name)})
    context.android = context.apps[app_name]
    if not context.android.launch_app():
        assert False
    assert True
