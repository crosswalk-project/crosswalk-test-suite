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
* Screenshot4.x: https://github.com/gitawego/cordova-screenshot
* Screenshot3.6: Get https://github.com/gitawego/cordova-screenshot and return to commit:6ac9f15316b680110f6c448798fabdb978698b44

Make a directory named "thirdparty_plugins", and git clone these plugins in it.

For easy to be used in suite.json, need rename the plugins:
* For Cordova 3.6: cordova-screenshot -> cordova-screenshot-3.6
* For Cordova 4.x: cordova-screenshot -> cordova-screenshot-4.x

## LICENSE

Copyright (c) 2013 Intel Corporation.  All rights reserved.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the LICENSE.BSD-3 file for the BSD-3-Clause License.
