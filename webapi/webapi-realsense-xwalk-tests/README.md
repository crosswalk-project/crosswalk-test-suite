# RealSense Test Suite

## Introduction

This test suite is for checking RealSense support in Crosswalk Project:
* https://crosswalk-project.github.io/realsense-extensions-crosswalk/spec/depth-enabled-photography.html
* https://crosswalk-project.github.io/realsense-extensions-crosswalk/spec/scene-perception.html
* https://crosswalk-project.github.io/realsense-extensions-crosswalk/spec/face.html

## Pre-Condition

1. Hardware Requirements:

   - 4th Generation Intel Core Processor, or later. Core i5/7 recommended

   - 8GB free hard disk space

   - The Intel RealSense Camera

2. Software Requirements:

   - Win 8.1 x64 or Win 10

3. Setup the build environment

  Please refer [Web_Test_Suite_Packaging_Guide](https://github.com/crosswalk-project/crosswalk-test-suite/blob/master/doc/Web_Test_Suite_Packaging_Guide.md)
  for Windows part.

   Please make sure Crosswalk Project for Windows is 18.48.475.0 or later, the version of
   crosswalk-app-tools is above 0.10.0:
   
   ```bat
   crosswalk-pkg -v
   ```

4. Install [R200 DCM](https://downloadmirror.intel.com/25044/eng/intel_rs_dcm_r200_2.1.24.6664.exe).

5. Install [RSSDK runtime](http://registrationcenter-download.intel.com/akdlm/irc_nas/8516/intel_rs_sdk_runtime_8.0.24.6528.exe).

## Build for Windows

1. Download and unzip [latest realsense_extensions(.zip)](https://github.com/crosswalk-project/realsense-extensions-crosswalk/releases/download/v19.6.0/realsense_extensions_v19.6.0.zip).

   The content of realsense_extensions looks like:

        realsense_extensions/
        ├── enhanced_photography
        │   ├── enhanced_photography.dll
        │   └── XWalkExtensionHooks.js
        ├── face
        │   ├── face.dll
        │   └── XWalkExtensionHooks.js
        └── scene_perception
            ├── scene_perception.dll
            └── XWalkExtensionHooks.js

2. Copy all the sub directories of realsense_extensions to the realsense_extensions directory of
   webapi-realsense-xwalk-tests test suite.

3. Create MSI file as follows:

   ```bat
   python ..\..\tools\build\pack.py -t msi
   ```

## Authors

* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
