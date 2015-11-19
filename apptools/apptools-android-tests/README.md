## Introduction

This test suite is for apptools-android-tests

1. ./allpairs.py is create pkgName.py and report directory for package name

## Common Precondition

1. Connect Android devices to your localhost

2. Need to edit the file "apptools-android-tests/arch.txt" according to the type of test device.
   If test device is "arm" platform, content of the file should be "arm". If test device is "x86" platform, content of the file should be "x86".
   If test devices are "arm" and "x86" platforms, content of the file should be "arm,x86", default value is "x86,arm"

3. Need to edit the file "apptools-android-tests/mode.txt" according to the type of build mode.
   If create project with crosswalk lite zip, content of the file should be "lite". If create project with crosswalk zip and build "shared" mode apk, content of the file should be "shared". If create project with crosswalk zip and build "embedded" mode apk, content of the file should be "embedded".
(Note: If you test "shared" mode, when uninstall crosswalk runtime library from android device before testing, it will be prompted to download crosswalk runtime library from google play in formal test process.)

4. Need to edit the file "apptools-android-tests/host.txt" according to the type of test host.
   If test host is "Windows" platform, content of the file should be "Windows", default value is "Android".

5. Need to edit the file "apptools-android-tests/version.txt" according to the Crosswalk which you want to test.
   For example: if you want to test with "crosswalk-17.45.434.0.zip", content of the file should be "17.45.434.0 32". If you want to test with "crosswalk-17.45.434.0-64bit.zip", content of the file should be "17.45.434.0 64".

6. The node.js, Android SDK, JDK, apache ant, and git must be functional

7. Install webp conversion tool from http://downloads.webmproject.org/releases/webp


## Precondition for AppTools on Linux or OS X host

1. Download crosswalk-app-tools and release crosswalk zip to apptools-android-tests/tools, then install npm and exec-sync

  1.1 cd tools, then clone source code from https://github.com/crosswalk-project/crosswalk-app-tools

  1.2 Download the release Crosswalk zip which you want to test

  1.3 Run commands: cd crosswalk-app-tools, then run:

      sudo npm install
      sudo npm install exec-sync

2. Install nodeunit: `sudo npm install nodeunit -g`

3. Environment variable configuration:

  3.1 export DEVICE_ID=test device id, DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00"

  3.2 export ANDROID_HOME=$(dirname $(dirname $(which android)))

  3.3 export CROSSWALK_APP_TOOLS_CACHE_DIR=/path/to/opt/apptools-android-tests/tools

4. Install BeautifulSoup: `sudo pip install BeautifulSoup`


## Precondition for AppTools on Windows host

1. Download crosswalk-app-tools and release crosswalk zip to apptools-android-tests/tools, then install npm

  1.1 cd tools, then clone source code from https://github.com/crosswalk-project/crosswalk-app-tools

  1.2 Download the release Crosswalk zip which you want to test

  1.3 Run commands: cd crosswalk-app-tools, then run:

      npm install
      npm install exec-sync

2. Install nodeunit: `npm install nodeunit -g`

3. Environment variable configuration:

  3.1 Set DEVICE_ID env, DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00"

  3.2 Set ANDORID_HOME env

  3.3 Set CROSSWALK_APP_TOOLS_CACHE_DIR env to /path/to/opt/apptools-sampleapp-tests/tools

4. Install BeautifulSoup: `pip install BeautifulSoup`

## Test Steps

1. unzip apptools-android-tests<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/apptools-android-tests/

3. run test case

   testkit-lite -f [testprefix-path]/opt/apptools-android-tests/tests.xml -A
   -o [testprefix-path]/opt/apptools-android-tests/result.xml --comm androidmobile
   --deviceid=Medfield3C6DFF2E --testprefix=[testprefix-path]

  DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
  Query device id by command "adb devices -l" in host.

## Authors:

* Wang, Hongjuan <hongjuanx.wang@intel.com>
* Yun, Liu<yunx.liu@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
