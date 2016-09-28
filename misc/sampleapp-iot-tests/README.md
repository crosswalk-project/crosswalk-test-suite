## Introduction

This test suite is for testing sampleapp-iot-tests specification

## Precondition

1. git clone https://github.com/crosswalk-project/crosswalk-samples.git /opt/crosswalk-samples

2. git clone https://github.com/crosswalk-project/crosswalk-demos.git /opt/crosswalk-demos
   mv /opt/crosswalk-demos/HangOnMan/manifest.json /opt/crosswalk-demos/HangOnMan/src
   cp -a /opt/crosswalk-demos/HangOnMan /opt/crosswalk-samples/
   mv /opt/crosswalk-demos/MemoryGame/manifest.json /opt/crosswalk-demos/MemoryGame/src
   cp -a /opt/crosswalk-demos/MemoryGame /opt/crosswalk-samples/

3. git clone https://github.com/BKcore/HexGL.git /opt/crosswalk-samples/HexGL
   echo -e '{ "name": "HexGL", \n "start_url": "index.html"}' > /opt/crosswalk-samples/HexGL/manifest.json

## Test Step

1. unzip sampleapp-iot-tests<version>.iot.zip -d [testprefix-path]

2. cd [testprefix-path]/opt/sampleapp-iot-tests/sampleapp-iot-tests

3. run test case

   xwalk --no-sandbox manifest.json

## Authors:

* Jiang, Xiuqi <xiuqix.jiang@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
