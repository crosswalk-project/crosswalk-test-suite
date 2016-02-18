## Introduction

pack_cordova_sample.py is used for auto build Cordova sample apps, including mobilespec, helloworld, remotedebugging, spacedodge, renamePkg, setBackgroundColor, xwalkCommandLine, privateNotes, setUserAgent, LoadExtension.
**Note**: Need to configure crosswalk version in crosswalk-test-suite/VERSION file

## Pre-conditions

###spacedodge build
* Clone https://github.com/crosswalk-project/crosswalk-samples.git to crosswalk-test-suite/tools/

###privateNotes build
* Clone https://github.com/gomobile/sample-my-private-notes.git to crosswalk-test-suite/tools/

###mobilespec build
* Require Android API level 22
* Require the latest Cordova CLI, and must >= 5.0.0, install with command: ```sudo npm install cordova -g```  
* Copy 'cordova-mobile-spec' suite(https://github.com/apache/cordova-mobile-spec.git) to crosswalk-test-suite/tools/mobilespec
* Copy 'cordova-coho' suite(https://github.com/apache/cordova-coho.git) to crosswalk-test-suite/tools/mobilespec

###CIRC and Eh build
* Require the support repository downloaded into your android SDK  
**Steps**: 1. Open the SDK manager (from command line, type "android"); 2. Under "Extras", Make sure you have "Android Support Repository" and "Google Repository" downloaded 
* Require cca 0.7.0, install with command: ```sudo npm install cca@0.7.0 -g```  
* Clone https://github.com/flackr/circ to crosswalk-test-suite/tools
* Clone https://github.com/MobileChromeApps/workshop-cca-eh to crosswalk-test-suite/tools

###Sample apps build
* Require Android API level 22
* Require the latest Cordova CLI, and must >= 5.0.0, install with command: ```sudo npm install cordova -g```

## Usage

* ```./pack_cordova_sample.py -n <pkg-name> --cordova-version <cordova-version> [-m <pkg-mode>] [-a <pkg-arch>] [--tools=<tools-path>]```  
**pkg-name**: mobilespec, helloworld, remotedebugging, spacedodge, CIRC, statusbar, renamePkg, setBackgroundColor, xwalkCommandLine, privateNotes, setUserAgent, LoadExtension  
**pkg-mode**: embedded(default), shared  
**pkg-arch**: arm(default), x86, arm64, x86_64  
**Note**: if no --tools argument, please run script under the path where it is.

## Authors:

* Lin, Wanming <wanming.lin@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
