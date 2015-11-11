## Introduction

This test suite is for the tests of Crosswalk Windows extensions using .Net.
In this tutorial, you will build a Crosswalk Android application with a .Net extension. This consists of two main pieces:

* A Crosswalk extension

  The extension consists of:
  1. C# source code: Standard C# classes, packaged into a dll file.
  
  Note that a Crosswalk application can use multiple extensions if desired.

* An HTML5 web application

  This is a self-contained web application which "lives inside" the Android application, but uses Crosswalk as its runtime. It consists of standard assets like HTML files, JavaScript files, images, fonts etc.  
  The Crosswalk extension is invoked by code in the web application, via the JavaScript wrapper mentioned above.


## Pre-conditions

* Require Microsoft Visual Studio 2013
* Require Windows Crosswalk pkg


## Build an extension

Build the xwalk-echo-extension source code to a dll file using Microsoft Visual Studio 2013  


## Run on Windows
Copy the extension dll file to myextension folder and rename it to "echo_extension.dll"
Copy the xwalk_dotnet_bridge.dll from windows Crosswalk pkg to myextension folder and rename it to "echo_extension_bridge.dll"
Enter opt/usecase-extension-windows-tests/xwalk-echo-app use cmd, execute "python -m SimpleHTTPServer 8080" to start a server
Unzip the windows crosswalk pkg, open cmd, execute "xwalk.exe http://localhost:8080 --allow-external-extensions-for-remote-sources --external-extensions-path=/path/to/myextension"


## Authors:

* Zhu, Yongyong <yongyongx.zhu@intel.com>


## LICENSE

Copyright (c) 2015 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
