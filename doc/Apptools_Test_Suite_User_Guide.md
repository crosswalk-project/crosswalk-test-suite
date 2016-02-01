# App-tools Test Suite User Guide

## Introduction

This document provides method to run App-tools test suite. Currently the target platforms are Android, iOS, Linux and Windows.

## Setup Environment

### Linux Host

1. Install Python, suggest version 2.7.6
1. Install Android SDK, JDK and git
1. Install [apache-ant-1.9.6](http://www.onlinedown.net/softdown/77637_2.htm)
1. Install node and npm, suggest node version 0.10.30 and npm version 1.4.21
1. Install [setuptools module](https://pypi.python.org/pypi/setuptools)
1. Install [webp conversion tool](http://downloads.webmproject.org/releases/webp)
1. Install BeautifulSoup: `$ sudo pip install BeautifulSoup`
1. Setup the environment variable for each path </br>
1) Set `JDK` and `Android SDK` env to "PATH" </br>
2) Set `ANT_HOME`, `ANDORID_HOME` and `CROSSWALK_APP_TOOLS_CACHE_DIR` env

### OS X Host

#### Android Testing

1. Install Python, suggest version 2.7.6
1. Install [Android SDK](http://www.androiddevtools.cn) for Mac, may be you need install [SDK tools](http://www.pan.baidu.com/s/1eQsHgI2)
1. Install [JDK(jdk-7u79-macosx-x64.dmg)](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html) for Mac
1. Install [apache-ant-1.9.6](http://www.onlinedown.net/softdown/77637_2.htm)
1. Install node and npm, suggest node version 0.10.30 and npm version 1.4.21
1. Install [brew](http://jingyan.baidu.com/article/335530da8b2b0419cb41c338.html) on Mac.you must agree to the license by opening Xcode.app or running
1. Install [webp conversion tool](http://downloads.webmproject.org/releases/webp)
1. Install BeautifulSoup: `$ pip install BeautifulSoup`
1. Setup the environment variable for each path </br>
1) Set `Android SDK` env to "PATH" </br>
2) Set `ANT_HOME`, `ANDORID_HOME` and `CROSSWALK_APP_TOOLS_CACHE_DIR` env

#### iOS Testing

1. Install Xcode 7.1(ios SDK) from App store on Mac
1. Install [Python](https://www.python.org/downloads/mac-osx/), suggest version 2.7.6
1. Make sure node version is 4.2.1
1. Install git and ruby.(It should be pre-installed on your Mac already.)
1. Install CocoaPods through ruby gem (install step please refer to http://blog.csdn.net/wangyang2698341/article/details/22678027 and http://www.jianshu.com/p/6e5c0f78200a): `$ sudo gem install cocoapods`
1. If “Fail to export application with return code：70” is displayed when build project. Please follow below steps to export iOS package with smaller size: </br>
1) Go to the App shell directory after creating project: `$ cd prj/ios/AppShell/` </br>
2) Open archived.xcarchive with Xcode </br>
3) Select the archive in the list, click ‘Export…” button at right side bar, choose “Save for Ad Hoc Deployment”, then next </br>
4) After the account validation, select “Export one app for All compatible devices” in Device Support page, then next </br>
5) In the summary page, select “Rebuild from bitcode”, which is the way to save the package size </br>
6) Then next, Xcode will start the exporting process and finally an IPA package will be generated onto your desktop </br>
7) After this, the “Rebuild from bitcode” will be kept selected, no matter if you export from Xcode IDE or command line with crosswalk-app

### Deepin Host

