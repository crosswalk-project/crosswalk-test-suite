## Introduction

Behavior Test Tool is a device behavior checker that uses jQuery.
It has these features:

* A list of behaviors you can test, with information about test cases
* Test cases for checking and evaluating the behavior of a device
* Automatically generated test reports you can view and save for further analysis

## Authors:

* Lin, Wanming <wanmingx.lin@intel.com>

## Pre-condition

There are third-party plugins needed for cordova usecase:
* AdMob: https://github.com/floatinghotpot/cordova-admob-pro
* Screenshot: https://github.com/gitawego/cordova-screenshot

Git clone these plugins in extra_plugins.

For easy to be used in suite.json, need rename the plugins:
* cordova-admob-pro -> cordova-admob
* cordova-screenshot -> cordova-screenshot

## Test Steps
* update usecase-cordova-android-tests/res/pack-type if your want to install cordova-plugin-crosswalk-webview from 'npm'

## LICENSE

Copyright (c) 2013 Intel Corporation.  All rights reserved.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the LICENSE.BSD-3 file for the BSD-3-Clause License.
