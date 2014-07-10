from behaving.web.steps import *

@then(u'There should be A and Finished! on the page')
def step_impl(context):
    a = context.browser.find_by_tag('dt')[0].text
    finish =  context.browser.find_by_tag('p')[2].text
    assert a == "A" and finish == "Finished!"
