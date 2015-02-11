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
