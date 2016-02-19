# Cordova Test Suite Developer Guide

## Overview

This document is intended for those who want to make test contributions to this Cordova test suite.

Please formiliarize yourself with the following knowledge:
- Basic knowledge in [web test suite developer guide](./Web_Test_Suite_Developer_Guide.md)
- [PyUnit](http://pyunit.sourceforge.net/pyunit.html), the standard unit testing framework for Python. It is called by testkit-lite to support the test execution.


## How to add a new Test Suite?

The best method to add a new test suite is to copy a simliar existing test suite
and then update related test scripts.

1. Fork and clone your forked repository to local system, and
   make a new branch. See http://testthewebforward.org/docs/configuration.html
1. Copy a simliar existing test suite, e.g. `cordova-feature-android-tests`, and rename it following `cordova-<suitename>-<platform>-tests`.
1. Create new test cases (see next section) and update `tests*.xml` files.
1. Package the test suite and run the test cases.
1. Submit your changes in a pull request.


## More info about Crosswalk Webview plugin
If you want to get more info about Crosswalk Webview plugin, please refer to [https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview](https://github.com/crosswalk-project/cordova-plugin-crosswalk-webview)
