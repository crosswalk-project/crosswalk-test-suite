## Introduction

This test is for the tests of Crosswalk Windows extensions using .Net.


## Pre-conditions

* Require Microsoft Visual Studio 2013
* Require Crosswalk windows binary


## Build an extension

1. Build the https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/usecase/usecase-extension-windows-tests/xwalk-echo-extension source code to a dll file using Microsoft Visual Studio 2013
2. Copy the extension dll file to ./extension/echo_extension/ and rename it to "echo_extension.dll"
3. Copy the xwalk_dotnet_bridge.dll from Crosswalk windows binary to ./extension/echo_extension_bridge/ and rename it to "echo_extension_bridge.dll"


## Authors:

* Liu,Yun <yunx.liu@intel.com>


## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
