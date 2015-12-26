## Introduction

This test suite is for testing wrt-packagemgt-tests specification

## Test Step

1. unzip -d [testprefix-path] wrt-packagemgt-tests<version>.zip

2. cd [testprefix-path]/opt/wrt-packagemgt-tests/

3. ./inst.py -i

4. run test case

   testkit-lite -f [testprefix-path]/opt/wrt-packagemgt-tests/tests.xml -A
   -o [testprefix-path]/opt/wrt-packagemgt-tests/result.xml --comm localhost
   --testprefix [testprefix-path]

## Authors:

* Zhu, Yongyong <yongyongx.zhu@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
