# Usecase Test Suite Developer Guide

## Overview

This document is intended for those who want to make test contributions
to Usecase test suite.

Please formiliarize yourself with the following knowledge:

- [Bootstrap](http://getbootstrap.com/getting-started/), a framework based on
  HTML, CSS, Javascript.
- [JQuery](https://jquery.com/)


## Test suite source layout

The layout of test source code is designed to meet requirements of
usecase and Crosswalk Project for supporting different package
formats for various platforms, such as Android, Windows, etc.

A typical test suite source layout looks like this:

```
<usecase-suite-name>
  |- <css>
  |- <fonts>
  |- <js>
  |- <samples>
  |- <steps>
  |- [res]
  |- index.html
  |- index.wts.html
  |- report.html
  |- tests_list.html
  |- VERSION
  |- icon.png/icon.ico
  |- inst.*.py
  |- manifest.json
  |- manifest.windows.json
  |- suite.json
  |- tests.android.xml
  |- tests.auto.xml
  |- tests.full.xml
  |- tests.windows.xml
  |- tests.wts.xml
```

Where,

- `<usecase-suite-name>`: name of usecase test suite package, usually in
  `usecase-<module>-<platform>-tests` format.
- `<css>`: css resources for bootstrap framework, maintained in tools/bootstrap-fw,
  and built into test suite package if specified in `suite.json`.
- `<fonts>`: font resources for bootstrap framework, maintained in tools/bootstrap-fw,
  and built into test suite package if specified in `suite.json`.
- `<js>`: js resources for bootstrap framework, maintained in tools/bootstrap-fw,
  and built into test suite package if specified in `suite.json`.
- `<samples>`: source files or directories for usecase test.
- `<steps>`: test steps file for usecase test.
- `[res]`: optional, css/font/images/js/media resources for usecase test.
- `index.html`: index page for bootstrap framework, which aslo be usecase home page,
   maintained in tools/bootstrap-fw, and built into test suite package if specified
   in `suite.json`.
- `index.wts.html`: index page for bootstrap framework, which aslo be wts service
   home page, maintained in tools/bootstrap-fw, and built into test suite package
   if specified in `suite.json`.
- `report.html`: report page of test result for bootstrap framework, maintained
   in tools/bootstrap-fw, and built into test suite package if specified in `suite.json`.
- `tests_list.html`: test list page for bootstrap framework, maintained in
   tools/bootstrap-fw, and built into test suite package if specified in `suite.json`.
- `VERSION`: bootstrap framework version, maintained in tools/bootstrap-fw,
   and built into test suite package if specified in `suite.json`.
- `icon.png`， `icon.ico`: icon image for usecase package as web application.
   icon.ico is for windows application.
- `inst.*.py`: scripts to install built test suite package.
- `manifest.json`, `manifest.windows.json`: webapp config file for android and windows
   platform. It can define app name, package id, icon, start url, permissions, etc.
- `suite.json`: a package specification file, which provides the test suite
  package's architecture in different package types. It will be parsed by the
  pack tool (`pack.py`) when build web test suite package.
- `tests.full.xml`, `tests.android.xml`, `tests.windows.xml`: files to describe
   all test cases in each platform for usecase.
   See [Appendix 1](#appendix-1-testsfullxml-and-testsxml) for details.
- `tests.auto.xml`: describe auto test cases for webdriver testing.
- `tests.wts.xml`: describe all test cases for web testing service.


## Test case coding style

See the [coding style guide cheatsheet](./Coding_Style_Guide_CheatSheet.md)
documentation.


## Add new usecase to test suite

Take "Jsenhance" as an example:

```
<samples>
  |- Jsenhance
      |- <js>
      |- index.html
      |- README.md
<steps>
  |- Jsenhance
      |- step.js
```

- Create test folder named `Jsenhance` under `samples` folder, add index.html as
  test main page html file, import bootstrap framework to index.html following below:

```
<link rel="stylesheet" type="text/css" href="../../css/bootstrap.css">
<link rel="stylesheet" type="text/css" href="../../css/main.css">
<script src="../../js/jquery-2.1.3.min.js"></script>
<script src="../../js/bootstrap.min.js"></script>
<script src="../../js/common.js"></script>
<script src="../../js/tests.js"></script>

<div id="header">
  <h3 id="main_page_title"></h3>
</div>
<div class="content">
    [test body]
<div class="footer">
  <div id="footer"></div>
</div>
<div class="modal fade" id="popup_info">
    [test description/purpose]
</div>
```

- Add `README.md` for usecase functions and covered interface.

- Create step folder named `Jsenhance` under `steps` folder, add `steps.js`
  for usecase test steps:

```
var step = '<font class="fontSize">'
            +'<p>Test Purpose: </p>'
            +'<p>Verifies the async and defer attributes of script element, classList, getElementsByClassName and matchesSelector work well.</p>'
            +'<p>Expected Result: </p>'
            +'<p>Test pass if a green PASS displays on the page, otherwise test fail</p>'
          +'</font>';
```

- Add `Jsenhance` to `tests.full.xml`, and keep case id same with test folder name. Set correct `platform` attribute.

    - **all**: usecase supported on all platforms
    - **android**: usecase only supported on android
    - **linux**: usecase only supported on linux
    - **windows**: usecase only supported on windows
    - **ios**: usecase only supported on ios

- Convert `tests.<platform>.xml` using [xmlsimplifier](https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/tools/xmlsimplifier).


## About demo-express

[demo-express](https://github.com/crosswalk-project/demo-express) is a central
place to collect web feature samples that demonstrate use of W3C standard APIs,
embedding APIs, and web runtime features.

It's similar with usecase, but have no test steps. If the usecase is developed by
standard APIs, its sample code will be moved to demo-express, and keep steps in
usecase test suite, each feature APIs have different floder:

```
|- samples-cordova
|- samples-embedding
|- samples-wrt
|- samples
```

When packing usecase test suite, need merge these sample floder of demo express
to usecase, to make sample code complete.


## Appendix 1 tests.full.xml and tests.xml

**tests.full.xml**:

```
<?xml version="1.0" encoding="UTF-8"?>
<test_definition>
  <suite name="usecase-webapi-xwalk-tests">
    <set name="Multimedia &amp;amp; Graphics" background="brand-success" icon="glyphicon-facetime-video" type="js">
      <testcase component="Crosswalk Use Cases/WebAPI" execution_type="auto" id="Jsenhance" platform="all" priority="P0" purpose="Jsenhance" status="approved" type="functional_positive">
      </testcase>
    </set>
  </suite>
</test_definition>
```

**tests.android.xml**:

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite name="usecase-webapi-xwalk-tests">
    <set background="brand-success" icon="glyphicon-facetime-video" name="Multimedia &amp;amp; Graphics">
      <testcase component="Crosswalk Use Cases/WebAPI" execution_type="auto" id="Jsenhance" purpose="Jsenhance">
      </testcase>
    </set>
  </suite>
</test_definition>
```

More test xml classification can refer to
[Test case classification](./Web_Test_Suite_Developer_Guide.md#test-case-classification) documentation.
