# EmbeddingAPI Test Suite Packaging Guide

Version 1.0

Copyright © 2014 Intel Corporation. All rights reserved. No portions of this document may be reproduced without the written permission of Intel Corporation.

Intel is a trademark of Intel Corporation in the U.S. and/or other countries.

Linux is a registered trademark of Linus Torvalds.

Tizen® is a registered trademark of The Linux Foundation.

ARM is a registered trademark of ARM Holdings Plc.

\*Other names and brands may be claimed as the property of others.

Any software source code reprinted in this document is furnished under a software license and may only be used or copied in accordance with the terms of that license.

## Overview

This document provides method to pack test suite packages for EmbeddingAPI. Currently the target platform is Android. Please use the following shell script to generate test suite packages.

- pack.sh:  a script for packing single test suite package

You are supposed to have gained the following knowledge:

- How to download and install JDK.
- How to download and install android SDK.

## Environment Setup

An Ubuntu (12.04) host is needed to pack the embeddingAPI test suites.

Set packaging environment for Android:

- Download and install Android SDK(>=android-19) for your platform from http://developer.android.com/sdk/index.html.

$unzip adt-bundle-linux-x86-20130917.zip

- Deploy Android SDK`s tools and platform-tools to PATH environment

$gedit ~/.bashrc

$ export PATH=/home/api/ADT/adt-bundle-linux-x86-20130917/sdk:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/tools:/home/api/ADT/adt-bundle-linux-x86-20130917/sdk/platform-tools:$PATH

- Install ant

$sudo apt-get install ant

- Install jdk


## Pack EmbeddingAPI Test Suite Packages

There is a pack.sh script in each test suite. Currently it supports a test suite package in the type of APK, in .zip, for Android platform.

- Download the latest crosss webview bundle from the following link:

[https://download.01.org/crosswalk/releases/crosswalk/android/beta/](https://download.01.org/crosswalk/releases/crosswalk/android/beta/)

- Copy crosswalk-webview-xxxx and rename it to /crosswalk-webview folder

- Download the embeddingapi test suit from the following link:

[https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/embeddingapi/webapi-embeddingapi-xwalk-tests](https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/embeddingapi/webapi-embeddingapi-xwalk-tests)

- Pack APK packages:

$ cd webapi-embeddingapi-xwalk-tests

$ ./pack.sh
