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
        test_platform = context.web.app_config["platform"]["name"].upper()
        url_components = urlparse(context.web.current_url())
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
    assert context.web.switch_url(url, True)


@step(u'I reload')
def reload(context):
    assert context.web.reload()


@step(u'I go back')
def go_back(context):
    assert context.web.back()


@step(u'I go forward')
def go_forward(context):
    assert context.web.forward()


@step(u'The current URL should be "{text}"')
def url_should_be_text(context, text):
    url = urljoin(context.web.url_prefix, text)
    assert context.web.current_url().upper() == url.upper()


@step(u'I should see title "{text}"')
def should_see_title_text(context, text):
    assert context.web.title() == text


@step(u'I should see "{text}"')
def should_see_text(context, text):
    assert context.web.check_normal_text_timeout(text), u'Text was not found'


@step(u'I should not see "{text}"')
def should_not_see_text(context, text):
    assert not context.web.check_normal_text_timeout(text), u'Text was found'


@step(u'I should see "{text}" in {timeout:d} seconds')
def should_see_text_timeout(context, text, timeout):
    assert context.web.check_normal_text_timeout(
        text, timeout=timeout), u'Text not found'


@step(u'I should not see "{text}" in {timeout:d} seconds')
def should_not_see_text_timeout(context, text, timeout):
    assert not context.web.check_normal_text_timeout(
        text, timeout=timeout), u'Text was found'


@step(u'I should see "{text}" in "{key}" area')
def should_see_text_element(context, text, key):
    assert context.web.check_normal_text_element_timeout(
        text, key), u'Text was not found'


@step(u'I should not see "{text}" in "{key}" area')
def should_not_see_text_element(context, text, key):
    assert context.web.check_normal_text_element_not_exist(
        text, key, display=True), u'Text was found!'


@step(u'I should see between "{num_a}" and "{num_b}" in "{key}" area')
def should_see_between_text_element(context, num_a, num_b, key):
    assert context.app.check_normal_text_element_isvalidate(
        num_a, num_b, key), u'Text was not validate'

@step(u'I should see num in "{key}" area greater than "{num_a}"')
def should_see_greater_text_element(context, key, num_a):
    assert context.app.check_normal_text_element_isgreater(
        key, num_a), u'Text was not greater'


@step(u'I press "{key}"')
def i_press(context, key):
    assert context.web.press_element_by_key(key)


@step(u'press "{key_c}" in "{key_p}"')
def i_press_in_key(context, key_p, key_c):
    assert context.web.press_element_by_keys(key_p, key_c)


@step(u'I click "{key}"')
def i_click(context, key):
    assert context.web.click_element_by_key(key)


@step(u'click "{key_c}" in "{key_p}"')
def i_click_keys(context, key_p, key_c):
    assert context.web.click_element_by_keys(key_p, key_c)


@step(u'I click coords {x:d} and {y:d} of "{key}"')
def i_click_coords(context, x, y, key):
    assert context.web.click_element_coords(x, y, key)


@step(u'I fill in "{key}" with "{text}"')
def fill_with_text(context, key, text):
    assert context.web.fill_element_by_key(key, text)


@step(u'I click the link "{text}"')
def click_element_by_link(context, text):
    element = context.web.driver.find_element_by_link_text(text)
    hyperl = element.get_attribute('href')
    if element:
        element.click()
        return True
    return False


@step(u'I check "{key}"')
def check_checkbox(context, key):
    assert context.web.check_checkbox_by_key(key)


@step(u'I uncheck "{key}"')
def uncheck_checkbox(context, key):
    assert context.web.uncheck_checkbox_by_key(key)


@step(u'I check "{key}" is "{islarger}" and "{key1}" is "{islarger2}" than after click "{key2}" for {nsec:d} seconds')
def check_checkvalue(context, key, islarger, key1, islarger2, key2, nsec):
    assert context.app.check_checkbox_by_compare_values(key, islarger, key1, islarger2, key2, nsec)


