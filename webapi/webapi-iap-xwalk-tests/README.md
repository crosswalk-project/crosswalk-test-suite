# In App Purchase Test Suite

## Introduction

This test suite is for checking In App Purchase support in Crosswalk Project:
* https://github.com/crosswalk-project/crosswalk-website/wiki/in-app-purchase
* https://crosswalk-project.org/jira/browse/XWALK-594

## Pre-conditions

To build an IAP application (e.g. this test suite), one needs to build IAP
extension `iap.jar` following the wiki page
[Manually Build IAP Extension](https://github.com/crosswalk-project/crosswalk-android-extensions/wiki/Manually-Build-IAP-Extension)

And one needs also to copy the `iap.js` and `iap.json` files to
`webapi-iap-xwalk-tests/iap` from
[crosswalk-android-extensions/iap](https://github.com/crosswalk-project/crosswalk-android-extensions/tree/master/iap).

Please login an account for Google Play or Xiaomi Store and make sure you can purchase products before the test. 
Specially for Google Play, please make sure 
1. You can connect to Google Play server
2. Your credit card had been bound to your Google account.
3. You Google account must be added to the testing group of iapdemo app in the Google Play Developer Console.

All the test cases are required to test on the Android 4.4.2 system.

## Authors

* Liu, Yun <yunx.liu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>
* Qiu, Zhong <zhongx.qiu@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
