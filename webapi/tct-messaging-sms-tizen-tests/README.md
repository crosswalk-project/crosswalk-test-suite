# Tizen Messaging API Test Suite

## Introduction

This test suite is for checking compliance with Tizen Messaging API
specification (SMS part):
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/messaging.html

## Pre-conditions

* A SIM card MUST be inserted for sending SMS messages.

* Before testing, you MUST change some variables defined in
`Messaging/support/messaging_common.js` for message recipients.

Here are the variables to be modified:

  * `TEST_SMS_RECIPIENT`  MUST be set to phone number, different from
    the device under test and without country calling code.
  * `TEST_SMS_RECIPIENT_2`  MUST be set to phone number, different from
    the device under test, different from TEST_SMS_RECIPIENT and without
    country calling code.

## Authors

* Zou, Zoe <yananx.xu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
