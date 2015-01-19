## Introduction

This test suite is for wrt-manifest-android-tests

## Precondition

1. download and install allpairs
   http://sourceforge.net/projects/allpairs/files/allpairs/
2. Connect a Android device to your localhost
3. Edit your input_seed.txt(in ./allpairs/) file to generate webapp.
4. Need to edit the file "wrt-manifest-android-tests/arch.txt" according to the type of test device.
If test device is "x86" platform, content of the file should be "x86".

## Authors:

* Xu, Kang <kangx.xu@intel.com>
* Wang, Hongjuan <hongjuanx.wang@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

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

Test Step:
1. unzip -d [testprefix-path] wrt-manifest-android-tests<version>.zip
2. cd [testprefix-path]/opt/wrt-manifest-android-tests/
3. ./ge_package.py
4. run test case
   testkit-lite -f [testprefix-path]/opt/wrt-manifest-android-tests/tests.xml -A -o [testprefix-path]/opt/wrt-manifest-android-tests/result.xml --comm localhost --testenvs "DEVICE_ID=Medfield3C6DFF2E;CONNECT_TYPE=adb;APK_DIR=[apk-folder-path]" --testprefix=[testprefix-path],DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
Query device id by command "adb devices -l" in host.

Base on the seed file, the total case number is 266.
