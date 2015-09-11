# Vehicle Info and Vehicle Data API Test Suite

## Introduction

This test suite is for checking compliance with the Vehicle Info and Vehicle
Data API specifications:
* http://rawgit.com/w3c/automotive-bg/master/vehicle_spec.html
* http://rawgit.com/w3c/automotive-bg/master/data_spec.html

## Pre-Conditions

* Install bluemonkey plugin on Tizen IVI:

```sh
zypper in automotive-message-broker-plugins-bluemonkey
```

* Update configuration `/etc/ambd/config.tizen` on Tizen IVI: copying the
`mainloop` and `sources` sections from `/etc/ambd/examples/bluemonkeyconfig`
to `/etc/ambd/config.tizen`.

* Restart `ambd`:

```sh
systemctl restart ambd
```

For details, please refer to the
[AMB Bluemonkey Plugin](https://wiki.tizen.org/wiki/AMB_Bluemonkey_Plugin)
wiki page.

## Authors

* Xu, Kang <kangx.xu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
