ATIP - a new BDD binding library 
===============

## Introduction

ATIP(Application Test in Python), a "behave" binding library as the bridge between application and BDD to "behave", and use WebDriver and platform interfaces to implement detailed BDD steps for application. 

## Configuration

Environmental controls. In ATIP usage, you can write the environment initial processes in config file - environment.py. ATIP provides a template of "environment.py" for tests developers. This template supports running tests independently by "behave" tool.

In Crosswalk testing, the template need to know the some test vars, e.g. which device be tested? which test platform? Some WebDriver vars. the vars can be got by following ways:  

* By environment vars:  
  TEST_PLATFORM: android, tizen, chrome_ubuntu, others(if have)   
  DEVICE_ID    
  CONNECT_TYPE: adb, sdb   
  WEBDRIVER_VARS: webdriver_url, desired_capabilities, others  
  LAUNCHER: XWalkLauncher, CordovaLauncher

ATIP source provides a script "tools/set_env.sh" which can help you to setup those environment vars. Especially, the environment.py template can get those environment vars from Testkit-lite tool automatically:

A JSON config file which named "bdd.json for environment vars sharing, a template provided for reference: "atip/tools/bdd.*.json"  

* Configuration source layout
```
tools/
|-- set_env.sh
|-- bdd.chrome.json
|-- bdd.android_cordova.json
|-- bdd.android_xwalk.json
`-- bdd.xw_tizen.json
```

## Tests Development
Before below sections, you'd better already pretty familiar with the tests developing with "behave": "behave" docs. A typical "behave" based tests source layout as below:

```
tests/
|-- environment.py
|-- steps
|   `-- steps.py
`-- test.feature
 
```

* test.feature  
  
A simple feature example as below
```
Feature: api tests
    Scenario: api test 001
        When launch "haha"
         And I go to "http://www.google.com"
         And I wait for 1 seconds
```

* steps.py  
  
A simple step example as below
```
@step(u'I go to "{url}"')
def i_visit_url(context, url):
    url = get_page_url(context, url)
    assert context.web.switch_url(url, True)
