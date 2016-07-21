# RealSense Test Suite

## Introduction

This test suite is for checking TwoInOne support in Crosswalk Project:
* https://github.com/crosswalk-project/crosswalk-extensions-twoinone/blob/master/twoinone-windows/XWalkExtensionApi.js
* JIRA Ticket: https://crosswalk-project.org/jira/browse/XWALK-5711

## Build for Windows

1. Create MSI file as follows:

   ```bat
   python ..\..\tools\build\pack.py -t msi --pkg-version xx.xx.xxx.x
   ```

## Authors

* Hao, Yunfei <yunfei.hao@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
