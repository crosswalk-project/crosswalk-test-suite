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
#         Lin, Wanming <wanming.lin@intel.com>

import os
import sys
import json
import time
from atip.common import common
from uiautomator import *
reload(sys)
sys.setdefaultencoding('utf-8')
DEFAULT_PARAMETER_KEYS = ["text", "textContains", "textMatches", "textStartsWith",
                "description", "descriptionContains", "descriptionMatches", "descriptionStartsWith",
                "resourceId", "resourceIdMatches", "className", "packageName", "index"]
OBJECT_INFO_KEYS = ["contentDescription", "checked", "scrollable", "text", "packageName",
                "selected", "enabled", "className"]
PRODUCTS_NAME = {"nexus7": "razor", "memo8": "CN_K011", "nexus4": "occam", "nexus5": "hammerhead", "zte": "V975", "ecs2-8a": "cloudpad", "xiaomipad2": "latte"}

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
        self.productName = self.d.info["productName"]
        self.info_temp = {}
        self.process_args = {"func_name": None, "func_args": []}
        try:
            # Android Verion: [x.x.x]
            (return_code, output) = self.doCMD(self.adb + " getprop |grep \"\[ro.build.version.release\]\" |awk -F \":\" '{print $NF}'")
            if return_code == 0 and output:
                androidVersion = output[0].strip()
            # Get frist 'x' as int
            self.androidVersion = int(androidVersion[1:2])
        except Exception as e:
            print("Fail to get android version: %s" % e)


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


    def openSettings(self):
        #Open settings via command line does not work on Xiaomi Pad2
        if self.productName == PRODUCTS_NAME["xiaomipad2"]:
            return self.selectAppIconInAllApps("text=Settings")
        else:
            self.doCMD(self.adb + " am force-stop com.android.settings")
            settings_cmd = self.adb + \
                        " am start -n " + \
                        "com.android.settings/.Settings"
            try:
                (return_code, output) = self.doCMD(settings_cmd)
                if return_code == 0:
                    if self.d.info["currentPackageName"] == "com.android.settings":
                        return True
                return False
            except Exception as e:
                return False



    def selectItem(self, text):
        obj = None
        settings = self.selectObjectBy("text=Settings")
        if self.androidVersion >= 5 and settings.exists:
            obj = self.d(className="android.widget.ScrollView", resourceId="com.android.settings:id/dashboard") \
                      .child_by_text(text, className="android.widget.FrameLayout")
        else:
            obj = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                      .child_by_text(text, className="android.widget.LinearLayout")
        return self.clickObject(obj)


    def selectSwitchChild(self, child_name, turnon, default_cls="android.widget.Switch"):
        try:
            switch = self.d(className="android.widget.ListView", resourceId="android:id/list") \
                         .child_by_text(child_name, className='android.widget.LinearLayout') \
                         .child(className=default_cls)
            if switch.exists:
                switch_state = self.getObjectInfo(switch, "checked")
                if (not turnon and switch_state) or (turnon and not switch_state):
                    self.clickObject(switch)
                return True
            return False
        except Exception as e:
            return False


    def selectToggle(self, turnon, default_cls='android.widget.Switch'):
        gps_switch = self.selectObjectBy("className=%s" % default_cls)
        if gps_switch.exists:
            for g in gps_switch:
                state = self.getObjectInfo(g, "checked")
                if (not state and turnon) or (state and not turnon):
                    self.clickObject(g)
                    time.sleep(2)
            return True
        return False


    def selectQuickSetting(self, child_name, turnon):
        self.openQuickSettings()
        label = self.selectObjectBy("text=%s"%child_name)
        if label.exists:
            icon = self.selectRelativeObjectBy(label, "up", "className=android.widget.CheckBox")
            if icon.exists:
                box_state = self.getObjectInfo(icon, "checked")
                if (not turnon and box_state) or (turnon and not box_state):
                    self.clickObject(icon)
                self.pressKeyBy("back")
                return True
        return False


    def backToActiveApp(self):
        # Back key cann't return to active app in Xiaomi Pad2, click the first app in Task Manager instead
        if self.productName == PRODUCTS_NAME["xiaomipad2"]:
            self.pressKeyBy("recent")
            self.d.click(self.d.info["displaySizeDpX"], self.d.info["displaySizeDpY"])
        else:
            while True:
                settings = self.selectObjectBy("text=Settings")
                if not settings.exists:
                    self.pressKeyBy("back")
                else:
                    break
            self.pressKeyBy("back")


    def wifiOperate(self, turnon):
        if self.openSettings():
            rtn = False
            if self.productName == PRODUCTS_NAME["nexus7"] \
                or self.productName == PRODUCTS_NAME["nexus5"] \
                or self.productName == PRODUCTS_NAME["nexus4"]:
                if self.androidVersion >= 5:
                    if self.selectItem(u'Wi\u2011Fi'):
                        rtn = self.selectToggle(turnon)
                else:
                    rtn = self.selectSwitchChild(u'Wi\u2011Fi', turnon)
            elif self.productName == PRODUCTS_NAME["xiaomipad2"]:
                self.d(text="WLAN").click()
                rtn = self.selectToggle(turnon, "android.widget.CheckBox")
            elif self.productName == PRODUCTS_NAME["memo8"]:
                if self.selectItem(u'WLAN'):
                    rtn = self.selectToggle(turnon)
            elif self.productName == PRODUCTS_NAME["zte"]:
                rtn = self.selectSwitchChild(u'WLAN', turnon)
            elif self.productName == PRODUCTS_NAME["ecs2-8a"]:
                if self.selectItem(u'Wi\u2011Fi'):
                    rtn = self.selectToggle(turnon)
            self.backToActiveApp()
            return rtn
        return False


    def airplaneModeOperate(self, turnon):
        if self.openSettings():
            rtn = False
            if self.productName == PRODUCTS_NAME["nexus7"] \
                or self.productName == PRODUCTS_NAME["nexus4"] \
                or self.productName == PRODUCTS_NAME["nexus5"] \
                or self.productName == PRODUCTS_NAME["memo8"]:
                more = None
                if self.androidVersion >= 5:
                    more = self.selectItem(u'More')
                else:
                    more = self.selectItem(u'More\u2026')
                if more:
                    if self.androidVersion >= 5:
                        rtn = self.selectSwitchChild(u'Airplane mode', turnon)
                    else:
                        rtn = self.selectSwitchChild(u'Airplane mode', turnon, "android.widget.CheckBox")
            elif self.productName == PRODUCTS_NAME["xiaomipad2"]:
                self.d(text="More").click()
                rtn = self.selectToggle(turnon, "android.widget.CheckBox")
            elif self.productName == PRODUCTS_NAME["zte"]:
                rtn = self.selectSwitchChild(u'Airplane mode', turnon)
            elif self.productName == PRODUCTS_NAME["ecs2-8a"]:
                if self.selectItem(u'More'):
                    rtn = self.selectToggle(turnon)
            self.backToActiveApp()
            return rtn
        return False


    def gpsOperate(self, turnon):
        if self.openSettings():
            rtn = False
            if self.productName == PRODUCTS_NAME["nexus7"]:
                rtn = self.modifyGPSSwitch("Location access", turnon)
            elif self.productName == PRODUCTS_NAME["xiaomipad2"]:
                self.d(text="Additional settings").click()
                self.d(text="Privacy").click()
                self.swipeBy("up")
                self.d(text="Location").click()
                rtn = self.modifyGPSSwitch("Location access", turnon)
            elif self.productName == PRODUCTS_NAME["nexus5"] \
                or self.productName == PRODUCTS_NAME["nexus4"] \
                or self.productName == PRODUCTS_NAME["memo8"] \
                or self.productName == PRODUCTS_NAME["ecs2-8a"]:
                rtn = self.modifyGPSSwitch("Location", turnon)
            elif self.productName == PRODUCTS_NAME["zte"]:
                self.d(scrollable=True).scroll(steps=10)
                rtn = self.modifyGPSSwitch("Location services", turnon)
            self.backToActiveApp()
            return rtn
        return False


    def modifyGPSSwitch(self, child_name, turnon):
        if self.productName == PRODUCTS_NAME["xiaomipad2"]:
            return self.selectToggle(turnon, "android.widget.CheckBox")
        elif self.selectItem(child_name):
            if self.productName == PRODUCTS_NAME["zte"]:
                return self.selectToggle(turnon, "android.widget.CheckBox")
            else:
                self.registerWatcher("gps1", u"Use Google's location service?", "Agree")
                self.registerWatcher("gps2", u"Location consent", "Agree")
                self.registerWatcher("gps3", u"Improve location accuracy?", "Agree")
                self.selectToggle(turnon)
                self.runAllWatchers()
                return True
        return False


    def switchLanguage(self, language):
        if self.openSettings():
            if self.selectItem(u'Language \u0026 input'):
                if self.selectItem('Language'):
                    rtn = self.selectItem(language)
                    self.backToActiveApp()
                    return rtn
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


    def pressKeyBy(self, device_key, times=1):
        for x in range(times):
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


    def waitObjectShow(self, ob, timeout=1):
        return ob.wait.exists(timeout=timeout*1000)


    def waitObjectGone(self, ob, timeout=1):
        return ob.wait.gone(timeout=timeout*1000)


    def getObjectInfo(self, ob, str_key="text"):
        if ob and ob.exists and str_key in OBJECT_INFO_KEYS:
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


    def selectObjectBy(self, params_str, timeout=1):
        params_kw = self.paramToDict(params_str)
        if params_kw:
            ob = self.d(**params_kw)
            if self.waitObjectShow(ob, timeout):
                return ob
        return self.AutomatorDeviceObject


    def paramToDict(self, params_str):
        return_dict = {}
        params = params_str.strip()
        params_list = params.split("^^^")
        for one in params_list:
            two_params = one.strip().split("=")
            if len(two_params) == 2:
                key = two_params[0]
                value = two_params[1]
                if key not in DEFAULT_PARAMETER_KEYS:
                    return None
                return_dict.update({key: value})
            else:
                return None
        return return_dict


    def selectRelativeObjectBy(self, ob, direction, params_str, timeout=1):
        params_kw = self.paramToDict(params_str)
        if ob.exists and params_kw:
            pre_time = time.time()
            while True:
                if direction == "left":
                    relative_ob = ob.left(**params_kw)
                elif direction == "right":
                    relative_ob = ob.right(**params_kw)
                elif direction == "up":
                    relative_ob = ob.up(**params_kw)
                elif direction == "down":
                    relative_ob = ob.down(**params_kw)
                if relative_ob:
                    return relative_ob
                elapsed_time = time.time() - pre_time
                if elapsed_time >= timeout:
                    return self.AutomatorDeviceObject
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


    def flingToBeginning(self):
        # fling to beginning vertically
        return self.d(scrollable=True).fling.vert.toBeginning()


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


    #use coordinates to swipe the page
    def swipeBy(self, direction, steps=10):
        displaySizeDpX = self.d.info["displaySizeDpX"]
        displaySizeDpY = self.d.info["displaySizeDpY"]
        if direction == "left":
            return self.d.swipe(displaySizeDpX, displaySizeDpY, 0, displaySizeDpY, steps=steps)
        elif direction == "right":
            return self.d.swipe(displaySizeDpX, displaySizeDpY, 2*displaySizeDpX, displaySizeDpY, steps=steps)
        elif direction == "up":
            return self.d.swipe(displaySizeDpX, displaySizeDpY, displaySizeDpX, 0, steps=steps)
        elif direction == "down":
            return self.d.swipe(displaySizeDpX, displaySizeDpY, displaySizeDpX, 2*displaySizeDpY, steps=steps)
        else:
            return False


    def closeAppFromTaskManager(self, app_name):
        params_kw = "description=" + app_name
        direction = "left"
        # swiping up to close app is only for Xiaomi Pad2
        # app name is shown as text attribute on task manager from Xiaomi Pad2
        if self.productName == PRODUCTS_NAME["xiaomipad2"]:
            params_kw = "text=" + app_name
            direction = "up"
        ob = self.selectObjectBy(params_kw)
        assert ob.exists
        #swipeTo does not work well on Xiaomi Pad2
        if self.productName == PRODUCTS_NAME["xiaomipad2"]:
            text_bounds = self.d(text=app_name).info["visibleBounds"]
            self.d.swipe(text_bounds["left"], text_bounds["top"], text_bounds["left"], 0)
        else:
            assert self.swipeTo(ob, direction)


    def selectAppIconInAllApps(self, params_str):
        max_fling_num = 10
        self.d.orientation = "n"
        self.d.press.home()
        # no Apps button on Xiaomi Pad2
        if self.productName != PRODUCTS_NAME["xiaomipad2"]:
            all_apps = self.selectObjectBy("description=Apps")
            if all_apps.exists:
                self.clickObject(all_apps)
                if self.productName != PRODUCTS_NAME["memo8"]:
                    self.d(scrollable=True).fling.horiz.toBeginning()
        for i in range(max_fling_num):
            app = self.selectObjectBy(params_str)
            if app.exists:
                self.clickObject(app)
                return True
            #self.flingBy("horiz", "forward")
            self.swipeBy("left")
        return False


    def getDumpedXml(self):
        return self.d.dump()



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
