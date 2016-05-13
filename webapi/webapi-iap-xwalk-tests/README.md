# In App Purchase Test Suite

## Introduction

This test suite is for checking In App Purchase support in Crosswalk Project:
* https://github.com/crosswalk-project/ios-extensions-crosswalk/blob/master/extensions/InAppPurchase/spec/iap.html
* https://crosswalk-project.org/jira/browse/XWALK-5695

## Pre-conditions

Get IAP extension iap.zip from [crosswalk-android-extensions/iap](https://github.com/crosswalk-project/crosswalk-android-extensions/releases). Then unzip the iap.zip file and copy all the files to `webapi-iap-xwalk-tests/iap`

Please login an account for Google Play or Xiaomi Store and make sure you can purchase products before the test.

Specially for Google Play, please make sure
* You device can connect to Google Play server successfully.
* Your credit card had been bound to your Google account.
* You Google account must be added to the testing group of iapdemo app in the Google Play Developer Console.

All the test cases are required to test on the Android 4.4.2 system.

## Authors

* Liu, Yun <yunx.liu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>
* Qiu, Zhong <zhongx.qiu@intel.com>
* He, YUe <yue.he@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

## Sign the Google Play IAP apk

The Google Play IAP purchase api need signed apk to test.
After pack the apk, use the following commands to sign and align:
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore iapdemo.keystore iapdemo.apk  iapdemo
zipalign -v 4 iapdemo.apk iapdemo_release.apk