1. Download [Crosswalk test binary (64bit)](http://pan.baidu.com/) (user: crosswalk_deepin@163.com)
1. Install Crosswalk Binary: `$ dpkg -i crosswalk_13.41.302-0_amd64.deb`
1. The Node.js, Android SDK, JDK, apache ant and git must be functional
1. Setup `ANDROID_HOME` environment variable
1. Enable .deb Backend in App-tools:
```xml
$ apt-get install devscripts
$ apt-get install build-essential
$ apt-get install debhelper
```

### Windows Host

#### Android Testing

1. Install Python, suggest version 2.7.6
1. Install Android SDK, JDK for Windows
1. Install [apache-ant-1.9.6](http://www.onlinedown.net/softdown/77637_2.htm)
1. Install node and npm, suggest node version 0.10.30 and npm version 1.4.21
1. Install [setuptools module](https://pypi.python.org/pypi/setuptools)
1. Install [webp conversion tool](http://downloads.webmproject.org/releases/webp)
1. Install BeautifulSoup: `$ pip install BeautifulSoup`
1. Setup the environment variable for each path: </br>
1) Set `Android SDK`, `npm` and `node` env to "PATH" </br>
2) Set `ANT_HOME`, `ANDORID_HOME` and `CROSSWALK_APP_TOOLS_CACHE_DIR` env

#### Windows Testing

1. Install [WiX](https://msdn.microsoft.com/en-us/library/gg513936.aspx) per
1. Install node and git
1. Install BeautifulSoup: `$ pip install BeautifulSoup`
1. Setup `Python`, `Wix` env to "PATH" and setup `CROSSWALK_APP_TOOLS_CACHE_DIR` env

## Run App-tools Test Suit

### Android Testing

- Install test suite and App-tools:
```xml
$ Unzip testsuit zip
$ cd opt/apptools-xxx-tests/tools/
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools
$ cd crosswalk-app-tools/
$ sudo npm install
$ sudo npm install exec-sync
```
- Connect Android devices to your localhost
- Edit "apptools-android-tests/arch.txt" to configure the type of test device, e.g. `x86`, `arm` and `x86,arm`.
- Edit "apptools-android-tests/mode.txt" to configure the type of build mode, e.g. `lite`, `shared` and `embedded`.
- Edit "apptools-android-tests/host.txt" to configure the type of test host, e.g. `Windows`, `iOS` and `Android`.
- Edit "apptools-android-tests/version.txt" to configure the Crosswalk which you want to test, e.g. `17.45.434.0 32` and `17.45.434.0 64`.
- Download [release crosswalk zip](https://download.01.org/crosswalk/releases/crosswalk/android/) to apptools-android-tests/tools
- Run android tests with testkit-lite:
```xml
$ cd [testprefix-path]/opt/apptools-android-tests/
$ testkit-lite -f [testprefix-path]/opt/apptools-android-tests/tests.xml -A -o [testprefix-path]/opt/apptools-android-tests/result.xml --comm androidmobile --deviceid=Medfield3C6DFF2E --testprefix=[testprefix-path]
```
### iOS Testing

- Install test suite, App-tools and iOS backend:
```xml
$ Unzip testsuit zip
$ cd opt/apptools-xxx-tests/tools/
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools
$ cd crosswalk-app-tools/
$ npm install
$ cd node_modules
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools-ios.git crosswalk-app-tools-backend-ios
$ cd crosswalk-app-tools-backend-ios
$ npm install
```
- Connect iOS devices to your localhost
- Run iOS tests with testkit-lite:
```xml
$ cd [testprefix-path]/opt/apptools-ios-tests/
$ testkit-lite -f [testprefix-path]/opt/apptools-ios-tests/tests.xml -A -o [testprefix-path]/opt/apptools-ios-tests/result.xml --comm localhost --testprefix=[testprefix-path] --non-active
```
### Linux Testing

- Install test suite, App-tools and deb backend:
```xml
$ Unzip testsuit zip
$ cd opt/apptools-xxx-tests/tools/
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools
$ cd crosswalk-app-tools/
$ npm install
$ cd node_modules
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools-deb.git crosswalk-app-tools-backend-deb
$ cd crosswalk-app-tools-backend-deb
$ npm install
```
- Add crosswalk-app-tools/src/ to environment PATH
- Run deb tests with testkit-lite:
```xml
$ cd [testprefix-path]/opt/apptools-linux-tests/
$ testkit-lite -f $PWD/tests.xml -A --comm deepin --testprefix $PWD/../../ -o $PWD/result.xml
```
### Windows Testing

- Install test suite and App-tools:
```xml
$ Unzip testsuit zip
$ cd opt/apptools-xxx-tests/tools/
$ git clone https://github.com/crosswalk-project/crosswalk-app-tools
$ cd crosswalk-app-tools/
$ npm install
```
- Download [Crosswalk windows binary](https://download.01.org/crosswalk/releases/crosswalk/windows/) to apptools-windows-tests/tools
- Run windows tests with testkit-lite:
```xml
$ cd [testprefix-path]/opt/apptools-windows-tests/
$ testkit-lite -f [testprefix-path]/opt/apptools-windows-tests/tests.xml -A -o [testprefix-path]/opt/apptools-windows-tests/result.xml --comm localhost --testprefix=[testprefix-path] --non-active
```
