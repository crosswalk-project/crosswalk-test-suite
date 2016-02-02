# Web Test Suite PackagingGuide

## 1. Overview

This document is intended for developers or testers who need to pack web test suites.

You are supposed to have gained the following knowledge:

- Where and how to download web test source code files.
- How to download and install android SDK.

## 2. EnvironmentSetup

An Ubuntu (12.04) host is needed to pack the web test suites.

- Install autoconf automake:

    $ sudo apt-get install autoconf automake

Set packaging environment for Tizen:

- Install python-dev:

    $ sudo apt-get install python-dev

- Download and install

    pycrypto([https://www.dlitz.net/software/pycrypto/](https://www.dlitz.net/software/pycrypto/))

The XPK tool make\_xpk.py is located in web test source code.

Set packaging environment for Android:

- Install ant nodejs:

    $ sudo apt-get install ant nodejs

- Download and install Android SDK(>=android-19) for your platform from [http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html).
- Deploy Android SDK`s tools and platform-tools to PATH environment

    $ export PATH=${PATH}:/path/to/adt-bundle-<version\>/sdk/platform-tools:/path/to/adb-bundle-/sdk/platform-tools

There are two tools to generate APK package, make\_apk.py and crosswalk-app-tools.

Before crosswalk-18.46.468.0, we use make\_apk.py:

- Get proper package of <version\>/crosswalk-<version\>.zip from [https://download.01.org/crosswalk/releases/crosswalk/android/canary/](https://download.01.org/crosswalk/releases/crosswalk/android/canary/).

    $ cd /path/to/crosswalk-test-suite/tools/

    $ unzip /path/to/crosswalk-<version\>.zip

    $ mv crosswalk-<version\>\* crosswalk/

From crosswalk-18.46.468.0, make\_apk.py had been removed, which means we use crosswalk-app-tools:

- Set a environment variable named CROSSWALK_APP_TOOLS_CACHE_DIR:

    export CROSSWALK_APP_TOOLS_CACHE_DIR=/custom/your/environment/path/

- Get proper package of <version\>/crosswalk-<version\>.zip from [https://download.01.org/crosswalk/releases/crosswalk/android/canary/](https://download.01.org/crosswalk/releases/crosswalk/android/canary/). And move the crosswalk zip file to CROSSWALK_APP_TOOLS_CACHE_DIR
    
    $ mv crosswalk-<version\>.zip ${CROSSWALK_APP_TOOLS_CACHE_DIR}


## 3. Pack Web Test Suite Packages

There is a pack.py script in crosswalk-test-suite/tools/build. Currently it supports 4 platforms: Android, Linux, Windows, iOS.

### 3.1  Pack Web Test Suite Packages for Android

Pack APK packages use pack.py

    $ ../../tools/build/pack.py –t apk –m embedded –a arm|x86

   Pack embedded mode APK package using pack.py. use –a arm or –a x86 to choose the right architecture.

    $ ../../tools/build/pack.py –t apk –m shared –a arm|x86

   Pack shared mode APK package using pack.py.

Please see the Appendix1 for the packages list.

Pack embedded mode APK package using pack.py. use –a arm or –a x86 to choose the right architecture.

Pack cordova packages use pack.py.

    $ ../../tools/build/pack.py –t cordova --cordova-version 4.x -m embedded -a arm|x86

Pack cordova sample apps package using pack.py.

    $ ../../tools/build/pack_cordova_sample.py -n APPNAME --cordova-version 4.x -m embedded -a arm|x86

Please see the Appendix 6 for the packages list and cordova sample app list.

### 3.2  Pack Web Test Suite Packages for Deepin Linux

    $ ../../tools/build/pack.py –t deb

Pack deb package.

Please see the Appendix 2 for the packages list.

### 3.3  Pack Web Test Suite Packages for Windows 8 & 10

    $ ../../tools/build/pack.py -t msi

Pack msi package.

Please see Appendix 2 for the package list

### 3.4  Pack Web Test Suite Packages for iOS

    $ ../../tools/build/pack.py -t ios

Pack iOS package for iOS.

Please see Appendix 5 for the package list.

## Appendix 1 APK Packages List

**WebAPI**

- tct-2dtransforms-css3-tests
- tct-3dtransforms-css3-tests
- tct-animations-css3-tests
- tct-animationtiming-w3c-tests
- tct-appcache-html5-tests
- tct-audio-html5-tests
- tct-backgrounds-css3-tests
- tct-batterystatus-w3c-tests
- tct-browserstate-html5-tests
- tct-canvas-html5-tests
- tct-capability-tests
- tct-colors-css3-tests
- tct-cors-w3c-tests
- tct-csp-w3c-tests
- tct-deviceorientation-w3c-tests
- tct-dnd-html5-tests
- tct-extra-html5-tests
- tct-fileapi-w3c-tests
- tct-filesystemapi-w3c-tests
- tct-filewriterapi-w3c-tests
- tct-flexiblebox-css3-tests
- tct-fonts-css3-tests
- tct-forms-html5-tests
- tct-fullscreen-nonw3c-tests
- tct-geoallow-w3c-tests
- tct-geodeny-w3c-tests
- tct-gumallow-w3c-tests
- tct-indexeddb-w3c-tests
- tct-jsenhance-html5-tests
- tct-mediacapture-w3c-tests
- tct-mediaqueries-css3-tests
- tct-multicolumn-css3-tests
- tct-navigationtiming-w3c-tests
- tct-netinfo-w3c-tests
- tct-notification-w3c-tests
- tct-pagevisibility-w3c-tests
- tct-sandbox-html5-tests
- tct-screenorientation-w3c-tests
- tct-security-tcs-tests
- tct-selectorslevel1-w3c-tests
- tct-selectorslevel2-w3c-tests
- tct-sessionhistory-html5-tests
- tct-sse-w3c-tests
- tct-svg-html5-tests
- tct-text-css3-tests
- tct-touchevent-w3c-tests
- tct-transitions-css3-tests
- tct-typedarrays-nonw3c-tests
- tct-ui-css3-tests
- tct-vibration-w3c-tests
- tct-video-html5-tests
- tct-webaudio-w3c-tests
- tct-webdatabase-w3c-tests
- tct-webgl-nonw3c-tests
- tct-webmessaging-w3c-tests
- tct-websocket-w3c-tests
- tct-webstorage-w3c-tests
- tct-workers-w3c-tests
- tct-xmlhttprequest-w3c-tests
- webapi-appuri-w3c-tests
- webapi-deviceadaptation-css3-tests
- webapi-devicecapabilities-w3c-tests
- webapi-dlna-ivi-tests
- webapi-hrtime-w3c-tests
- webapi-input-html5-tests
- webapi-locale-ivi-tests
- webapi-messageport-ivi-tests
- webapi-notification-ivi-tests
- webapi-presentation-w3c-tests
- webapi-promises-nonw3c-tests
- webapi-rawsockets-w3c-tests
- webapi-resourcetiming-w3c-tests
- webapi-simd-nonw3c-tests
- webapi-speechapi-ivi-tests
- webapi-usertiming-w3c-tests
- webapi-vehicleinfo-ivi-tests
- webapi-webrtc-w3c-tests
- webapi-webspeech-w3c-tests

**WRT**

- wrt-common-webapp-tests
- wrt-extension-android-tests
- wrt-integration-android-tests
- wrt-packagemgt-android-tests
- wrt-packertool-android-tests
- wrt-rtcore-android-tests
- wrt-rtlib-android-tests
- sampleapp-android-tests
- wrt-security-android-tests
- wrt-webappmgt-android-tests
- wrt-webfeatures-android-tests

**Behavior**

- tct-behavior-tests

**Cordova**

- cordova-appsecurityapi-android-tests
- cordova-feature-android-tests
- cordova-sampleapp-android-tests
- cordova-webapp-android-tests

**Misc**

- web-mbat-xwalk-tests
- stability-iterative-android-tests
- web-abat-xwalk-tests
- wrt-stabiterative-android-tests
- wrt-stablonglast2D-android-tests
- wrt-stablonglast3D-android-tests
- wrt-stablonglastplayvideo-android-tests
- wrt-stabrecovery-android-tests

## Appendix 2 XPK Package List

**WebAPI**

- tct-2dtransforms-css3-tests
- tct-3dtransforms-css3-tests
- tct-animations-css3-tests
- tct-animationtiming-w3c-tests
- tct-appcache-html5-tests
- tct-application-tizen-tests
- tct-audio-html5-tests
- tct-backgrounds-css3-tests
- tct-batterystatus-w3c-tests
- tct-bluetooth-tizen-tests
- tct-bookmark-tizen-tests
- tct-browserstate-html5-tests
- tct-callhistory-tizen-tests
- tct-canvas-html5-tests
- tct-capability-tests
- tct-colors-css3-tests
- tct-content-tizen-tests
- tct-cors-w3c-tests
- tct-csp-w3c-tests
- tct-datasync-tizen-tests
- tct-deviceorientation-w3c-tests
- tct-dnd-html5-tests
- tct-download-tizen-tests
- tct-extra-html5-tests
- tct-fileapi-w3c-tests
- tct-filesystemapi-w3c-tests
- tct-filesystem-tizen-tests
- tct-filewriterapi-w3c-tests
- tct-flexiblebox-css3-tests
- tct-fonts-css3-tests
- tct-forms-html5-tests
- tct-fullscreen-nonw3c-tests
- tct-geoallow-w3c-tests
- tct-geodeny-w3c-tests
- tct-getcapabilities
- tct-gumallow-w3c-tests
- tct-indexeddb-w3c-tests
- tct-jsenhance-html5-tests
- tct-mediacapture-w3c-tests
- tct-mediaqueries-css3-tests
- tct-messageport-tizen-tests
- tct-multicolumn-css3-tests
- tct-namespace-tizen-tests
- tct-navigationtiming-w3c-tests
- tct-netinfo-w3c-tests
- tct-networkbearerselection-tizen-tests
- tct-notification-tizen-tests
- tct-notification-w3c-tests
- tct-pagevisibility-w3c-tests
- tct-power-tizen-tests
- tct-privilege-tizen-tests
- tct-sandbox-html5-tests
- tct-screenorientation-w3c-tests
- tct-security-tcs-tests
- tct-selectorslevel1-w3c-tests
- tct-selectorslevel2-w3c-tests
- tct-sessionhistory-html5-tests
- tct-sse-w3c-tests
- tct-svg-html5-tests
- tct-systeminfo-tizen-tests
- tct-systemsetting-tizen-tests
- tct-testconfig
- tct-text-css3-tests
- tct-time-tizen-tests
- tct-touchevent-w3c-tests
- tct-transitions-css3-tests
- tct-typedarrays-nonw3c-tests
- tct-ui-css3-tests
- tct-vibration-w3c-tests
- tct-video-html5-tests
- tct-webaudio-w3c-tests
- tct-webdatabase-w3c-tests
- tct-webgl-nonw3c-tests
- tct-webmessaging-w3c-tests
- tct-websocket-w3c-tests
- tct-webstorage-w3c-tests
- tct-workers-w3c-tests
- tct-xmlhttprequest-w3c-tests
- webapi-appuri-w3c-tests
- webapi-deviceadaptation-css3-tests
- webapi-devicecapabilities-w3c-tests
- webapi-dlna-ivi-tests
- webapi-hrtime-w3c-tests
- webapi-input-html5-tests
- webapi-locale-ivi-tests
- webapi-messageport-ivi-tests
- webapi-notification-ivi-tests
- webapi-promises-nonw3c-tests
- webapi-rawsockets-w3c-tests
- webapi-resourcetiming-w3c-tests
- webapi-sanityapp-w3c-tests
- webapi-speechapi-ivi-tests
- webapi-usertiming-w3c-tests
- webapi-vehicleinfo-ivi-tests
- webapi-webrtc-w3c-tests
- webapi-webspeech-w3c-tests

**WRT**

- wrt-autodevice-tizen-tests
- wrt-common-webapp-tests
- wrt-integration-tizen-tests
- wrt-packagemgt-tizen-tests
- wrt-rtbin-tizen-tests
- wrt-rtcore-tizen-tests
- sampleapp-tizen-tests
- wrt-signature-tizen-tests
- wrt-webfeatures-tizen-tests

**Behavior**

- tct-behavior-tests

**Misc**

- web-mbat-xwalk-tests
- web-abat-xwalk-tests

## Appendix 3 WGT Package List for Tizen Mobile

**WebAPI**

- tct-2dtransforms-css3-tests
- tct-3dtransforms-css3-tests
- tct-alarm-tizen-tests
- tct-animations-css3-tests
- tct-animationtiming-w3c-tests
- tct-appcache-html5-tests
- tct-appcontrol-tizen-tests
- tct-application-tizen-tests
- tct-audio-html5-tests
- tct-backgrounds-css3-tests
- tct-batterystatus-w3c-tests
- tct-bluetooth-tizen-tests
- tct-bookmark-tizen-tests
- tct-browserstate-html5-tests
- tct-calendar-tizen-tests
- tct-callhistory-tizen-tests
- tct-canvas-html5-tests
- tct-capability-tests
- tct-colors-css3-tests
- tct-contact-tizen-tests
- tct-content-tizen-tests
- tct-cors-w3c-tests
- tct-csp-w3c-tests
- tct-datacontrol-tizen-tests
- tct-datasync-tizen-tests
- tct-deviceorientation-w3c-tests
- tct-dnd-html5-tests
- tct-download-tizen-tests
- tct-extra-html5-tests
- tct-fileapi-w3c-tests
- tct-filesystemapi-w3c-tests
- tct-filesystem-tizen-tests
- tct-filewriterapi-w3c-tests
- tct-flexiblebox-css3-tests
- tct-fonts-css3-tests
- tct-forms-html5-tests
- tct-fullscreen-nonw3c-tests
- tct-geoallow-w3c-tests
- tct-geodeny-w3c-tests
- tct-getcapabilities
- tct-gumallow-w3c-tests
- tct-indexeddb-w3c-tests
- tct-jsenhance-html5-tests
- tct-mediacapture-w3c-tests
- tct-mediaqueries-css3-tests
- tct-messageport-tizen-tests
- tct-messaging-email-tizen-tests
- tct-messaging-mms-tizen-tests
- tct-messaging-sms-tizen-tests
- tct-multicolumn-css3-tests
- tct-namespace-tizen-tests
- tct-navigationtiming-w3c-tests
- tct-netinfo-w3c-tests
- tct-networkbearerselection-tizen-tests
- tct-nfc-tizen-tests
- tct-notification-tizen-tests
- tct-notification-w3c-tests
- tct-package-tizen-tests
- tct-pagevisibility-w3c-tests
- tct-power-tizen-tests
- tct-privilege-tizen-tests
- tct-push-tizen-tests
- tct-sandbox-html5-tests
- tct-screenorientation-w3c-tests
- tct-secureelement-tizen-tests
- tct-security-tcs-tests
- tct-selectorslevel1-w3c-tests
- tct-selectorslevel2-w3c-tests
- tct-sessionhistory-html5-tests
- tct-sse-w3c-tests
- tct-svg-html5-tests
- tct-systeminfo-tizen-tests
- tct-systemsetting-tizen-tests
- tct-testconfig
- tct-text-css3-tests
- tct-time-tizen-tests
- tct-tizen-tizen-tests
- tct-touchevent-w3c-tests
- tct-transitions-css3-tests
- tct-typedarrays-nonw3c-tests
- tct-ui-css3-tests
- tct-vibration-w3c-tests
- tct-video-html5-tests
- tct-webaudio-w3c-tests
- tct-webdatabase-w3c-tests
- tct-webgl-nonw3c-tests
- tct-webmessaging-w3c-tests
- tct-websetting-tizen-tests
- tct-websocket-w3c-tests
- tct-webstorage-w3c-tests
- tct-workers-w3c-tests
- tct-xmlhttprequest-w3c-tests

**Behavior**

- tct-behavior-tests

## Appendix 4 WGT Package List for Tizen IVI

**WebAPI**

- tct-wgtapi01-w3c-tests
- tct-wgtapi02-w3c-tests
- tct-widget01-w3c-tests
- tct-widget02-w3c-tests
- tct-widgetpolicy-w3c-tests

**WRT**

- tct-appwgt-wrt-tests
- tct-ext01-wrt-tests
- tct-ext02-wrt-tests
- tct-pm-wrt-tests
- tct-rt01-wrt-tests
- tct-rt02-wrt-tests
- tct-sp01-wrt-tests
- tct-sp02-wrt-tests
- tct-stab-wrt-tests
- tct-ui01-wrt-tests

## Appendix 5 XPK Package List for Tizen IVI Generic

**MISC**

- web-mbat-xwalk-tests
- web-abat-xwalk-tests

## Appendix 6 Cordova APK Packages List and Cordova Sample App apk list

**WebAPI**

- tct-2dtransforms-css3-tests
- tct-3dtransforms-css3-tests
- tct-animations-css3-tests
- tct-animationtiming-w3c-tests
- tct-appcache-html5-tests
- tct-audio-html5-tests
- tct-backgrounds-css3-tests
- tct-batterystatus-w3c-tests
- tct-browserstate-html5-tests
- tct-canvas-html5-tests
- tct-capability-tests
- tct-colors-css3-tests
- tct-cors-w3c-tests
- tct-csp-w3c-tests
- tct-deviceorientation-w3c-tests
- tct-dnd-html5-tests
- tct-extra-html5-tests
- tct-fileapi-w3c-tests
- tct-filesystemapi-w3c-tests
- tct-filewriterapi-w3c-tests
- tct-flexiblebox-css3-tests
- tct-fonts-css3-tests
- tct-forms-html5-tests
- tct-fullscreen-nonw3c-tests
- tct-geoallow-w3c-tests
- tct-geodeny-w3c-tests
- tct-gumallow-w3c-tests
- tct-indexeddb-w3c-tests
- tct-jsenhance-html5-tests
- tct-mediacapture-w3c-tests
- tct-mediaqueries-css3-tests
- tct-multicolumn-css3-tests
- tct-navigationtiming-w3c-tests
- tct-netinfo-w3c-tests
- tct-notification-w3c-tests
- tct-pagevisibility-w3c-tests
- tct-sandbox-html5-tests
- tct-screenorientation-w3c-tests
- tct-security-tcs-tests
- tct-selectorslevel1-w3c-tests
- tct-selectorslevel2-w3c-tests
- tct-sessionhistory-html5-tests
- tct-sse-w3c-tests
- tct-svg-html5-tests
- tct-text-css3-tests
- tct-touchevent-w3c-tests
- tct-transitions-css3-tests
- tct-typedarrays-nonw3c-tests
- tct-ui-css3-tests
- tct-vibration-w3c-tests
- tct-video-html5-tests
- tct-webaudio-w3c-tests
- tct-webdatabase-w3c-tests
- tct-webgl-nonw3c-tests
- tct-webmessaging-w3c-tests
- tct-websocket-w3c-tests
- tct-webstorage-w3c-tests
- tct-workers-w3c-tests
- tct-xmlhttprequest-w3c-tests
- webapi-appuri-w3c-tests
- webapi-deviceadaptation-css3-tests
- webapi-devicecapabilities-w3c-tests
- webapi-dlna-ivi-tests
- webapi-hrtime-w3c-tests
- webapi-input-html5-tests
- webapi-locale-ivi-tests
- webapi-messageport-ivi-tests
- webapi-notification-ivi-tests
- webapi-presentation-w3c-tests
- webapi-promises-nonw3c-tests
- webapi-rawsockets-w3c-tests
- webapi-resourcetiming-w3c-tests
- webapi-simd-nonw3c-tests
- webapi-speechapi-ivi-tests
- webapi-usertiming-w3c-tests
- webapi-vehicleinfo-ivi-tests
- webapi-webrtc-w3c-tests
- webapi-webspeech-w3c-tests

**Cordova**

- cordova-appsecurityapi-android-tests
- cordova-feature-android-tests
- cordova-sampleapp-android-tests
- cordova-webapp-android-tests
- usecase-cordova-android-tests

**Cordova Sample Apps**

- CIRC
- Eh
- helloworld
- mobilespec
- privateNotes
- remotedebugging
- renamePkg
- setBackgroundColor
- spacedodge
- statusbar
- xwalkCommandLine
