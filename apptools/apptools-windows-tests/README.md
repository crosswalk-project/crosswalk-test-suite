## Introduction

This test suite is for apptools-windows-tests

1. ./allpairs.py is create pkgName.py and report directory for package name

## Precondition

1. The node.js, and git must be functional

2. Install WiX per https://msdn.microsoft.com/en-us/library/gg513936.aspx (do not forget to add the WiX tools to the windows path environment variable)

3. Download crosswalk-app-tools to apptools-windows-tests/tools, then install npm

  3.1 cd tools, then clone source code from https://github.com/crosswalk-project/crosswalk-app-tools

  3.2 Run commands: `cd crosswalk-app-tools`, then run: `npm install`

  3.3 Download Crosswalk windows binary to the same path with crosswalk-app-tools

4. Install nodeunit: `npm install nodeunit -g`

5. Install BeautifulSoup: `pip install BeautifulSoup`

6. Environment variable configuration:

   `export CROSSWALK_APP_TOOLS_CACHE_DIR=/path/to/opt/apptools-windows-tests/tools`

## Test Steps

1. unzip apptools-windows-tests<version>.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/apptools-windows-tests/

3. run test case

    testkit-lite -f [testprefix-path]/opt/apptools-windows-tests/tests.xml -A
    -o [testprefix-path]/opt/apptools-windows-tests/result.xml --comm localhost
    --testprefix=[testprefix-path] --non-active

## Authors:

* Yun, Liu<yunx.liu@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
