from behaving.web.steps import *

@when(u'I click on blank')
def step_impl(context):
    context.browser.find_by_tag('p').first.click()
