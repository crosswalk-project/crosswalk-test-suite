# Geolocation API Test Suite

## Introduction

This test suite is for checking compliance with Geolocation API specification:
* http://www.w3.org/TR/2013/REC-geolocation-API-20131024/

## Pre-conditions

* Enable GPS or connect to an available network.
* Allow the user agent to access the device's location.
* Make configure:
```sh
sudo vconftool set -t int db/location/replay/ReplayEnabled 1 -f
```

## Authors

* Lin, Wanming <wanmingx.lin@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
