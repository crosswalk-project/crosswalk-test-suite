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
import json
import re
import colorsys
import Image
import string
import os
import ConfigParser
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    NoAlertPresentException,
    WebDriverException)
from atip.tizen import tizen
from atip.common import common
try:
    from urlparse import urljoin, urlparse
except ImportError:
    from urllib.parse import urljoin, urlparse


class WebAPP(common.APP):

    def __init__(self, app_config=None, app_name=None,
                 apk_pkg_name=None, apk_activity_name=None):
        self.driver = None
        self.app_type = common.APP_TYPE_WEB
        self.app_name = app_name
        self.app_id = ""
        self.cur_path = os.getcwd()
        self.config_file = "data.conf"
        self.device_platform = ""
        self.test_type = ""
        self.read_config()
	self.test_url = app_config["test-url"]
        self.baseline_path = self.test_url + "/../../data/" + self.device_platform
        self.text_value = {}
        self.picture_list = []
        self.color_dict = {
            "rgb(255, 0, 0)": "red",
            "rgb(0, 255, 0)": "green",
            "rgb(0, 0, 255)": "blue",
            "rgb(255, 255, 0)": "yellow",
            "rgb(0, 0, 0)": "black",
            "rgb(0, 128, 0)": "green",
            "rgb(255, 255, 255)": "white",
            "rgba(0, 0, 0, 0)": "white"}
        apk_activity_name = apk_activity_name
        apk_pkg_name = apk_pkg_name
        if "platform" in app_config and "name" in app_config["platform"]:
            if app_config["platform"]["name"].upper().find('TIZEN') >= 0:
                self.app_id = tizen.get_appid_by_name(
                    self.app_name, app_config["platform"], app_config["tizen_user"])
            if app_config["platform"]["name"].upper().find('ANDROID') >= 0:
                if apk_activity_name == apk_pkg_name is None:
                    if "app_launcher" in app_config and app_config[
                            "app_launcher"] == "XWalkLauncher":
                        self.app_name = self.app_name.replace("-", "_")
                        apk_name_update = "".join(
                            [i.capitalize() for i in self.app_name.split("_") if i])
                        apk_activity_name = ".%sActivity" % apk_name_update
                        apk_pkg_name = "org.xwalk.%s" % self.app_name
                    if "app_launcher" in app_config and app_config[
                            "app_launcher"] == "CordovaLauncher":
                        self.app_name = self.app_name.replace("-", "_")
                        apk_activity_name = ".%s" % self.app_name
                        apk_pkg_name = "org.xwalk.%s" % self.app_name
        app_config_str = json.dumps(app_config).replace(
            "TEST_APP_NAME", self.app_name).replace(
            "TEST_APP_ID", self.app_id).replace(
            "TEST_PKG_NAME", apk_pkg_name).replace(
            "TEST_ACTIVITY_NAME", apk_activity_name)
        self.app_config = json.loads(app_config_str)
        if "url-prefix" in app_config:
            self.url_prefix = app_config["url-prefix"]
        else:
            self.url_prefix = ""

    def read_config(self):
        try:
            config = ConfigParser.ConfigParser()
            with open(self.config_file, "r") as cfgfile:
                config.readfp(cfgfile)
            self.device_platform = config.get('info', 'platform')
            self.test_type = config.get('info', 'test_type')
        except Exception as e:
            print "Parser config data.config failed: %s" % e

    def __get_element_by_xpath(self, xpath, display=True):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if display:
                try:
                    if element.is_displayed():
                        return element
                except StaleElementReferenceException:
                    pass
            else:
                return element
            print "Failed to get element"
        except Exception as e:
            print "Failed to get element: %s" % e
        return None

    def __get_element_by_key_attr(self, key, attr, display=True):
        xpath = "//*[@%s='%s']" % (attr, key)
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if display:
                try:
                    if element.is_displayed():
                        return element
                except StaleElementReferenceException:
                    pass
            else:
                return element
            print "Failed to get element"
        except Exception as e:
            print "Failed to get element: %s" % e
        return None

    def __get_element_by_tag(self, key, display=True):
        try:
            element = self.driver.find_element_by_tag(key)
            return element
        except Exception as e:
            print "Failed to get element: %s" % e
            return None

    def __get_element_by_key(self, key, display=True):
        try:
            for i_element in self.driver.find_elements_by_xpath(str(
                    "//*[@id='%(key)s']|"
                    "//*[@name='%(key)s']|"
                    "//*[@value='%(key)s']|"
                    "//*[contains(@class, '%(key)s')]|"
                    "//div[contains(text(), '%(key)s')]|"
                    "//button[contains(text(), '%(key)s')]|"
                    "//input[contains(text(), '%(key)s')]|"
                    "//textarea[contains(text(), '%(key)s')]|"
                    "//a[contains(text(), '%(key)s')]") % {'key': key}):
                if display:
                    try:
                        if i_element.is_displayed():
                            return i_element
                    except StaleElementReferenceException:
                        pass
                else:
                    return i_element
            print "Failed to get element"
        except Exception as e:
            print "Failed to get element: %s" % e
        return None

    def __get_element_by_keys(self, key_p, key_c, display=True):
        try:
            for i_element in self.driver.find_elements_by_xpath(str(
                    "//*[@id='%(key)s']|"
                    "//*[@name='%(key)s']|"
                    "//*[@value='%(key)s']|"
                    "//*[contains(@class, '%(key)s')]|"
                    "//div[contains(text(), '%(key)s')]|"
                    "//button[contains(text(), '%(key)s')]|"
                    "//input[contains(text(), '%(key)s')]|"
                    "//textarea[contains(text(), '%(key)s')]|"
                    "//a[contains(text(), '%(key)s')]") % {'key': key_p}):
                get_element = False
                if display:
                    try:
                        if i_element.is_displayed():
                            get_element = True
                    except StaleElementReferenceException:
                        pass
                else:
                    get_element = True

                if get_element:
                    print "%s ++ %s" % (i_element.get_attribute("id"), i_element.get_attribute("class"))
                    for ii_element in i_element.find_elements_by_xpath(str(
                            "./*[@id='%(key)s']|"
                            "./*[@name='%(key)s']|"
                            "./*[@value='%(key)s']|"
                            "./*[contains(@class, '%(key)s')]|"
                            "./div[contains(text(), '%(key)s')]|"
                            "./button[contains(text(), '%(key)s')]|"
                            "./input[contains(text(), '%(key)s')]|"
                            "./textarea[contains(text(), '%(key)s')]|"
                            "./a[contains(text(), '%(key)s')]") % {'key': key_c}):
                        if display:
                            try:
                                if ii_element.is_displayed():
                                    return ii_element
                            except StaleElementReferenceException:
                                pass
                        else:
                            return ii_element

            print "Failed to get element"
        except Exception as e:
            print "Failed to get element: %s" % e
        return None

    def __check_normal_text(self, text, display=True):
        try:
            for i_element in self.driver.find_elements_by_xpath(str(
                    '//*[@value="{text}"]|'
                    '//*[contains(normalize-space(.),"{text}") '
                    'and not(./*[contains(normalize-space(.),"{text}")])]'
                    .format(text=text))):
                if display:
                    try:
                        if i_element.is_displayed():
                            return i_element
                    except StaleElementReferenceException:
                        pass
                else:
                    return i_element
        except Exception as e:
            print "Failed to get element: %s" % e
        return None

    def check_normal_text_element_not_exist(self, text, key, display=True):
        element = self.__get_element_by_key(key, display)
        if element:
            try:
                e_list = element.find_elements_by_xpath(str(
                    '//*[@value="{text}"]|'
                    '//*[contains(normalize-space(.),"{text}") '
                    'and not(./*[contains(normalize-space(.),"{text}")])]'
                    .format(text=text)))
                for i_element in e_list:
                    if i_element.text == text:
                        return False
                return True
            except Exception as e:
                print "Failed to get element: %s" % e
        return False

    def __check_normal_text_element(self, text, key, display=True):
        element = self.__get_element_by_key(key, display)
        if element:
            try:
                for i_element in element.find_elements_by_xpath(str(
                        '//*[@value="{text}"]|'
                        '//*[contains(normalize-space(.),"{text}") '
                        'and not(./*[contains(normalize-space(.),"{text}")])]'
                        .format(text=text))):
                    if display:
                        try:
                            if i_element.is_displayed():
                                return i_element
                        except StaleElementReferenceException:
                            pass
                    else:
                        return i_element
            except Exception as e:
                print "Failed to get element: %s" % e
        return None

    def compare_two_values(self, first=None, second=None):
        try:
            if eval(self.text_value[first]) < eval(self.text_value[second]):
                return True
            else:
                return False
        except Exception as e:
            print "Failed to compare these two param: %s" % e
        return False

    def compare_two_values_range(self, first=None, second=None, value=None):
        try:
            result = eval(self.text_value[second]) - eval(self.text_value[first])
            if  result >= eval(value) :
                return True
            else:
                return False
        except Exception as e:
            print "Failed to compare these two param with value: %s" % e
        return False

    def save_content(self, p_name=None, key=None):
        try:
            js_script = 'var style=document.getElementById(\"' + \
                key + '\").innerHTML; return style'
            style = self.driver.execute_script(js_script)
            self.text_value[p_name] = style
            return True
        except Exception as e:
            print "Failed to get element: %s" % e
            return False

    def launch_app(self):
        try:
            desired_capabilities = self.app_config["desired-capabilities"]
            self.driver = WebDriver(
                str(self.app_config["driver-url"]), desired_capabilities)
        except Exception as e:
            print "Failed to launch %s: %s" % (self.app_name, e)
            return False
        return True

    def switch_url(self, url, with_prefix=True):
        if with_prefix:
            url = urljoin(self.url_prefix, url)
        try:
            self.driver.get(url)
        except Exception as e:
            print "Failed to visit %s: %s" % (url, e)
            return False
        return True

    def title(self):
        try:
            return self.driver.title
        except Exception as e:
            print "Failed to get title: %s" % e
            return None

    def current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print "Failed to get current url: %s" % e
            return None

    def reload(self):
        self.driver.refresh()
        return True

    def back(self):
        self.driver.back()
        return True

    def forward(self):
        self.driver.forward()
        return True

    def check_normal_text_timeout(self, text=None, display=True, timeout=2):
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.__check_normal_text(text, display):
                return True
            time.sleep(0.2)
        return False

    def check_normal_text_element_timeout(
            self, text=None, key=None, display=True, timeout=2):
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.__check_normal_text_element(text, key, display):
                return True
            time.sleep(0.2)
        return False

    def check_normal_text_element_timeout_with_color(
            self, text=None, key=None, color=None, display=True, timeout=2):
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.__check_normal_text_element(text, key, display):
                if self.check_text_color(key, color):
                    return True
            time.sleep(0.2)
        return False

    def check_normal_element_timeout_with_color(
            self, key=None, color=None, display=True, timeout=2):
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.check_background_color(key, color):
                return True
            time.sleep(0.2)
        return False

    def check_background_color(self, key=None, color=None, display=True):
        try:
            js_script = 'var bg_color=document.getElementById(\"' + \
                key + '\").style.backgroundColor; return bg_color'
            bg_color = self.driver.execute_script(js_script)
            if not bg_color:
                js_script = 'var element=document.getElementById(\"' + key + '\");' \
                    ' if(element.currentStyle) {return element.currentStyle.backgroundColor;} ' \
                    ' else { return  document.defaultView.getComputedStyle(element,null).backgroundColor; } '
                bg_color = self.driver.execute_script(js_script)
            if not bg_color:
                bg_color = "white"
            number = re.match(r'[A-Za-z]+$', bg_color)
            if not number:
                bg_color = self.color_dict[bg_color]
            if bg_color.strip() == color:
                return True
        except Exception as e:
            print "Failed to get element color: %s" % e
        return False

    def check_text_color(self, key=None, color=None, display=True):
        try:
            js_script = 'var text_color=document.getElementById(\"' + \
                key + '\").style.color; return text_color'
            text_color = self.driver.execute_script(js_script)
            if not text_color:
                js_script = 'var element=document.getElementById(\"' + key + '\");' \
                    ' if(element.currentStyle) {return element.currentStyle.color;} ' \
                    ' else { return  document.defaultView.getComputedStyle(element,null).color; } '
                text_color = self.driver.execute_script(js_script)
            if not text_color:
                text_color = "black"
            is_rgb = re.match(r'[A-Za-z]+$', text_color)
            if not is_rgb:
                text_color = self.color_dict[text_color]
            if text_color.strip() == color:
                return True
        except Exception as e:
            print "Failed to get element: %s" % e
        return False

    def check_content_type(self, key=None, display=True):
        try:
            js_script = 'var text=document.getElementById(\"' + \
                key + '\").innerText; return text'
            text = self.driver.execute_script(js_script)
            if text.strip() == '':
                return 'none'
            number = re.match(r'(-?\d+)(\.\d+)?', text)
            if number:
                if "." in text:
                    return "float"
                else:
                    return "int"
            else:
                if text.upper() == "TRUE" or text.upper() == "FALSE":
                    return "boolean"
                else:
                    return "string"
        except Exception as e:
            print "Failed to get element text: %s" % e

    def press_element_by_key(self, key, display=True):
        element = self.__get_element_by_key(key, display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            element.click()
            return True

        return False

    def press_element_by_keys(self, key_p, key_c, display=True):
        element = self.__get_element_by_keys(key_p, key_c, display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            element.click()
            return True

        return False

    def press_element_by_key_attr(self, key, attr, display=True):
        element = self.__get_element_by_key_attr(key, attr, display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            element.click()
            return True

        return False

    def click_element_by_keys(self, key_p, key_c, display=True):
        element = self.__get_element_by_keys(key_p, key_c, display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            ActionChains(self.driver).click(element).perform()
            return True
        return False

    def click_element_by_key(self, key, display=True):
        element = self.__get_element_by_key(key, display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            ActionChains(self.driver).click(element).perform()
            return True
        return False

# * The method click_element_by_key will fail when VKB shelter the button, and js can avoid this issue.
    def click_element_by_id_with_js(self, key, display=True):
        element = self.__get_element_by_key_attr(key, "id", display)
        print "%s == %s" % (element.get_attribute("id"), element.get_attribute("class"))
        if element:
            js_script = 'document.getElementById(\"' + key + '\").click()'
            self.driver.execute_script(js_script)
            return True
        return False

    def click_element_coords(self, x, y, key, display=True):
        element = self.__get_element_by_key(key, display)
        if element:
            ActionChains(self.driver).move_to_element_with_offset(
                element, x, y).click().perform()
            return True
        return False

    def execute_js_code(self, js_code):
        try:
            return self.driver.execute_script(js_code)
        except Exception as e:
            print "Execute js code failed: %s" % e
            return 0

    # Calculate the location params of element
    def calculate_element_location(self, key, width=0, height=0):
        try:
            if width:
                width = string.atoi(width)
            if height:
                height = string.atoi(height)
            js_script = 'var top=document.getElementById(\"' + \
                key + '\").getBoundingClientRect().top;  return top'
            top = self.execute_js_code(js_script)
            js_script = 'var left=document.getElementById(\"' + \
                key + '\").getBoundingClientRect().left; return left'
            left = self.execute_js_code(js_script)
            if not width:
                js_script = 'var width=document.getElementById(\"' + \
                    key + '\").getBoundingClientRect().width; return width'
                width = self.execute_js_code(js_script)
            if not height:
                js_script = 'var height=document.getElementById(\"' + \
                    key + '\").getBoundingClientRect().height; return height'
                height = self.execute_js_code(js_script)
            return (left, top, left + width, top + height)
        except Exception as e:
            print "Get element location failed: %s" % e
            return 0

    def calculate_resolution_ratio(self, pic_name):
        try:
            js_script = 'var width=window.screen.availWidth; return width'
            body_width = self.execute_js_code(js_script)
            js_script = 'var height=window.screen.availHeight; return height'
            body_height = self.execute_js_code(js_script)
            im = Image.open(pic_name)
            w, h = im.size
            ratio_w = w / body_width
            ratio_h = h / body_height
            ration = 0
            if ratio_w > ratio_h:
                ratio = ratio_w
            else:
                ratio = ratio_h
            return w / ratio, h / ratio
        except Exception as e:
            print "Calculate page picture resolution failed: %s" % e
            return 0

    # Save the specified element as a single picture
    def save_div_as_picture(self, key, element_pic, width=0, height=0):
        try:
            page_pic = "page.png"
            self.driver.get_screenshot_as_file(page_pic)
            self.picture_list.append(page_pic)
            ratio = self.calculate_resolution_ratio(page_pic)
            self.convert_pic(page_pic, ratio)
            box = self.calculate_element_location(key, width, height)
            self.crop_pic(page_pic, element_pic, box)
            self.picture_list.append(element_pic)
            return True
        except Exception as e:
            print "Save element picture failed: %s" % e
            return False

    # Remove these temporary pictures
    def remove_picture(self):
        try:
            picture_list = list(set(self.picture_list))
            for element in picture_list:
                os.remove(element)
            self.picture_list = []
            return True
        except Exception as e:
            print "Remove the tmp pictures fail: %s" % e
            return False

    # Check if 2 files content are the same
    def check_md5_file_same(self, file_name):
        try:
            result_path = self.baseline_path + "/" + file_name + ".md5"
            fp_result = open(result_path, "r")
            str_result = fp_result.read()
            fp_result.close()
            baseline_path = self.baseline_path + \
                "/" + file_name + "_baseline.md5"
            fp_baseline = open(baseline_path, "r")
            str_baseline = fp_baseline.read()
            fp_baseline.close()
            index = cmp(str_result, str_baseline)
            if not index:
                return True
            else:
                return False
        except Exception as e:
            print "Check md5 file failed: %s" % e
            return False

    # Save pic as base64 data's md5
    def save_base64_md5_pic(self, pic_name):
        try:
            md5file_path = ""
            if self.test_type == "result":
                md5file_path = self.baseline_path + "/" + pic_name + ".md5"
            elif self.test_type == "baseline":
                md5file_path = self.baseline_path + \
                    "/" + pic_name + "_baseline.md5"
            pic_base64 = self.driver.get_screenshot_as_base64()
            pic_md5 = self.get_string_md5(pic_base64)
            fp = open(md5file_path, "w")
            fp.write(pic_md5)
            fp.close()
            return True
        except Exception as e:
            print "Save pic as base64 failed: %s" % e
            return False

    # Save page as pictures
    def save_page_per_conf(self, pic_name):
        try:
            if not os.path.exists(self.baseline_path):
                os.makedirs(self.baseline_path)
            if self.test_type == "result":
                picname_result = self.baseline_path + "/" + pic_name + ".png"
                self.driver.get_screenshot_as_file(picname_result)
                return True
            elif self.test_type == "baseline":
                picname_baseline = self.baseline_path + \
                    "/" + pic_name + "_baseline.png"
                self.driver.get_screenshot_as_file(picname_baseline)
                return True
            else:
                print "Test_type is wrong. It should be baseline or result. Please check the data.config file."
                return False
        except Exception as e:
            print "Save baseline pictures fail: %s" % e
            return False

    def check_base_result_similarity(self, pic_name, similarity):
        resu_pic = self.baseline_path + "/" + pic_name + ".png"
        base_pic = self.baseline_path + "/" + pic_name + "_baseline.png"
        if not os.path.exists(resu_pic):
            print "The result picture %s is not existed! Case fail" % pic_name
            return False
        if not os.path.exists(base_pic):
            print "The baseline picture %s is not existed! Case fail" % base_pic
            return False
        return self.check_pic_same(base_pic, resu_pic, similarity)

    def fill_element_by_key(self, key, text, display=True):
        element = self.__get_element_by_key(key, display)
        if element:
            element.send_keys(text)
            return True
        return False

    def fill_element_by_key_attr(self, key, attr, text, display=True):
        element = self.__get_element_by_key_attr(key, attr, display)
        if element:
            element.send_keys(text)
            return True
        return False

    def check_checkbox_by_key(self, key, display=True):
        element = self.__get_element_by_xpath(str(
            "//input[@id='%(key)s'][@type='checkbox']|"
            "//input[@name='%(key)s'][@type='checkbox']") % {'key': key}, display)
        if element:
            if not element.is_selected():
                element.click()
            return True
        return False

    def uncheck_checkbox_by_key(self, key, display=True):
        element = self.__get_element_by_xpath(str(
            "//input[@id='%(key)s'][@type='checkbox']|"
            "//input[@name='%(key)s'][@type='checkbox']") % {'key': key}, display)
        if element:
            if element.is_selected():
                element.click()
            return True
        return False

    def get_alert_text(self):
        try:
            alert_element = self.driver.switch_to_alert()
            if alert_element:
                return alert_element.text
        except Exception as e:
            print "Failed to get alert text: %s" % e

        return None

    def check_alert_existing(self):
        try:
            self.driver.switch_to_alert().text
        except NoAlertPresentException:
            return False
        return True

    def accept_alert(self):
        try:
            alert_element = self.driver.switch_to_alert()
            alert_element.accept()
            return True
        except Exception as e:
            print "Failed to accept alert: %s" % e
            return False

    def quit(self):
        if self.driver:
            self.driver.quit()


def launch_webapp_by_name(
        context, app_name, apk_pkg_name=None, apk_activity_name=None):
    if not context.bdd_config:
        assert False

    if app_name in context.webs:
        context.webs[app_name].quit()
    context.webs.update(
        {app_name: WebAPP(context.bdd_config, app_name, apk_pkg_name, apk_activity_name)})
    context.web = context.webs[app_name]
    if not context.web.launch_app():
        assert False
    assert True