@step(u'I should see an alert')
def should_see_alert(context):
    assert context.web.check_alert_existing()


@step(u'I should not see an alert')
def should_not_see_alert(context):
    assert not context.web.check_alert_existing()


@step(u'I accept the alert')
def i_accept_alert(context):
    assert context.web.accept_alert()


@step(u'I should see an alert with text "{text}"')
def should_see_alert_text(context, text):
    assert context.web.get_alert_text() == text, u'Text was not found'


@step(u'I wait {n:d} seconds')
def wait_senconds(context, n):
    time.sleep(n)


@step(u'I go to frame "{key}"')
def i_visit_frame(context, key):
    context.web.driver.switch_to_frame(key)
    assert True


@step(u'I go out of frame')
def i_jump_frame(context):
    context.web.driver.switch_to_default_content()
    assert True


@step(u'I should see nothing in "{attr}" attr of "{key}" area')
def check_text_by_key(context, attr, key):
    elements = context.web.driver.find_elements_by_id(key)
    if len(elements) == 1 and elements[0].get_attribute(attr) == "":
        assert True
    else:
        assert False


@step(u'I should see "{text}" with "{color}" color in "{key}" area')
def should_see_text_element_with_color_in_area(context, text, key, color):
    assert context.web.check_normal_text_element_timeout_with_color(
        text, key, color), u'The text or color is wrong'


@step(u'I should see "{key}" area in "{color}" color')
def should_see_text_element_with_color(context, key, color):
    assert context.web.check_normal_element_timeout_with_color(
        key, color), u'The color is wrong'


@step(u'I verify value in "{key}" is "{expecttype}" type')
def check_type_by_key(context, key, expecttype):
    typename = context.web.check_content_type(key, display=True)
    if typename == expecttype:
        assert True
    else:
        assert False


@step(
    u'I save div "{key}" as "{pic_name}" with width "{width}" and height "{height}"')
def save_div_with_attr(context, key, pic_name, width, height):
    assert context.web.save_div_as_picture(key, pic_name, width, height)


@step(u'I save div "{key}" as "{pic_name}"')
def save_div(context, key, pic_name):
    assert context.web.save_div_as_picture(key, pic_name, width=0, height=0)


@step(u'I remove all the pictures')
def remove_pic(context):
    assert context.web.remove_picture()


@step(u'I save the page to "{pic_name}"')
def save_page_per_conf(context, pic_name):
    assert context.web.save_page_per_conf(pic_name)


@step(u'I save the screenshot md5 as "{pic_name}"')
def save_page_as_base64(context, pic_name):
    assert context.web.save_base64_md5_pic(pic_name)


@step(u'file "{file_name}" of baseline and result should be the same')
def check_md5_file(context, file_name):
    assert context.web.check_md5_file_same(file_name)


@step(
    u'pic "{pic_name}" of baseline and result should be "{similarity}" similar if have results')
def check_base_result_similarity(context, pic_name, similarity):
    assert context.web.check_base_result_similarity(pic_name, similarity)


@step(u'I save "{p_name}" from "{key}" area')
def save_content_by_key(context, p_name, key):
    assert context.web.save_content(p_name, key)


@step(u'I click element with id "{key}" by js')
def click_button_by_js(context, key):
    assert context.web.click_element_by_id_with_js(key)


@step(u'I fill in element "{key}" by "{attr}" with "{text}"')
def fill_element_by_attr_with_text(context, key, attr, text):
    assert context.web.fill_element_by_key_attr(key, attr, text)


@step(u'"{second}" should be greater than "{first}"')
def compare_two_value(context, first, second):
    assert context.web.compare_two_values(
        first, second), u'The second value is less than the first one'

@step(u'"{first}" should be less than "{second}" beyond "{value}"')
def compare_two_value_with_range(context, first, second, value):
    assert context.web.compare_two_values_range(first, second, value)
