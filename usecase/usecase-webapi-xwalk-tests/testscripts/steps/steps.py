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

@step(u'I should see nothing in "{key}"')
def check_text_by_key(context, key):
    elements = context.app.driver.find_elements_by_id(key)
    if len(elements) == 1 and elements[0].get_attribute("value") == "":
        assert True
    else:
        assert False

@step(u'I should see "{text}" with "{color}" color in "{key}" area')
def should_see_text_element_with_color(context, text, key, color):
    assert context.app.check_normal_text_element_timeout_with_color(
        text, key, color), u'Text was not found'

@step(u'I verify value in "{key}" is "{expecttype}" tpye')
def check_type_by_key(context, key, expecttype):
    typename = context.app.check_content_type(key, display=True)
    if typename == expecttype:
        assert False
    else:
        assert False

@step(u'I save "{p_name}" from "{key}" area')
def check_type_by_key(context, p_name, key):
    assert context.app.save_content(p_name, key)

@step(u'"{second}" should be greater than "{first}"')
def check_type_by_key(context, first, second):
    assert context.app.compare_two_values(first, second), u'The second value is lesser than the first one'

