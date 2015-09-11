## Introduction

This test suite is for testing webappmanu-linux-tests specification

## Precondition
1. Need to remove the file "/usr/bin/xwalk"
2. Create shell script named 'xwalk.sh' in /usr/bin/:

   #!/bin/sh
   exec /opt/crosswalk-project/crosswalk --remote-debugging-port=12450 $1

3. Add executable permissions with "sudo chmod 755 /usr/bin/xwalk.sh"
4. Create new soft link with "sudo ln /usr/bin/xwalk.sh /usr/bin/xwalk

Details in https://crosswalk-project.org/jira/browse/XWALK-4721

## Authors:

* Yin,Haichao <haichaox.yin@intel.com>

## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
