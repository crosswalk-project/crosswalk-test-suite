## Introduction

This test suite is for testing Crosswalk Lite in https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview
feature: https://crosswalk-project.org/jira/browse/XWALK-5095


## Pre-conditions

* Require Android API level 22
* Require the latest Cordova CLI, and must >= 5.0.0, install with command: `$ sudo npm install cordova -g`
* Get cordova_sampleapp.zip from internal release link, then unzip it to /tmp/cordova-sampleapp/


## Test Steps
1. unzip cordova-lite-android-tests<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/wrt-apptools-android-tests/

3. update arch.txt if your run with 'x86' device

4. run test case

   ```
   testkit-lite -f [testprefix-path]/opt/cordova-lite-android-tests/tests.xml -A
   -o [testprefix-path]/opt/cordova-lite-android-tests/result.xml --comm localhost
   --testenvs "DEVICE_ID=Medfield3C6DFF2E;CONNECT_TYPE=adb" --testprefix=[testprefix-path]
   ```

   DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
   Query device id by command "adb devices -l" in host.

## Authors:

* Zhu, Yongyong <yongyongx.zhu@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
