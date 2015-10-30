## Introduction

This test suite is for testing wrt-packagemgt-android-tests specification

## Test Step

1. unzip -d [testprefix-path] wrt-packagemgt-android-tests<version>.zip

2. cd [testprefix-path]/opt/wrt-packagemgt-android-tests/

3. ./inst.py -i

4. run test case

   testkit-lite -f [testprefix-path]/opt/wrt-packagemgt-android-tests/tests.xml -A
   -o [testprefix-path]/opt/wrt-packagemgt-android-tests/result.xml --comm localhost
   --testprefix [testprefix-path]

## Authors:

* Xu,Yuhan <yuhanx.xu@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
