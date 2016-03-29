## Introduction

The test suite embeddingapi-silentdownload & embeddingapi-silentdownload-lzma is for testing CrossWalk Silent Download mode. This CrossWalk Silent Download Mode only works on the shared mode. So you can test the feature when you pack apk with shared mode. Related Bug is XWALK-5214, XWALK-5121, XWALK-5591, XWALK-5681

## Pre-conditions

* You need update the XWalkRuntimeLib.apk and XWalkRuntimeLibLzma.apk manually to your server.
* Modify the AndroidManifest.xml key 'xwalk_apk_url' value to your server apk address.
* The apk's version needs to keep consistent with the xwalk_shared_library version when you pack the project.


## Authors:

* Yang, YunlongX <yunlongx.yang@intel.com>


## LICENSE

Copyright (c) 2014 Intel Corporation.<br/>
Except as noted, this software is licensed under BSD-3-Clause License.<br/>
Please see the COPYING file for the BSD-3-Clause License.
