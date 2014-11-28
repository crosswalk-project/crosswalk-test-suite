## Introduction

This test suite is for testing android basic featrue

## Precondition

1. download Xwalk Runtime Library and put it in crosswalk-test-suite/tools folder
2. need to update the file Crosswalk_sharedmode.conf according to the package path

## Authors:

* Ivan Chen <yufeix.chen@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

Test Step:
1. unzip -d [testprefix-path] wrt-sharedmode-android-tests<version>.zip
2. cd [testprefix-path]/opt/wrt-sharedmode-android-tests/
3. ./inst.py -i
4. run test case
   testkit-lite -f [testprefix-path]/opt/wrt-sharedmode-android-tests/tests.xml -A -o [testprefix-path]/opt/wrt-sharedmode-android-tests/result.xml --comm localhost --testprefix [testprefix-path] --testenvs "DEVICE_ID=E6OKCY411012  CONNECT_TYPE=adb".
