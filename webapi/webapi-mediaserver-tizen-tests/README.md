# Media Server API Test Suite

## Introduction

This test suite is for checking Media Server API support on Tizen platform:
* http://01org.github.io/cloud-dleyna/mediaserver.html

## Pre-conditions

Set up DLNS media server by the steps below:

* Modify `rygel.conf` on Tizen IVI device.

```sh
cp /etc/rygel.conf TESTER-HOME-DIR/apps_rw/
```

The diff looks like this:

```sh
- video-upload-folder=@VIDEOS@
+ video-upload-folder=TESTER-HOME-DIR/Videos

- music-upload-folder=@MUSIC@
+ music-upload-folder=TESTER-HOME-DIR/Sounds

- picture-upload-folder=@PICTURES@
+ picture-upload-folder=TESTER-HOME-DIR/Images

# Allow upload of media files?
- allow-upload=false
+ allow-upload=true

# Allow deletion of media folders and files?
- allow-deletion=false
+ allow-deletion=true

strict-sharing=false
- title=@REALNAME@'s media
+ title=iTracker

[MediaExport]
- enabled=false
- title=@REALNAME@'s media
+ enabled=true
+ title=iMediaExport

- uris=@MUSIC@;@VIDEOS@;@PICTURES@
+ uris=TESTER-HOME-DIR/Videos;TESTER-HOME-DIR/Sounds;TESTER-HOME-DIR/Images;
 
enabled=true
- title=My Media
+ title=iLMS

enabled=true
- title=Audio/Video playback on @HOSTNAME@
+ title=iPlaybin
```

* Create `Videos`, `Sounds` and `Images` directories in `TESTER-HOME-DIR/` on
the Tizen IVI device.

* Add some media clips to Tizen IVI device, for example, to
`TESTER-HOME-DIR/Videos`, `TESTER-HOME-DIR/Sounds` and `TESTER-HOME-DIR/Images`.

* Launch of services on Tizen IVI device.

```sh
su - app
rygel
```

## Authors

* Wang, Hongjuan <hongjuanx.wang@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.

