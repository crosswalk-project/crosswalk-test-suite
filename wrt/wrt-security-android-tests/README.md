## Introduction

This test suite is for wrt-security-android-tests

## Precondition

1. Connect Android devices to your localhost

2. Install the XwalkRuntime apk to devices if the test suite mode is shared.

3. Need to edit the file "wrt-security-android-tests/arch.txt" according to the type of test device.
   If test device is "x86" platform, content of the file should be "x86".

4. Need to edit the file "wrt-security-android-tests/mode.txt" according to the mode of build.
   If test need "embedded" mode, content of the file should be "embedded".

5. Set CROSSWALK_APP_TOOLS_CACHE_DIR
  ```export CROSSWALK_APP_TOOLS_CACHE_DIR=[local-path]```

6. Clone crosswalk-app-tools to CROSSWALK_APP_TOOLS_CACHE_DIR
   ```
   git clone https://github.com/crosswalk-project/crosswalk-app-tools
   cd crosswalk-app-tools
   sudo npm install
   ```
7. Download the crosswalk zip you want to test to CROSSWALK_APP_TOOLS_CACHE_DIR

## Test Step

1. unzip wrt-security-android-tests<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/wrt-security-android-tests/

4. run test case

   testkit-lite -f [testprefix-path]/opt/wrt-security-android-tests/tests.xml -A
   -o [testprefix-path]/opt/wrt-security-android-tests/result.xml --comm localhost
   --testenvs "DEVICE_ID=Medfield3C6DFF2E;CONNECT_TYPE=adb;XWALK_VERSION=18.46.458.0"
   --testprefix=[testprefix-path]

  DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
  Query device id by command "adb devices -l" in host.


## Authors:

* Wang, Hongjuan <hongjuanx.wang@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

