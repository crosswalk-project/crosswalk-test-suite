ATIP - a new BDD binding library 
===============

## Introduction

ATIP(Application Test in Python), a "behave" binding library as the bridge between application and BDD to "behave", and use WebDriver and platform interfaces to implement detailed BDD steps for application. 

## Configuration

Environmental controls. In ATIP usage, you can write the environment initial processes on this file. ATIP provides two templates of "environment.py" for tests developers. One is for WebDriver backend, the other is for uiautomator backend. These templates support running tests independently by "behave" tool.

In WebDriver testing, the template need to know the some test variables, e.g. which device be tested? which test platform? Some WebDriver variables. These variables can be got by following ways:

* By environment variables:  
  TEST_PLATFORM: android, tizen, chrome_ubuntu, others(if have)   
  DEVICE_ID    
  CONNECT_TYPE: adb, sdb   
  WEBDRIVER_VARS: webdriver_url, desired_capabilities, others  
  LAUNCHER: XWalkLauncher, CordovaLauncher

In uiautomator testing, only two environment variables are required, "TEST_PLATFORM" and "DEVICE_ID". This allows running uiautomator tests independently without WebDriver.

ATIP source provides a script "tools/set_env.sh" which can help you to setup those environment variables. Especially, the environment.py template can get those environment variables from Testkit-lite tool automatically:

A JSON config file which named "bdd.json for environment variables sharing, a template provided for reference: "atip/tools/bdd.*.json"  

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
                <td>Select object by relative position</td>
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
                <td>Get view info from object by key</td>
        </tr>
        <tr>
                <td></td>
                <td>Save view to object</td>
        </tr>
        <tr>
                <td></td>
                <td>Save finding view process</td>
        </tr>
        <tr>
                <td></td>
                <td>Reload above process to get object</td>
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
@step(u'I swipe view "{params_kw}" to "{orientation}"')
@step(u'I swipe saved object "{key}" to "{orientation}"')
@step(u'I force to run all watchers')
@step(u'I remove all watchers')
@step(u'I register watcher "{watcher_name}" when "{when_text}" click "{click_text}"')
@step(u'I register watcher2 "{watcher_name}" when "{when_text1}" and "{when_text2}" click "{click_text}"')
@step(u'I should see view "{params_kw}"')
@step(u'I should see relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
@step(u'I should see view "{params_kw}" in {time_out:d} seconds')
@step(u'I should see relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}" in {time_out:d} seconds')
@step(u'I should not see view "{params_kw}"')
@step(u'I should not see relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
@step(u'I click view "{params_kw}"')
@step(u'I click saved object "{key}"')
@step(u'I edit view "{params_kw}" to input "{text}"')
@step(u'I edit index {n:d} EditText to input "{text}"')
@step(u'The view "{params_kw}" info "{info_name}" should be "{except_result}"')
@step(u'The saved info "{key1}" is equal to "{key2}"')
@step(u'The saved info "{key1}" is unequal to "{key2}"')
@step(u'I save view "{params_kw}" to object by "{key}"')
@step(u'I save relative view "{params_kw1}" on the "{position}" side of view "{params_kw2}" to object "{key}"')
@step(u'I save object "{key}" info "{info_name}" to temp "{info_key}"')
@step(u'I save process of finding view "{params_kw1}" on the "{position}" side of view "{params_kw2}"')
@step(u'I reload above process and save result to object "{key}"')
@step(u'I wait saved object "{key}" gone in {time_out:d} seconds')
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
@step(u'I open GPS')
@step(u'I close GPS')
@step(u'I execute command "{command_line}"')
@step(u'I save command "{command_line}" result "{result_key}"')
@step(u'The value "{expected_value}" should be in result "{result_key}"')
```

## Run Tests 

* Testkit-lite: Please check testkit-lite project for details
* Behave: setup test ENVs by set_env.sh or bdd.json firstly, then run "behave" as:  
  cd path-to/tests  
  behave  

