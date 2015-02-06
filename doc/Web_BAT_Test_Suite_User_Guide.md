# Web BAT Test Suite User Guide

## 1. Introduction

This document provides the method to run Web BAT TestSuite on Tizen Generic Platform.


Note that the `tester` in this guide is the user name of the device under test. It just means a normal username for multiuser support.

## 2. Test Environments

- Tizen Generic Platform Hardware: Acer Sandy Bridge Notebook with USB-to-Ethernet(The model Tizen Image supported) converter. Ensure [Tizen generic-wayland-x86\_64 image](http://download.tizen.org/snapshots/tizen/generic/generic-wayland-x86_64/) installed following the WIKI for image installation.
- [setuptools](https://pypi.python.org/packages/source/s/setuptools/): a testkit-lite dependent pythonmodule for Device Mode.
- Request-master: [request-master.zip](https://codeload.github.com/kennethreitz/requests/zip/master), a testkit-lite dependent package for Device Mode.
- [testkit-lite](https://github.com/testkit/testkit-lite): a command-line interface application
- [teskit-stub](https://github.com/testkit/testkit-stub): a test stub application
- [tinyweb](https://github.com/testkit/tinyweb): a web service application
- Test Suite:web-xbat-tests-xxx.xpk.zip

    **Note:**If you want to generate these Test Suite packages from the source code by yourself, you can refer to **Web\_Test\_Suite\_Packaging\_Guide\_v1.0** chapter 3.3 "Pack Web Test Suite Packages for Tizen IVI"

## 3. BAT Preconditions

### 3.1 Setup Ubuntu (12.04 64bit) Host for the Test Environments

- Install git

    sudo apt-get install git #Maybe you need setup HTTP Proxy

- Install g++

    sudo apt-get install g++ #Maybe you need setup HTTP Proxy

- Get setuptools package

    wget -r -np -nd [https://pypi.python.org/packages/source/s/setuptools/setuptools-latest-version.tar.gz](https://pypi.python.org/packages/source/s/setuptools/setuptools-latest-version.tar.gz)#Maybe you need setup HTTPS Proxy

- Get request-master.zip

    wget -r -np -nd [https://github.com/kennethreitz/requests/archive/master.zip](https://github.com/kennethreitz/requests/archive/master.zip) #Maybe you need setup HTTPS Proxy

- Download testkit-lite source codes

    git clone git@github.com:testkit/testkit-lite.git

- Download testkit-stub source codes and generate execute binary

    git clone [git@github.com:testkit/testkit-stub.git](mailto:git@github.com:testkit/testkit-stub.git)

    cd testkit-stub

    make #here will generate testkit-stub execute binary used in next execution steps

- Download tinyweb source codes and generate execute binaries

    git clone [git@github.com:testkit/tinyweb.git](mailto:git@github.com:testkit/tinyweb.git)

    cd tinyweb

    make #here will generate tinyweb, cgi-getcookie and cgi-getfield execute binaries used in next execution steps

**Note** : To execute these last two above steps, make sure you use Ubuntu 12.04 **64 bit** OS.

### 3.2 Use SSH to Connect Tizen Device

ssh root@device-ip #you may need input the pwd: tizen

### 3.3 Install Crosswalk Binary on Tizen Device

zypper ar [http://download.tizen.org/snapshots/tizen/generic/generic-wayland-x86\_64/latest/repos/generic/x86\_64/packages/](http://download.tizen.org/snapshots/tizen/generic/generic-wayland-x86_64/latest/repos/generic/x86_64/packages/) Repo\_Generic

\#Maybe you need setup HTTP Proxy

zypper ref -r Repo\_Generic

zypper in crosswalk

### 3.4 Install testkit-lite on Tizen Device

scp username@host-ip:/path/to/requests-master.zip /tmp

unzip /tmp/requests-master.zip -d /tmp

cd /tmp/requests-master

python setup.py install

scp username@host-ip:/path/to/setuptools-latest-version.tar.gz /tmp

tar -xzvf /tmp/setuptools-latest-version.tar.gz -C /tmp

cd /tmp/setuptools-x-x

python setup.py install

scp –r username@host-ip:/path/to/testkit-lite /tmp

cd /tmp/testkit-lite

python setup.py install

### 3.5 Install testkit-stub on Tizen Device

scp username@host-ip:/path/to/testkit-stub/testkit-stub /usr/bin

### 3.6 Install tinyweb on Tizen Device

scp username@host-ip:/path/to/tinyweb/tinyweb /opt/home/tester

scp username@host-ip:/path/to/tinyweb/cgi-getcookie /opt/home/tester

scp username@host-ip:/path/to/tinyweb/cgi-getfield /opt/home/tester

scp username@host-ip:/path/to/tinyweb/server.pem /opt/home/tester

cd /opt/home/tester/

chmod 666 server.pem

ln -s /usr/lib64/libssl.so.1.0.0 /opt/home/tester/libssl.so

ln -s /usr/lib64/libcrypto.so.1.0.0 /opt/home/tester/libcrypto.so

### 3.7 Install Test Suiten Tizen Device

scp username@host-ip:/path/to/web-xbat-tests-xxx.xpk.zip /tmp

unzip /tmp/web-xbat-tests-xxx.xpk.zip -d /opt/usr/media/tct/

sh /opt/usr/media/tct/opt/web-xbat-tests/inst.sh

**Note** : Please update the suite name when you use above commands, e.g. change "web-xbat-tests" to "web-abat-xwalk-tests"

Then you can get the appid of the test APP (will be used in next execution steps):

su tester -c "export DBUS\_SESSION\_BUS\_ADDRESS=\"unix:path=/run/user/5000/dbus/user\_bus\_socket\";export XDG\_RUNTIME\_DIR=\"/run/user/5000\";app_launcher -l"

## 4. Run BAT Tests

### 4.1 Launch tinyweb

env LD\_LIBRARY\_PATH=/opt/home/tester PATH=$PATH:/opt/home/tester tinyweb -ssl\_certificate /opt/home/tester/server.pem -document\_root /opt/usr/media/tct/ -listening\_ports 80,8080,8081,8082,8083,8443s&

### 4.2 Run Tests

testkit-lite -e 'su tester -c "export DBUS\_SESSION\_BUS\_ADDRESS=\"unix:path=/run/user/5000/dbus/user\_bus\_socket\";export XDG\_RUNTIME\_DIR=\"/run/user/5000\";app_launcher -s $appid"' -f /opt/usr/media/tct/opt/web-xbat-tests/tests.xml --comm localhost -o /path/to/result.xml

**Note:** Please update the suite name when you use above commands, e.g. change "web-xbat-tests" to "web-abat-xwalk-tests"

### 4.3 Get result from /path/to/result.xml

### 4.4 Uninstall Tests

sh /opt/usr/media/tct/opt/web-xbat-tests/inst.sh -u

**Note** : Please update the suite name when you use above commands, e.g. change "web-xbat-tests" to "web-abat-xwalk-tests"

