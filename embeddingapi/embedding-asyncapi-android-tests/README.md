## Introduction

This test suite is for the unit tests of Embedding API crosswalk module with XWalkView asynchronous initialization method.

## Pre-conditions

* Require Android API level 21
* For ant build: Please make sure copy the downloaded crosswalk-webview-xxxx to crosswalk-test-suite/tools directory, then rename it to /crosswalk-webview folder.
* For gradle build and maven build: Need to configure the crosswalk version in crosswalk-test-suite/VERSION file

## Environment

1. Install android sdk

    ```
    unzip adt-bundle-linux-x86-20130917.zip 
    gedit ~/.bashrc 
    export PATH=/home/api/ADT/adt-bundle-linux-x86-20130917/sdk:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/tools:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/platform-tools:$PATH
    ```

2. Install ant

    ```
    sudo apt-get install ant
    ```

3. Install jdk

4. Install Gradle(gradle-2.3 is known work)

5. Install Maven(apache-maven-3.2.5 is known work)

6. Install Maven Android SDK Deployer

7. Install Maven Android Plugin

## Authors:

* Yang, YunlongX <yunlongx.yang@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