```

## ATIP Library  

* WebDriver Library Overview

<table>
  <tr>
                <td>Category</td>
                <td>Steps</td>
        </tr>
        <tr>
                <td>Web Element Management</td>
                <td>Create element</td>
        </tr>
        <tr>
                <td></td>
                <td>Click element</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by id</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by tag name</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by xpath</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by class name</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by css selector</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by link text</td>
        </tr>
        <tr>
                <td></td>
                <td>Find element(s) by partial link text</td>
        </tr>
        <tr>
                <td>Window Management</td>
                <td>get current window handle</td>
        </tr>
        <tr>
                <td></td>
                <td>get window position</td>
        </tr>
        <tr>
                <td></td>
                <td>get window size</td>
        </tr>
        <tr>
                <td></td>
                <td>maximize window</td>
        </tr>
        <tr>
                <td></td>
                <td>set window position</td>
        </tr>
        <tr>
                <td></td>
                <td>set window size</td>
        </tr>
        <tr>
                <td></td>
                <td>close current window</td>
        </tr>
        <tr>
                <td></td>
                <td>switch to alert</td>
        </tr>
        <tr>
                <td></td>
                <td>switch to window</td>
        </tr>
        <tr>
                <td></td>
                <td>switch to frame</td>
        </tr>
        <tr>
                <td>Page Management</td>
                <td>get url of current page</td>
        </tr>
        <tr>
                <td></td>
                <td>get source of current page</td>
        </tr>
        <tr>
                <td></td>
                <td>get page title</td>
        </tr>
        <tr>
                <td></td>
                <td>refresh current page</td>
        </tr>
        <tr>
                <td></td>
                <td>forward the page</td>
        </tr>
        <tr>
                <td></td>
                <td>backward the page</td>
        </tr>
        <tr>
                <td>Cookie</td>
                <td>add cookie</td>
        </tr>
        <tr>
                <td></td>
                <td>get cookie(s)</td>
        </tr>
        <tr>
                <td></td>
                <td>delete cookie</td>
        </tr>
        <tr>
                <td></td>
                <td>delete all cookies</td>
        </tr>
        <tr>
                <td>Execution External</td>
                <td>execute command</td>
        </tr>
        <tr>
                <td></td>
                <td>execute script synchronously</td>
        </tr>
        <tr>
                <td></td>
                <td>execute script asynchronously</td>
        </tr>
        <tr>
                <td>Image Processing</td>
                <td>get screenshot as base64</td>
        </tr>
        <tr>
                <td></td>
                <td>get screenshot as file/png</td>
        </tr>
</table>

* Uiautomator Library Overview

<table>
  <tr>
                <td>Category</td>
                <td>Steps</td>
        </tr>
        <tr>
                <td>Android System Operation</td>
                <td>Turn on/off device</td>
        </tr>
        <tr>
                <td></td>
                <td>Press hard/soft key</td>
        </tr>
        <tr>
                <td></td>
                <td>Set device orientation</td>
        </tr>
        <tr>
                <td></td>
                <td>Freeze/unfreeze device rotation</td>
        </tr>
        <tr>
                <td></td>
                <td>Take screenshot</td>
        </tr>
        <tr>
                <td></td>
                <td>Open notification</td>
        </tr>
        <tr>
                <td></td>
                <td>Open quick settings</td>
        </tr>
        <tr>
                <td></td>
                <td>Turn on/off wifi</td>
        </tr>
        <tr>
                <td></td>
                <td>Turn on/off airplane mode</td>
        </tr>                
        <tr>
                <td></td>
                <td>Identify current launched app</td>
        </tr>
        <tr>
                <td>Gesture Action</td>
                <td>Fling by orientation and direction</td>
        </tr>
        <tr>
                <td></td>
                <td>Fling to end</td>
        </tr>
        <tr>
                <td></td>
                <td>Scroll forward vertically</td>
        </tr>
        <tr>
                <td></td>
                <td>Scroll to end</td>
        </tr>
        <tr>
                <td></td>
                <td>Scroll to text</td>
        </tr>
        <tr>
                <td></td>
                <td>Swipe object to some direction</td>
        </tr>
        <tr>
                <td>Watcher Management</td>
                <td>Register watcher</td>
        </tr>
        <tr>
                <td></td>
                <td>Remove all watchers</td>
        </tr>
        <tr>
                <td></td>
                <td>Reset all watchers</td>
        </tr>
        <tr>
                <td></td>
                <td>Run all watchers</td>
        </tr>
        <tr>
                <td>Selector Management</td>
                <td>Select object by key, value and class name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select any object by value and class name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select TextView object by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select Button object by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select Edit object by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select ImageView object by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select ImageButton object by name</td>
        </tr>
        <tr>
                <td></td>
                <td>Select View object by desc</td>
        </tr>
        <tr>
                <td></td>
                <td>Select Web object by desc</td>
        </tr>
        <tr>
                <td></td>
                <td>Select object by direction and class name</td>
        </tr>
        <tr>
                <td></td>
                <td>Wait for object show</td>
        </tr>
        <tr>
                <td></td>
                <td>Wait for object gone</td>
        </tr>
        <tr>
                <td>Object Management</td>
                <td>Click object</td>
        </tr>
        <tr>
                <td></td>
                <td>Edit text</td>
        </tr>
        <tr>
                <td></td>
                <td>Get object info from temp by key</td>
        </tr>
        <tr>
                <td></td>
                <td>Get object info by text</td>
        </tr>
        <tr>
                <td></td>
                <td>Save object info to temp</td>
        </tr>
</table>

* Functions Category  
  "web": web based(Webdriver API) functions  
  "native": native based functions (TBD)  
  "common": common operations cross different platforms, e.g. call python image lib to compare image files  
  "android": Android platform specific functions which is implemented by uiautomator  
  "tizen": Tizen platform specific functions  

* "web" steps - done
```
@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}"')
@step(u'switch to "{app_name}"')
@step(u'I go to "{url}"')
@step(u'I reload')
@step(u'I go back')
@step(u'I go forward')
@step(u'The current URL should be "{text}"')
@step(u'I should see title "{text}"')
@step(u'I should see "{text}"')
@step(u'I should not see "{text}"')
@step(u'I should see "{text}" in {timeout:d} seconds')
@step(u'I should not see "{text}" in {timeout:d} seconds')
@step(u'I should see "{text}" in "{key}" area')
@step(u'I press "{key}"')
@step(u'press "{key_c}" in "{key_p}"')
@step(u'I click "{key}"')
@step(u'click "{key_c}" in "{key_p}"')
@step(u'I click coords {x:d} and {y:d} of "{key}"')
@step(u'I fill in "{key}" with "{text}"')
@step(u'I check "{key}"')
@step(u'I uncheck "{key}"')
@step(u'I should see an alert')
@step(u'I should not see an alert')
@step(u'I accept the alert')
@step(u'I should see an alert with text "{text}"')
```

* "android" steps - done
```
@step(u'I launch "{app_name}" with "{apk_pkg_name}" and "{apk_activity_name}" on android')
@step(u'I scroll to end')
@step(u'I fling "{orientation}" goto "{direction}"')
@step(u'I swipe object "{key}" to "{orientation}"')
@step(u'I force to run all watchers')
@step(u'I remove all watchers')
@step(u'I register watcher "{watcher_name}" when "{when_text}" click "{click_text}"')
@step(u'I register watcher2 "{watcher_name}" when "{when_text1}" and "{when_text2}" click "{click_text}"')
@step(u'I should see text "{text_name}"')
@step(u'I should see image "{image_name}"')
@step(u'I should see web "{web_desc}"')
@step(u'I should see view "{view_desc}"')
@step(u'I should see "{class_name}" on the "{relative}" side of text "{text_name}"')
@step(u'I should see "{class_name}" on the "{relative}" side of view "{view_desc}"')
@step(u'I should see "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}"')
@step(u'I wait object "{key}" exist for "{time_out}"')
@step(u'I wait object "{key}" gone for "{time_out}"')
@step(u'I click button "{button_name}"')
@step(u'I click other "{class_name}" by "{which_key}" "{which_value}"')
@step(u'I click object "{key}"')
@step(u'I edit text "{edit_text}" to input "{text}"')
@step(u'I edit index {n:d} text to input "{text}"')
@step(u'I compare text "{text_name}" info "{what}" with "{except_result}"')
@step(u'I compare view "{view_desc}" info "{what}" with "{except_result}"')
@step(u'I compare object "{key1}" equal "{key2}" on info "{what}"')
@step(u'I compare object "{key1}" unequal "{key2}" on info "{what}"')
@step(u'I save text object "{text_name}" to temporary value "{key}"')
@step(u'I save view object "{view_desc}" to temporary value "{key}"')
@step(u'I save any object "{class_name}" "{value_name}" to temporary value "{key}"')
@step(u'I save "{class_name}" on the "{relative}" side of text "{text_name}" to temporary value "{key}"')
@step(u'I save "{class_name}" on the "{relative}" side of view "{view_desc}" to temporary value "{key}"')
@step(u'I save "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}" to temporary value "{key}"')
@step(u'I process text object "{text_name}"')
@step(u'I process view object "{view_desc}"')
@step(u'I process any object "{class_name}" "{value_name}"')
@step(u'I process "{class_name}" on the "{relative}" side of text "{text_name}"')
@step(u'I process "{class_name}" on the "{relative}" side of view "{view_desc}"')
@step(u'I process "{class_target}" on the "{relative}" side of any "{class_name}" "{value_name}"')
@step(u'I reload process result to temporary value "{key}"')
```

* "common" steps - done
```
@step(u'I wait for {timeout:d} seconds')
@step(u'call "{js}" scripts') - TBD
@step(u'call PIL to handle "{image_file}"') - TBD
@step(u'launch "{app_name}"')
@step(u'I turn on device')
@step(u'I turn off device')
@step(u'I set orientation "{orientation}"')
@step(u'I take screenshot as "{name}"')
@step(u'I open notification')
@step(u'I open quick settings')
@step(u'I press "{key}" hardware key')
@step(u'I open wifi')
@step(u'I close wifi')
@step(u'I open airplane mode')
@step(u'I close airplane mode')
```

## Run Tests 

* Testkit-lite: Please check testkit-lite project for details
* Behave: setup test ENVs by set_env.sh or bdd.json firstly, then run "behave" as:  
  cd path-to/tests  
  behave  

