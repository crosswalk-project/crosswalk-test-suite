from behaving.web.steps import *

@when(u'I click center area')
def step_impl(context):
    context.browser.execute_script('document.getElementsByTagName("area")[0].click()')

@when(u'I click around area')
def step_impl(context):
    context.browser.execute_script('document.getElementsByTagName("area")[1].click()')
