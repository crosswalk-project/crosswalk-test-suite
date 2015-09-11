# Tizen Bluetooth API Test Suite

## Introduction

This test suite is for checking compliance with Tizen Bluetooth API
specification:
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/bluetooth.html

## Pre-conditions

In order to run manual tests, you need an additional target, and
you MUST modify `REMOTE_DEVICE_ADDRESS`, `REMOTE_DEVICE_NAME` and
`REMOTE_HEALTH_DEVICE_TYPE` in `bluetooth/support/bluetooth_common.js`
before making RPM package.
* `REMOTE_DEVICE_ADDRESS`: Address of the device on which `tct-bt-helper` will be run.
* `REMOTE_DEVICE_NAME`: Name of the device on which `tct-bt-helper` will be run.
* `REMOTE_HEALTH_DEVICE_TYPE`: Type of health device 4100 is for oximeter or
blood pressure monitor 4103.

`tct-bt-helper` MUST be installed on the remote device whose address is
`REMOTE_DEVICE_ADDRESS`.

`tct-bt-helper` is included in the RPM package of this test. So,
you MUST install the RPM package both on the test device and the remote device.

In addition, the bluetooth of the remote device MUST be turned on and
discoverable from other devices. When you run the manual tests, you MUST
register a service to the remote device by pushing "Register service" button
on `tct-bt-helper`.

## Authors

* Lei, ZhanX <zhanx.lei@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
