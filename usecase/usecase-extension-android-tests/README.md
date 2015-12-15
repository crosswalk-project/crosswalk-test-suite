## Introduction

This test suite is for the tests of Crosswalk Android extensions using Java.
In this tutorial, you will build a Crosswalk Android application with a Java extension. This consists of two main pieces:

* A Crosswalk extension

  The extension consists of:
  1. Java source code: Standard Android/Java classes, packaged into a jar file.
  2. JavaScript wrapper or not: A JavaScript file which exposes the Java code to an app running on Crosswalk, or extension with auto-generating js-stub feature
  3. Configuration: A JSON file to wire up the JavaScript wrapper with the Java classes.

  Note that a Crosswalk application can use multiple extensions if desired.

* An HTML5 web application

  This is a self-contained web application which "lives inside" the Android application, but uses Crosswalk as its runtime. It consists of standard assets like HTML files, JavaScript files, images, fonts etc.
  The Crosswalk extension is invoked by code in the web application, via the JavaScript wrapper mentioned above.


## Pre-conditions

* Require Android API level 22
* Require Android SDK TOOLS
* For ant build & web build: Please make sure copy the downloaded crosswalk-xxxx to xwalk-xxxx-extension/libs directory, then move xwalk_core_library/libs/xwalk_core_library_java.jar to libs folder.


## Build an extension

user@host:~$ cd usecase-extension-android-tests/xwalk-echo-extension/
user@host:~$ android update project --target android-22 --path .
user@host:~$ ant release -Dandroid.library=true


## Build a web application

user@host:~$ mv bin/classes.jar echoextension/echoextension.jar
user@host:~$ cp echoextension.json js/echoextension.js echoextension/
user@host:~$ cd libs/crosswalk-xxxx
user@host:~$ python make_apk.py --fullscreen --enable-remote-debugging --manifest=/local/crosswalk_project/crosswalk-test-suite/usecase/usecase-extension-android-tests/xwalk-echo-app/manifest.json --extensions=/local/crosswalk_project/crosswalk-test-suite/usecase/usecase-extension-android-tests/xwalk-echo-extension/echoextension --package=org.crosswalkproject.sample


## Run on Android

user@host:~$ adb install -r Sample.apk


## Authors:

* Yang, YunlongX <yunlongx.yang@intel.com>


## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
