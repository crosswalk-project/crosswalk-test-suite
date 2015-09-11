# Tizen NFC API Test Suite

## Introduction

This test suite is for testing Tizen NFC API, which covers the following specifications:
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/nfc.html

## Pre-Conditions

Before executing tests please:
- enable NFC on the device
- allow the device to read some NFC tag (some tests uses cached message)
  You do that by touch the device with the tag.

During manual tests You are expected to either:
- touch the device with NFC tag (NFCAdapter_setTagListener*, NFCTag* tests)
- touch the device with different NFC enabled device (NFCAdapter_setPeerListener*, NFCPeer* tests)
- touch the device with different NFC enabled device and send NFC data from it

## Authors

* Han, GuangX <guangx.han@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
