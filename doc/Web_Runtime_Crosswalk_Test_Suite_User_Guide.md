# Web Runtime Crosswalk Test Suite User Guide

Version 1.0

Copyright © 2014 Intel Corporation. All rights reserved. No portions of this document may be reproduced without the written permission of Intel Corporation.

Intel is a trademark of Intel Corporation in the U.S. and/or other countries.

Linux is a registered trademark of Linus Torvalds.

Tizen® is a registered trademark of The Linux Foundation.

ARM is a registered trademark of ARM Holdings Plc.

\*Other names and brands may be claimed as the property of others.

Any software source code reprinted in this document is furnished under a software license and may only be used or copied in accordance with the terms of that license.

#1. Introduction

This document provides method to run WRT Crosswalk Test Suite on TIZEN. You can use the following method to run itwith testkit-lite. Testkit tool-chain includes 2 components:

- testkit-lite: a command-line interface application deployed on Host
- testkit-stub: a test stub application deployed on Device

#2. Install testkit-lite on Host

- Deploy testkit-lite

 - Install dependency python-requests (version>1.0)

        $ sudo apt-get install python-pip

        $ sudo pip install requests

 - Install testkit-lite from source code in GitHub

        $ git clone [git@github.com:testkit/testkit-lite.git](mailto:git@github.com:testkit/testkit-lite.git)

        $ cd testkit-lite && sudo python setup.py install
        
#3. Install Crosswalk

- Install crosswalk on Tizen

  - Download crosswalk from here

        https://download.01.org/crosswalk/releases/crosswalk/tizen-ivi/canary/<version\>/crosswalk-<version\>.i686.rpm

        https://download.01.org/crosswalk/releases/tizen-extensions-crosswalk/tizen-ivi/canary/<version\>/tizen-extensions-crosswalk-<version\>.i686.rpm

  - Deploy crosswalk to Tizen device

        $ sdb push crosswalk-<version\>.i686.rpm /home/app/content/tct

        $ sdb push tizen-extensions-crosswalk-<version\>.i686.rpm /home/app/content/tct

        $ sdb shell "rpm -ivh /home/app/content/tct/crosswalk-<version\>.i686.rpm"

        $ sdb shell "rpm -ivh /home/app/content/tct/tizen-extensions-crosswalk-<version\>.i686.rpm"


#4 Installation Web Runtime Crosswalk Test Suite

- Pack Web Runtime Crosswalk Test Suite:

    $ cd wrt-x-tizen-tests

    $ python ../../tools/build/pack.py -t wgt
    
- Launch WRT test with tct-mgr on Tizen device:

    $ cp  wrt-x-tizen-tests.version.wgt.zip /opt/tct/packages/
    
    $ tct-mgr to launch the test tool
    
    $ select the test suite and click 'Run' to start suite test

- Launch WRT test with lite on localhost:

    $ unzip wrt-x-tizen-tests.version.wgt.zip

    $ testkit-lite -f "/path/tests.xml" --comm localhost

#5. Viewing the Report

- tct-mgr: To generate the result XML at the specific location, click Export. You can view the summary information, including the case title and result.
- testkit-lite: You can use -o parameter to generate the report file. 
