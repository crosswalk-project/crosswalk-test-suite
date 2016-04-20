## Introduction

This test suite is for testing Cordova Android and Windows App Security API specification:
* https://software.intel.com/en-us/app-security-api/api

## Pre-condition before pack this suite

For Cordova Android:

There are extra plugins needed for packing this suite:

Create extra_plugins directory in webapi-appsecurity-external-tests

Git clone https://github.com/AppSecurityApi/com-intel-security-cordova-plugin in extra_plugins directory

For Windows:

Git clone https://github.com/AppSecurityApi/com-intel-security-crosswalk-extension to the current directory

## Pre-condition before testing

Require available network to access https://crosswalk-project.org

For Windows:

Need to install "Visual C++ Redistributable" for Visual Studio 2015 on the system.

## Note
To improve the compatibility of this test suite for Windows and Cordova Android, the case page code contains these code: 
```
<script src="../../../cordova.js"></script> 
<script src="js/appSecurityApi.js"></script>
<script src="js/q.js"></script>
```

The
```
<script src="../../../cordova.js"></script> 
```
is only for cordova android app, it's unuseful for windows app 

<br/>
The

```
<script src="js/appSecurityApi.js"></script>
<script src="js/q.js"></script>
```
is only for windows app, it's unuseful for cordova android app
, they can work on the corresponding platform.


## Authors:

* Zhu, YongyongX <yongyongx.zhu@intel.com>


## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
