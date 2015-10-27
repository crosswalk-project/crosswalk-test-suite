## Introduction

This test suite is for testing wrt-maven-android-tests specification

## Envrionment

1. Install android sdk

   ```
   unzip adt-bundle-linux-x86-20130917.zip
   gedit ~/.bashrc
   export PATH=/home/api/ADT/adt-bundle-linux-x86-20130917/sdk:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/tools:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/platform-tools:$PATH
   ```

2. For ADT build, need to install ADT

3. Install ant

   ```
   sudo apt-get install ant
   ```

4. Install jdk

5. Require Android API level 21

6. Install Gradle(gradle-2.3 is known work)

7. Install Maven(apache-maven-3.2.5 is known work)

8. Install Maven Android SDK Deployer

9. Install Maven Android Plugin

## Test Steps

1. unzip embedding-build-android-tests-<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/embedding-build-android-tests/

3. update arch if your run with 'arm' device

4. update crosswalk-version to configure the crosswalk version

5. update crosswalk-type to configure the crosswalk version type(beta, stable, canary)

6. run test case

   ```
   testkit-lite -f [testprefix-path]/opt/embedding-build-android-tests/tests.xml -A
   -o [testprefix-path]/opt/embedding-build-android-tests/result.xml --comm localhost
   --testenvs "DEVICE_ID=Medfield3C6DFF2E;CONNECT_TYPE=adb" --testprefix=[testprefix-path]
   ```

   DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
   Query device id by command "adb devices -l" in host.

## Authors:

* Zhu,Yongyong <yongyongx.zhu@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
