from atip.common.steps import *
from atip.web.steps import *
import time
import datetime

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
        text, key, color), u'Text was not found'

@step(u'I should see "{key}" area in "{color}" color')
def should_see_text_element_with_color(context, key, color):
    assert context.app.check_normal_element_timeout_with_color(
        key, color), u'The background color is wrong'

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

@step(u'pic "{pic1}" and pic "{pic2}" should be more than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.app.check_pic_same(pic1, pic2, similarity)

@step(u'pic "{pic1}" and pic "{pic2}" should be less than "{similarity}" similar')
def check_picture(context, pic1, pic2, similarity):
    assert context.app.check_pic_different(pic1, pic2, similarity)

@step(u'I remove all the pictures')
def remove_pic(context):
    assert context.app.remove_picture()

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
    assert context.app.compare_two_values(first, second), u'The second value is lesser than the first one'

@step(u'I should not see "{text}" in "{key}" area')
def should_see_text_element(context, text, key):
    assert context.app.check_normal_text_element_not_exist(
        text, key, display=True), u'Text exists!'
