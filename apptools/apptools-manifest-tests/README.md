## Introduction

This test suite is for apptools-manifest-tests


## Common Precondition

1. Install node(>=0.12)

2. Download crosswalk-app-tools, then install npm

  2.1 Download source code from https://github.com/crosswalk-project/crosswalk-app-tools

  2.2 Run commands: cd crosswalk-app-tools, then run: npm install

3. The main script is crosswalk-app-tools/src/crosswalk-pkg. Set environment PATH or invoke with directory
  (Note: On Windows, Need create 'crosswalk-pkg' env, invoke with 'crosswalk-app-tools/src/crosswalk-pkg' directory).

4. Edit your input_seed.txt(in ./allpairs/) file to generate webapp.


## Precondition for AppTools on Android

1. Connect Android devices to your localhost

2. The Android SDK, JDK and apache ant must be functional

3. Download release crosswalk zip

  3.1 Download the release Crosswalk zip which you want to test, and edit "../../VERSION"

4. Install webp conversion tool from http://downloads.webmproject.org/releases/webp

5. Install exec-sync

  5.1 Run commands: cd crosswalk-app-tools, then run:
      npm install exec-sync

6. Environment variable configuration:

  6.1 Set ANDORID_HOME env

  6.2 Set CROSSWALK_APP_TOOLS_CACHE_DIR env to the release Crosswalk zip downloaded dir

  6.3 Set DEVICE_ID env, DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00"

7. Need to edit the file "apptools-manifest-tests/arch.txt" according to the type of test device.
   If test device is "arm" platform, content of the file should be "arm". If test device is "x86" platform, content of the file should be "x86".
   If test devices are "arm" and "x86" platforms, content of the file should be "arm,x86", default value is "x86,arm"
   If you want to test with 64 bit crosswalk, content of the file should be "arm,x86,64", default value is "x86,arm,32"

8. Need to edit the file "apptools-manifest-tests/mode.txt" according to the type of build mode.
   If create project with crosswalk lite zip, content of the file should be "lite". If create project with crosswalk zip and build "shared" mode apk, content of the file should be "shared". If create project with crosswalk zip and build "embedded" mode apk, content of the file should be "embedded".
(Note: If you test "shared" mode, when uninstall crosswalk runtime library from android device before testing, it will be prompted to download crosswalk runtime library from google play in formal test process.)


## Precondition for AppTools on Windows

1. Install WiX per https://msdn.microsoft.com/en-us/library/gg513936.aspx (do not forget to add the WiX tools to the windows path environment variable)

2. Download release crosswalk zip

  2.1 Download the release Crosswalk zip which you want to test, and edit "../../VERSION"

3. Environment variable configuration:

  3.1 Set CROSSWALK_APP_TOOLS_CACHE_DIR env to the release Crosswalk zip downloaded dir


## Precondition for AppTools on Deepin

1. The debuild tool, and the Crosswalk runtime must be functional

2. Checkout the deb backend: cd crosswalk-app-tools/node_modules, then download source code from https://github.com/crosswalk-project/crosswalk-app-tools-deb.git crosswalk-app-tools-backend-deb

3. Install dependencies: cd crosswalk-app-tools-backend-deb, then npm install, and cd ../..


## Precondition for AppTools on iOS

1. Connect iOS devices to your localhost

2. the Xcode command line tools, and the Xcode iOS SDK 8.1 must be functional

3. Checkout the iOS backend: cd crosswalk-app-tools/node_modules, then download source code from https://github.com/crosswalk-project/crosswalk-app-tools-ios.git crosswalk-app-tools-backend-ios

4. Install dependencies: cd crosswalk-app-tools-backend-ios, then npm install, and cd ../..


## Layout

1. allpairs is seed file folder:

  1.1 allparis/positive -> positive seed folder,support multi seed files
      allparis/negative -> negative seed folder,support multi seed files

  1.2 seed file format:

     1)Values separator ","
       name-1:a,b

     2)The same field value separter by "-":
       name-1:a,b
       name-2:c,d

     3)Self combination add 'null' to each self field:
       name-2:000,a000b,000b,b000,null

     4)The space character please use 000 to replace:
       000a-> a,a000b->a b,b000->b

     5)The icon value include ",", so the separator is "comma",please refer to seed file:
       icon-1:{"src": "icon/lowres"comma"sizes": "64x64"comma"type": "image/webp"}

2. ./resource/ folder is webapp resource file, such as index.html icon.png....

3. ./metacomm/ folder is allpairs.

4. ./ge_manifest.py create manifest resource

5. ./ge_package.py create manifest package

6. ./ge_unitcase.py create tests.py


## Test Steps

1. unzip -d [testprefix-path] apptools-manifest-tests<version>.zip

2. cd [testprefix-path]/opt/apptools-manifest-tests/

3. run test cases on Android
   testkit-lite -f [testprefix-path]/opt/apptools-manifest-tests/tests.xml -A -o [testprefix-path]/opt/apptools-manifest-tests/result.xml --comm androidmobile --deviceid=Medfield3C6DFF2E --testprefix=[testprefix-path]
  DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
  Query device id by command "adb devices -l" in host.

4. run test cases on Windows
   testkit-lite -f [testprefix-path]/opt/apptools-manifest-tests/tests.xml -A -o [testprefix-path]/opt/apptools-manifest-tests/result.xml --comm localhost --testprefix=[testprefix-path] --non-active

5. run test cases on Deepin
   testkit-lite -f $PWD/tests.xml -A --comm deepin --testprefix $PWD/../../ -o $PWD/result.xml

6. run test cases on iOS
   testkit-lite -f [testprefix-path]/opt/apptools-manifest-tests/tests.xml -A -o [testprefix-path]/opt/apptools-manifest-tests/result.xml --comm localhost --testprefix=[testprefix-path]


## Authors

* Yun, Liu<yunx.liu@intel.com>


## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
