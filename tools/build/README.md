## Introduction

pack_cordova_sample.py is used for auto build Cordova sample apps, including mobilespec, helloworld, remotedebugging, gallery, and support both Cordova 3.6 and Cordova 4.0 build.  
**Note**: mobilespec build based on Cordova 4.0 is not in scope currently.

## Pre-conditions

###mobilespec build based on Cordova 4.0
* Require Android API level 22
* Require the latest Cordova CLI, and must >= 5.0.0, install with command: ```sudo npm install cordova -g```  
* Copy 'mobilespec' suite to crosswalk-test-suite/tools/mobilespec
* Copy 'cordova-mobile-spec' suite(https://github.com/apache/cordova-mobile-spec.git) to crosswalk-test-suite/tools/mobilespec
* Copy 'cordova-coho' suite(https://github.com/apache/cordova-coho.git) to crosswalk-test-suite/tools/mobilespec

###mobilespec build based on Cordova 3.6
* Build upstream Cordova with Mobile Spec 3.6, steps please follow [https://github.com/apache/cordova-mobile-spec/blob/3.6.x/createmobilespec/README.md](https://github.com/apache/cordova-mobile-spec/blob/3.6.x/createmobilespec/README.md), here will generate a 'mobilespec' folder
* Copy 'mobilespec' folder to crosswalk-test-suite/tools
* You may need to install latest cordova by ```sudo npm -g install cordova```  

###CIRC and Eh build based on Cordova 4.0
* Require the support repository downloaded into your android SDK  
**Steps**: 1. Open the SDK manager (from command line, type "android"); 2. Under "Extras", Make sure you have "Android Support Repository" and "Google Repository" downloaded 
* Require cca 0.7.0, install with command: ```sudo npm install cca@0.7.0 -g```  
* Clone https://github.com/flackr/circ to crosswalk-test-suite/tools
* Clone https://github.com/MobileChromeApps/workshop-cca-eh to crosswalk-test-suite/tools

###Sample apps build based on Cordova 4.0
* Require Android API level 22
* Require the latest Cordova CLI, and must >= 5.0.0, install with command: ```sudo npm install cordova -g```

## Usage

* ```./pack_cordova_sample.py -n <pkg-name> --cordova-version <cordova-version> [-m <pkg-mode>] [-a <pkg-arch>] [--tools=<tools-path>]```  
**pkg-name**: mobilespec, helloworld, remotedebugging, gallery, CIRC  
**cordova-version**: 3.6, 4.0  
**pkg-mode**: embedded(default), shared  
**pkg-arch**: arm(default), x86  
**Note**: -a argument is only for cordova version 4.0, if no --tools argument, please run script under the path where it is.

## Authors:

* Lin, Wanming <wanming.lin@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
