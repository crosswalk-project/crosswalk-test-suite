# Tizen Messaging API Test Suite

## Introduction

This test suite is for checking compliance with Tizen Messaging API
specifications (e-mail part):
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/messaging.html

## Pre-conditions

* There MUST be established Network connection for sending and receiving email
tests (preferably through WiFi as it has smaller delays on connection)

* Add an account through `Settings` application (Settings -> Personal/Accounts)
  * Click "Add"
  * Select type of account: Email
  * Enter e-mail address and password (preferably Gmail account)
  * Click "Next" - configuration will be verified and stored

* There MUST be several email messages in your mailbox to be used for
searching and removing messages tests

* Before testing, you MUST change some variables defined in
`Messaging/support/messaging_common.js` for message recipients.

Assign proper values to following variables:

  * `TEST_EMAIL_RECIPIENT_1`      MUST be set to email address of the account
    configured on the device on which the tests will be run
  * `TEST_EMAIL_RECIPIENT_2`      MUST be set to email address, different from
    `TEST_EMAIL_RECIPIENT_1`.

* There MUST be exactly one email service configured on the device.

## Authors

* Zou, Zoe <yananx.xu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
