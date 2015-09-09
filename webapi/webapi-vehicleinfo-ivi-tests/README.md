## Introduction

This test suite is for testing  Vehicle info and Vehicle data API:
* http://rawgit.com/w3c/automotive-bg/master/vehicle_spec.html
* http://rawgit.com/w3c/automotive-bg/master/data_spec.html

## Pre-Conditions
* Install Bluemonkey plugin in IVI:
  zypper in automotive-message-broker-plugins-bluemonkey

* Update configuration /etc/ambd/config.tizen in IVI:
  Copy 'mainloop' and 'sources' sections from /etc/ambd/examples/bluemonkeyconfig to /etc/ambd/config.tizen

* Restart ambd:
  systemctl restart ambd

 Details referring https://wiki.tizen.org/wiki/AMB_Bluemonkey_Plugin

## Authors:

* Xu, Kang <kangx.xu@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
