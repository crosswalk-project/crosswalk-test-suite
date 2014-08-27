## Introduction

This sample demostrates the basic useage of standard APIs that are supported by Crosswalk.
Please refer to the API spec details to https://crosswalk-project.org/#documentation/apis/web_apis

## Authors:

* Lin, Wanming <wanmingx.lin@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.  All rights reserved.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the LICENSE.BSD-3 file for the BSD-3-Clause License.

## Deploy tinyweb

1. Deploy tinyweb on Tizen

  Make binaries for tinyweb from source code in Github
  $ git clone git@github.com:testkit/tinyweb.git
  $ cd tinyweb && make
  Note: The generated tinyweb type depends on your OS system type (32/64 bit).

  Deploy binaries to TIZEN device
  $ sdb shell "mkdir -p /opt/usr/media/tct/"
  $ sdb push tinyweb /opt/home/developer/
  $ sdb shell "chmod a+x /opt/home/developer/tinyweb"
  $ sdb push cgi-getcookie /opt/home/developer/
  $ sdb shell "chmod a+x /opt/home/developer/cgi-getcookie"
  $ sdb push cgi-getfield /opt/home/developer/
  $ sdb shell "chmod a+x /opt/home/developer/cgi-getfield"
  $ sdb push server.pem /opt/home/developer/
  $ sdb shell "chmod 666 /opt/home/developer/server.pem"
  $ sdb shell "ln -s /usr/lib/libssl.so.1.0.0 /opt/home/developer/libssl.so"
  $ sdb shell "ln -s /usr/lib/libcrypto.so.1.0.0 /opt/home/developer/libcrypto.so"

  Launch tinyweb
  $ DPATH=`sdb shell "printenv PATH"`
  $ timeout 5 sdb shell "env LD_LIBRARY_PATH=/opt/home/developer
  PATH=$DPATH:/opt/home/developer tinyweb -ssl_certificate
  /opt/home/developer/server.pem -document_root /opt/usr/media/tct/ -
  listening_ports 80,8080,8081,8082,8083,8443s; sleep 3s"

2. Deploy tinyweb on Android

  Make binaries for tinyweb from source code in Github
  $ git clone git@github.com:testkit/tinyweb.git
  $ cd tinyweb/android/native/jni/ && /path/to/android-ndk-<version>/ndk-build

  Copy tinyweb/android/native/libs/ to folder tinyweb/android/assets/system/libs/
  For example:
  $ cp -r /path/to/tinyweb/android/native/libs/ /path/to/tinyweb/android/assets/system/libs/

  Import project tinyweb to Android developer Tool by location tinyweb /android

  Export the android project to APK and install APK to android device
  $ adb install /path/to/tinyweb/bin/TinywebTestService.apk

  Launch tinyweb by clicking the tinyweb app icon in launcher

## Deploy DLNA server on tizen ivi device

  * Set up dlna server follow the steps:
  1. Modify rygel.conf on IVI device.
  $ cp /etc/rygel.conf /home/app/.config/

  - video-upload-folder=@VIDEOS@
  + video-upload-folder=/home/app/Videos

  - music-upload-folder=@MUSIC@
  + music-upload-folder=/home/app/Sounds

  - picture-upload-folder=@PICTURES@
  + picture-upload-folder=/home/app/Images

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
  + uris=/home/app/Videos;/home/app/Sounds;/home/app/Images;
 
  enabled=true
  - title=My Media
  + title=iLMS

  enabled=true
  - title=Audio/Video playback on @HOSTNAME@
  + title=iPlaybin

  2. Create Videos, Sounds and Images directories in /home/app/ on IVI device.

  3. Add some media content to IVI device.
  * Copy media files to /home/app/Videos, /home/app/Sounds and /home/app/Images.

  4. Launch of services on IVI device.
  $ su - app
  $ rygel
