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

from behave import step
import time
import datetime
try:
    from urlparse import urljoin, urlparse
except ImportError:
    from urllib.parse import urljoin, urlparse


def get_page_url(context, text):
    url = ''
    test_prefix = ''
    try:
        test_platform = context.app.app_config["platform"]["name"].upper()
        url_components = urlparse(context.app.current_url())
        if test_platform == 'TIZEN':
            test_prefix = '%s://%s//' % (url_components.scheme,
                                         url_components.netloc)
        elif test_platform == 'ANDROID':
            if url_components.scheme == 'http':
                test_prefix = '%s://%s/' % (url_components.scheme,
                                            url_components.netloc)
    except Exception as e:
        print "Failed to get page url: %s" % e
        return None
    try:
        nPos = text[0]
        while nPos == '/':
            text = text[1:]
            nPos = text[0]
    except Exception as e:
        print "Test page URL error: %s" % e
        return None
    url = "%s%s" % (test_prefix, text)
    return url


@step(u'I go to "{url}"')
def i_visit_url(context, url):
    url = get_page_url(context, url)
    assert context.app.switch_url(url, True)


@step(u'I reload')
def reload(context):
    assert context.app.reload()


@step(u'I go back')
def go_back(context):
    assert context.app.back()


@step(u'I go forward')
def go_forward(context):
    assert context.app.forward()


@step(u'The current URL should be "{text}"')
def url_should_be_text(context, text):
    url = urljoin(context.app.url_prefix, text)
    assert context.app.current_url().upper() == url.upper()


@step(u'I should see title "{text}"')
def should_see_title_text(context, text):
    assert context.app.title() == text


@step(u'I should see "{text}"')
def should_see_text(context, text):
    assert context.app.check_normal_text_timeout(text), u'Text was not found'


@step(u'I should not see "{text}"')
def should_not_see_text(context, text):
    assert not context.app.check_normal_text_timeout(text), u'Text was found'


@step(u'I should see "{text}" in {timeout:d} seconds')
def should_see_text_timeout(context, text, timeout):
    assert context.app.check_normal_text_timeout(
        text, timeout=timeout), u'Text not found'


@step(u'I should not see "{text}" in {timeout:d} seconds')
def should_not_see_text_timeout(context, text, timeout):
    assert not context.app.check_normal_text_timeout(
        text, timeout=timeout), u'Text was found'


@step(u'I should see "{text}" in "{key}" area')
def should_see_text_element(context, text, key):
    assert context.app.check_normal_text_element_timeout(
        text, key), u'Text was not found'


@step(u'I press "{key}"')
def i_press(context, key):
    assert context.app.press_element_by_key(key)


@step(u'press "{key_c}" in "{key_p}"')
def i_press(context, key_p, key_c):
    assert context.app.press_element_by_keys(key_p, key_c)


@step(u'I click "{key}"')
def i_click(context, key):
    assert context.app.click_element_by_key(key)


@step(u'click "{key_c}" in "{key_p}"')
def i_click_keys(context, key_p, key_c):
    assert context.app.click_element_by_keys(key_p, key_c)


@step(u'I click coords {x:d} and {y:d} of "{key}"')
def i_click_coords(context, x, y, key):
    assert context.app.click_element_coords(x, y, key)


@step(u'I fill in "{key}" with "{text}"')
def fill_with_text(context, key, text):
    assert context.app.fill_element_by_key(key, text)


@step(u'I click the link "{text}"')
def click_element_by_link(context, text):
    element = context.app.driver.find_element_by_link_text(text)
    hyperl = element.get_attribute('href')
    if element:
        element.click()
        return True
    return False


@step(u'I check "{key}"')
def check_checkbox(context, key):
    assert context.app.check_checkbox_by_key(key)


@step(u'I uncheck "{key}"')
def uncheck_checkbox(context, key):
    assert context.app.uncheck_checkbox_by_key(key)


@step(u'I should see an alert')
def should_see_alert(context):
    assert context.app.check_alert_existing()


@step(u'I should not see an alert')
def should_not_see_alert(context):
    assert not context.app.check_alert_existing()


@step(u'I accept the alert')
def i_accept_alert(context):
    assert context.app.accept_alert()


@step(u'I should see an alert with text "{text}"')
def should_see_alert_text(context, text):
    assert context.app.get_alert_text() == text, u'Text was not found'


@step(u'I wait {n:d} seconds')
def wait_senconds(context,n):
   time.sleep(n)


@step(u'I go to frame "{key}"')
def i_visit_frame(context, key):
    context.app.driver.switch_to_frame(key)
    assert True


@step(u'I go out of frame')
def i_jump_frame(context):
    context.app.driver.switch_to_default_content()
    assert True


@step(u'I should see nothing in "{attr}" attr of "{key}" area')
def check_text_by_key(context, attr, key):
    elements = context.app.driver.find_elements_by_id(key)
    if len(elements) == 1 and elements[0].get_attribute(attr) == "":
        assert True
    else:
        assert False


@step(u'I should see "{text}" with "{color}" color in "{key}" area')
def should_see_text_element_with_color(context, text, key, color):
    assert context.app.check_normal_text_element_timeout_with_color(
        text, key, color), u'The text or color is wrong'


@step(u'I should see "{key}" area in "{color}" color')
def should_see_text_element_with_color(context, key, color):
    assert context.app.check_normal_element_timeout_with_color(
        key, color), u'The color is wrong'


@step(u'I verify value in "{key}" is "{expecttype}" type')
def check_type_by_key(context, key, expecttype):
    typename = context.app.check_content_type(key, display=True)
    if typename == expecttype:
        assert True
    else:
        assert False


@step(u'I save div "{key}" as "{pic_name}" with width "{width}" and height "{height}"')
def save_div(context, key, pic_name, width, height):
    assert context.app.save_div_as_picture(key, pic_name, width, height)


@step(u'I save div "{key}" as "{pic_name}"')
def save_div(context, key, pic_name):
    assert context.app.save_div_as_picture(key, pic_name, width=0, height=0)


@step(u'I remove all the pictures')
def remove_pic(context):
    assert context.app.remove_picture()


@step(u'I save the page to "{pic_name}"')
def save_page_per_conf(context, pic_name):
    assert context.app.save_page_per_conf(pic_name)

@step(u'I save the screenshot md5 as "{pic_name}"')
def save_page_as_base64(context, pic_name):
    assert context.app.save_base64_md5_pic(pic_name)

@step(u'file "{file_name}" of baseline and result should be the same')
def check_md5_file(context, file_name):
    assert context.app.check_md5_file_same(file_name)


@step(u'pic "{pic_name}" of baseline and result should be "{similarity}" similar if have results')
def check_base_result_similarity(context, pic_name, similarity):
    assert context.app.check_base_result_similarity(pic_name, similarity)


@step(u'I save "{p_name}" from "{key}" area')
def check_type_by_key(context, p_name, key):
    assert context.app.save_content(p_name, key)


@step(u'I click element with id "{key}" by js')
def click_button_by_js(context, key):
    assert context.app.click_element_by_id_with_js(key)


@step(u'I fill in element "{key}" by "{attr}" with "{text}"')
def fill_element_by_attr_with_text(context, key, attr, text):
    assert context.app.fill_element_by_key_attr(key, attr, text)


@step(u'"{second}" should be greater than "{first}"')
def check_type_by_key(context, first, second):
    assert context.app.compare_two_values(first, second), u'The second value is less than the first one'


@step(u'I should not see "{text}" in "{key}" area')
def should_see_text_element(context, text, key):
    assert context.app.check_normal_text_element_not_exist(
        text, key, display=True), u'Text exists!'
