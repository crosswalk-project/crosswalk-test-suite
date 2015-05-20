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
* AdMob3.6: https://github.com/floatinghotpot/cordova-plugin-admob
* AdMob4.0: https://github.com/floatinghotpot/cordova-admob-pro

Make a directory named "thirdparty_plugins", and git clone these plugins in it.

For easy to be used in suite.json, need rename the plugins:
* cordova-plugin-admob -> cordova-admob-3.6
* cordova-admob-pro -> cordova-admob-4.0

## LICENSE

Copyright (c) 2013 Intel Corporation.  All rights reserved.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the LICENSE.BSD-3 file for the BSD-3-Clause License.
