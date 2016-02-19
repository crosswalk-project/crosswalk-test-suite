# Cordova Test Suite User Guide

## Introduction

This document provides method to run Crosswalk based Cordova test suite. Currently the target platform is Android only. You can use the following method to run it with testkit-lite. Testkit tool-chain includes 3 components:

- testkit-lite:  a command-line interface application deployed on Host
- testkit-stub: a test stub application deployed on Device
- tinyweb:  a web service application deployed on Device

## Cordova Web Testing Architecture

- Cordova Web Testing on Android

![Behavior Test Tool Home Page](img/Cordova_Test_Suite_User_Guide_1.png)

There are two types of Webapi tests:

- Web service dependent

Client side is a stub test package which link to remote web runner, no local TCs and web runner, thus avoid cross origin issue.

Server side includes tinyweb, webrunner and TCs.

- Web service independent

Self contained test package which include all things - web runner, TCs.

## Install testkit-lite on Host

- Deploy testkit-lite

  - Install dependency python-requests (version>1.0)

        ```
        $ sudo apt-get install python-pip

        $ sudo pip install requests
        ```

  - Install testkit-lite from source code in GitHub

        ```
        $ git clone https://github.com/testkit/testkit-lite

        $ cd testkit-lite

        $ sudo python setup.py install
        ```

## Crosswalk based Cordova System Requirements

- Java JDK 1.5 or greater [http://www.oracle.com/technetwork/java/javase/downloads/index.html](http://www.oracle.com/technetwork/java/javase/downloads/index.html).
- Apache ANT 1.8.0 or greater [http://ant.apache.org/bindownload.cgi](http://ant.apache.org/bindownload.cgi).
- Android SDK  [http://developer.android.com](http://developer.android.com).
- Python 2.7 or greater  [https://www.python.org/download/](https://www.python.org/download/).
- Node.js 0.10.24 or greater  [http://nodejs.org/download/](http://nodejs.org/download/).
- Require npm  [https://www.npmjs.com/package/npm](https://www.npmjs.com/package/npm).
- Require maven tool, you may need to set up maven proxy:  
  ```export MAVEN_OPTS="-DsocksProxyHost=[proxy] –DsocksProxyPort=[port]```
- Require Android API level 22.

## Install Crosswalk Canary aar
If you run the cordova test suite with Crosswalk Canary version, you need to download and install the Crosswalk Canary aar to the local maven repo:
- For embedded mode 32-bit Crosswalk:
  - Download Crosswalk Canary aar:  
    ```$ wget https://download.01.org/Crosswalk/releases/Crosswalk/android/Canary/<Canary-version>/crosswalk-<Canary-version>.aar```
  - Install Crosswalk Canary aar:  
    ```$ mvn install:install-file -DgroupId=org.xwalk -DartifactId=xwalk_core_library -Dversion=<Canary-version> -Dpackaging=aar -Dfile=<Crosswalk-path>/crosswalk-<Canary-version>.aar -DgeneratePom=true```

- For embedded mode 64-bit Crosswalk:
  - Download Crosswalk Canary aar:  
    ```$ wget https://download.01.org/Crosswalk/releases/Crosswalk/android/Canary/<Canary-version>/crosswalk-<Canary-version>-64bit.aar```
  - Install Crosswalk Canary aar:  
    ```$ mvn install:install-file -DgroupId=org.xwalk -DartifactId=xwalk_core_library -Dversion=<Canary-version> -Dpackaging=aar -Dfile=<Crosswalk-path>/crosswalk-<Canary-version>-64bit.aar -DgeneratePom=true -Dclassifier=64bit```

- For shared mode Crosswalk:
  - Download Crosswalk Canary aar:  
    ```$ wget https://download.01.org/Crosswalk/releases/Crosswalk/android/Canary/<Canary-version>/crosswalk-shared-<Canary-version>.aar```
  - Install Crosswalk Canary aar:  
    ```$ mvn install:install-file -DgroupId=org.xwalk -DartifactId=xwalk_shared_library -Dversion=<Canary-version> -Dpackaging=aar -Dfile=<Crosswalk-path>/crosswalk-shared-<Canary-version>.aar -DgeneratePom=true```

Notes:
- Canary-version: the version of Crosswalk Canary, e.g. 18.46.472.0.
- Crosswalk-path: the downloaded Crosswalk Canary file path.

## Install Cordova Test Suite

```
$ unzip <package-name>-<version>.zip

$ cd opt/<test-suite>

$ ./inst.py
```

## Run Test
### Cordova Features and Sample Apps
There are two types(js, pyunit) of test cases in Cordova test suites.
- js tests:

  ```$ testkit-lite -f /path/to/tests.xml --e XWalkLauncher -comm androidmobile -o /path/to/result.xml```

- pyunit tests:
  - Get cordova_sampleapp.zip from internal release link, then unzip it to /tmp/cordova-sampleapp/
  - Update opt/&lt;test-suite>/arch.txt if your run with 'x86' device
  - Update opt/&lt;test-suite>/mode.txt if your run with 'shared' mode pkg
  - Run the cordova cases:

    ```
    $ testkit-lite -f [testprefix-path]/opt/cordova-feature-android-tests/tests.xml -A
     -o [testprefix-path]/opt/cordova-feature-android-tests/result.xml --comm localhost
     --testenvs "DEVICE_ID=Medfield3C6DFF2E;CONNECT_TYPE=adb" --testprefix=[testprefix-path]
    ```
Notes:
  - More environment requirements are documented in opt/&lt;test-suite>/README.md.
  - DEVICE_ID can also be multiple ids like "DEVICE_ID=Medfield3C6DFF2E,Medfield3C6DFF00".
  - Query device id by command "adb devices -l" in host.

### Cordova API
  - [Cordova Mobile Spec](https://github.com/apache/cordova-mobile-spec), is a set of automated & manual tests that test Cordova core functionality, we leverage it by adding Crosswalk WebView plugin in Mobile Spec for Cordova API testing. You need to get the "mobilespec.apk", install and run it following the instruction contained in the app, and then collect the result manually.

