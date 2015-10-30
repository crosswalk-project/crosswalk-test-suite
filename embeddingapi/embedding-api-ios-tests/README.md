## Introduction

This test suite is for embedding-api-ios-tests
1. ./setUp_ios.py is download the project crosswal-ios from https://github.com/crosswalk-project/crosswalk-ios

## Precondition

1. Connect iOS devices to your localhost

## Run Test

1. unzip embedding-api-ios-tests<version>.zip -d [testprefix-path]

2. testkit-lite -f /path/tests.xml -A --comm localhost -e XWalkLauncher --testprefix=[testprefix-path]
--testenvs "IOS_PLATFORM=iOS Simulator;IOS_NAME=iPhone 6;IOS_VERSION=8.3" --non-active


## Authors:

* Wang, Hongjuan <hongjuanx.wang@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.


