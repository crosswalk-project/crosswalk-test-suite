## Introduction

This test suite is for usecase-wrt-auto-tests

## Precondition

1. Connect Android devices to your localhost
2. Set the path of make_apk.py to environment path and chmod it.
3. Install the XwalkRuntime apk to devices if the test suite mode is shared. 
4. Need to edit the file "usecase-wrt-auto-tests/arch.txt" according to the type of test device.
If test device is "arm" platform, content of the file should be "arm", default value is "x86".
5. Need to edit the file "usecase-wrt-auto-tests/mode.txt" according to the mode of build.
If test need "shared" mode, content of the file should be "shared", default value is "embedded"

## Authors:

* Wang, Hongjuan <hongjuanx.wang@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

Test Step:
1. unzip usecase-wrt-auto-tests<version>.zip -d [testprefix-path]
2. cd [testprefix-path]/opt/usecase-wrt-auto-tests/
3. run test case
   testkit-lite -f [testprefix-path]/opt/usecase-wrt-auto-tests/tests.xml -A -o [testprefix-path]/opt/usecase-wrt-auto-tests/result.xml --comm androidmobile --deviceid=Medfield3C6DFF2E
   --testprefix=[testprefix-path]
Query device id by command "adb devices -l" in host.
