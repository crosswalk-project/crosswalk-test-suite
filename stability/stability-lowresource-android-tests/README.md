## Introduction

This test suite is for testing stability-lowresource-android-tests specification

## Authors:

* Li, Hao <haox.li@intel.com>

## Pre-condition
- TestAppRepeatedlyInLowMemory
  1. Enable root user in test device
  2. Access root user of test device by adb:
     $ adb shell
     $ su
  3. Get free memory size:
     # cat /proc/meminfo |grep "MemFree:"
  4. Cost the free memory:
     # mkdir /data/memory
     # mount -t tmpfs -o size={MemFree Size}M tmpfs /data/memory  (MemFree Size is the num in 3rd step, Unit: M(egabits))
     # dd if=/dev/zero of=/data/memory/block
     # sleep 3600  (keep the low memory for 1 hour)
  5. Check free memory in low status


After complete the testing, we need release the memory:
     # rm /data/data/block
     # umount /data/memory
     # rmdir /data/memory

- TestAppRepeatedlyInLowDisk
  1. Download crosswalk from https://crosswalk-project.org/documentation/downloads.html
  2. Unzip it to /path/to/opt/
  3. Make sure test envrionment can build apk successfully:
     $ python /path/to/opt/crosswalk/make_apk.py --package=org.xwalk.helloworld
       --name=helloworld --app-url=www.baidu.com

- TestAppRepeatedlyInLowBattery
  1. Cost the battery level of test device to less than 20%

Note: To make test result more correctly, suggest to run them one by one using "--id"
      after deploy each pre-condition.

 

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
