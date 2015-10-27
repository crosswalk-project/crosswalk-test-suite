## Introduction

This test suite is for testing wrt-extension-android-tests specification

## Precondition

1. download Xwalk Runtime Library and put it in crosswalk-test-suite/tools folder

## Authors:

* Xu,Yuhan <yuhanx.xu@intel.com>

## Test Step

1. unzip -d [testprefix-path] wrt-extension-android-tests<version>.zip

2. cd [testprefix-path]/opt/wrt-extension-android-tests/

3. ./inst.py -i

4. run test case

   testkit-lite -f [testprefix-path]/opt/wrt-extension-android-tests/tests.xml -A
   -o [testprefix-path]/opt/wrt-extension-android-tests/result.xml --comm localhost
   --testprefix [testprefix-path] --testenvs "DEVICE_ID=Medfield3D5BD1C7 CONNECT_TYPE=adb"

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
