## Introduction

This test suite is for cordova-api-ios-tests

1. ./setup_ios.py is download the projects crosswal-ios and mobileSpec-crosswalk

## Precondition

1. Connect iOS devices to your localhost

2. Make Sure the command line "ios-deploy" is available, if not installed, please link:
   https://github.com/phonegap/ios-deploy 

## Run Test:

1. unzip cordova-api-ios-tests<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/cordova-api-ios-tests/cordovaapi

3. `./mobilespec_test.py -d "destinationspecifier" -u "DEVICE_ID"`

## Authors:

* Wang, Hongjuan <hongjuanx.wang@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

