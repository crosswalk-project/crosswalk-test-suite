## Introduction

This test suite is for testing Tizen Application API, which covers the following specifications:
* https://developer.tizen.org/help/topic/org.tizen.web.device.apireference/tizen/application.html

## Pre-conditions

* The following tests require the existence (and ready to installation) the file /home/TIZEN_USER/content/Others/TCTAppInfoEventTest1.wgt
(this file exist in tct-application-tizen-tests-<version>-<release>.<arch>.rpm and will be copied to /home/TIZEN_USER/content/Others during installation of test - the ApplicationId this application must be defined in app_common.js):
  ApplicationManager_addAppInfoEventListener_oninstalled
  ApplicationManager_addAppInfoEventListener_onuninstalled
  ApplicationManager_addAppInfoEventListener_onupdated
  ApplicationInformationEventCallback_oninstalled
  ApplicationInformationEventCallback_onuninstalled
  ApplicationInformationEventCallback_onupdated
* The following tests require the existence (and ready to installation) the file /home/TIZEN_USER/content/Others/TCTAppInfoEventTest2.wgt (the newer version of TCTAppInfoEventTest1.wgt)
(this file exist in tct-application-tizen-tests-<version>-<release>.<arch>.rpm and will be copied to /home/TIZEN_USER/content/Others during installation of test - the ApplicationId this application must be defined in app_common.js):
  ApplicationManager_addAppInfoEventListener_onupdated
  ApplicationInformationEventCallback_onupdated

## Special tests

* ApplicationManager_addAppInfoEventListener_oninstalled.html, ApplicationInformationEventCallback_oninstalled.html - manual tests
Make sure that TCTAppInfoEventTest1 application is not installed (uninstall it).
Click Run and install TCTAppInfoEventTest1.wgt application from My files app (Phone/Others directory).
* ApplicationManager_addAppInfoEventListener_onuninstalled.html, ApplicationInformationEventCallback_onuninstalled.html - manual tests
Make sure that TCTAppInfoEventTest1 application is installed (you can install it from My files app (Phone/Others directory)).
Click Run and uninstall TCTAppInfoEventTest1 application.
* ApplicationManager_addAppInfoEventListener_onupdated.html, ApplicationInformationEventCallback_onupdated.html - manual tests
Make sure that TCTAppInfoEventTest1 application is installed (you can install it from My files app (Phone/Others directory)).
Click Run and install TCTAppInfoEventTest2.wgt application from My files app (Phone/Others directory).

## Authors:

* Cao, Jenny <jenny.q.cao@intel.com>
* Mariusz Polasinski <m.polasinski@samsung.com>

## LICENSE

Copyright (c) 2013 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
