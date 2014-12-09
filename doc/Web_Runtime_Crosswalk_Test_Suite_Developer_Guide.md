# Web Runtime Crosswalk Test Suite DeveloperGuide

Version 1.0

Copyright © 2014 Intel Corporation. All rights reserved. No portions of this document may be reproduced without the written permission of Intel Corporation.

Intel is a trademark of Intel Corporation in the U.S. and/or other countries.

Linux is a registered trademark of Linus Torvalds.

Tizen® is a registered trademark of The Linux Foundation.

ARM is a registered trademark of ARM Holdings Plc.

\*Other names and brands may be claimed as the property of others.

Any software source code reprinted in this document is furnished under a software license and may only be used or copied in accordance with the terms of that license.

#1. Overview

This document is intended for developers who contribute WebAPI test cases development.

You are supposed to have gained the following knowledge:

- Where to download WebAPI test source codes and how to run them
- How to download and run Testkit-lite
- What is W3C test harness, which is called by Testkit-lite to support the execution of WebAPI tests

    Note: Testkit-lite is a test execution framework. For details, see [https://github.com/testkit/testkit-lite](https://github.com/testkit/testkit-lite).

#2. Test Suite Source Layout

The layout of test source codes should:

- Meet the requirements of Testkit-lite
- Meet the requirements of W3C test harness
- Meet project requirements, for example, support different package formats so that tests can be executed on various platforms

The test suite source layout is detailed as follows:

\<wrt-module-tizen-tests\>/

├── [common]/

├── config.xml

├── COPYING

├── icon.png

├── inst.sh.apk

├── inst.sh.ivi

├── inst.sh.wgt

├── inst.sh.xpk

├── manifest.json

├── \<module\>/

├── [README]

├── resources/

├── suite.json/

├── testcase.xsl

├── testresult.xsl

├── tests.css

├── tests.xml

├── tests.full.xml

└── webrunner/

- \<wrt-module-category-tests\>: name of WRT test package. The 'wrt-' prefix and the '-tests' suffix must be available.

- Documents:
  - README: an introduction of the test suite, and (optional) pre-/post-conditions.
  - COPYING: license and copying file

- Test-related files and folders:
  - \<module\>/: a serial of source files or directories for test cases that are well organized by components or features to be tested, e.g. shadowdom/xxx, input/xxx
  - full.xml & tests.xml: a mandatory file to describe all test cases for this test suite. For details, see "Appendix 2 Tests.full.xml and tests.xml."

- W3C test harness support:
  - [common]/: (optional) integrated from [https://github.com/w3c/web-platform-tests/tree/master/common](https://github.com/w3c/web-platform-tests/tree/master/common) to include common test functions
  - resources/: integrated from [https://github.com/w3c/testharness.js](https://github.com/w3c/testharness.js) to include W3C test harness as an API test framework

- Build/pack support: 
  - ../../tool/build/pack.py: script for generating a zip package 
  - inst.sh.apk: script for installing the apk package on Android mobile.
  - inst.sh.ivi: script for installing the xpk package on Tizen IVI device.
  - inst.sh.wgt: script for installing the wgt package on Tizen mobile.
  - inst.sh.xpk: script for installing the xpk package on Tizen mobile.
  - config.xml: configuration file for creating a .wgt package
  - icon.png: Widget/Extension icon
  - manifest.json: manifest file for creating a .crx extension
  - suite.json: suite package file including version and configuration for setting suite signature.

- Installation/execution support:
  - webrunner/: web test runner for executing WebAPI test suite. It is integrated from https://github.com/testkit/webrunner


#3. Test Case Coding Style

Test case developers shall follow the following rules:

- Comment each code block in a uniform way
- Return a clear pass/fail result 
- Clean environment before exiting tests
- Automate test under condition of stability 
- Keep test cases independent from each other 
- Keep case independent from UX or vertical specific applications 
- Avoid complicated code logic (comment it if unavoidable) 
- Avoid duplicated code 
- Remove redundant code 

Please refer to the `Coding_Style_Guide_CheatSheet.md` to get a quick start.

You can find detailed coding style instructions for specific languages from:

1. CSS & HTML: [http://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml](http://google-styleguide.googlecode.com/svn/trunk/htmlcssguide.xml)
2. JavaScript: [http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml](http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml)
3. Python: [http://google-styleguide.googlecode.com/svn/trunk/pyguide.html](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
4. Shell: [http://google-styleguide.googlecode.com/svn/trunk/shell.xml](http://google-styleguide.googlecode.com/svn/trunk/shell.xml)
5. XML: 'xmllint --format' with default indent 2 spaces. See [http://xmlsoft.org/xmllint.html](http://xmlsoft.org/xmllint.html)

#4. Test Case Naming Convention

**Template**

A test case should be named as per the following conventions:

- Use Feature name
- Use '\_' to connect words in file names 

**Examples**

packagemgt\Crosswalk_XPK_Update_VersionOneToMultiLower.html

#5. Test Case Folder Naming Convention

A test case folder should be named as per the following conventions:

- Allow only letter, digit, and hyphen in test case folder name.
- For folder name, please also use lower-case with '-' if necessary. 
- Name \<module\> as a feature, component.

#6. Test Case Classification (<testcase\> field in tests.xml)

**Template**

<testcase purpose="" type="" status="" component="" execution_type="" priority="" id=""\>

Test case created should be classified by the following rules:

- Purpose: test assertion; should be unique in whole tests.xml (no duplicate test case).
- Type: currently only support 'compliance'.
- Status: test case status
  - designed: test case is just designed but notready for review.
  - ready: test case is ready for review.
  - approved: test case is reviewed and qualified to be released; currently only use this status when merge tests into test suites.

- Component: should comply with the WRT component name list.
- Execution\_type: 
  - auto: 
  - manual: 

- Priority: P0/P1/P2/P3
  - P0: use cases for feature to be tested, WRT use cases; P0 tests will be used in sanity testing.
  - P1: feature verification tests, WRT and its attribute presence and normal usage; P0+P1 tests will be used in feature verification testing.
  - P2: positive tests of extended feature tests, WRT parameter combination tests.
  - P3: negative tests of extended feature tests, complicated use cases, stress tests; P0+P1+P2+P3 tests will be used in full-pass testing.

- Id: test case identification should be unique in whole tests.xml (no duplicate test case); can be simply as test case name without extension.

**Example**

    <testcase purpose="Validate if the web app can show 'text' when settings language is set to English" type="Functional" status="approved" component="Crosswalk I18n" execution_type="manual" priority="P1" id="Crosswalk_I18n_TestEn">
      <description>
        <pre_condition>
          Make sure Crosswalk application is launched.
        </pre_condition>
        <test_script_entry>/opt/wrt-i18nmanu-tizen-tests/i18n/Crosswalk_I18n_TestEn.html</test_script_entry>
      </description>
    </testcase>

#7. How to Add New Test Suite to WRT 
To add a new suite to wrt, perform the following steps:

1. Fork and clone the webtest project from https://github.com/crosswalk-project/crosswalk-test-suite
2. Copy a test suite to the spec under testing, for example, "tct-style-css3-tests".
3. Update `suite.json` to `../../tools/pack.py` happy.
4. Update config.xml, e.g:

    <widget id='http://tizen.org/test/wrt-i18nmanu-tizen-tests' xmlns='http://www.w3.org/ns/widgets' xmlns:tizen='http://tizen.org/ns/widgets' version='1.0.0.1'>
      <access origin="*"/>
      <icon src="icon.png" height="117" width="117"/>
      <name>wrt-i18nmanu-tizen-tests</name>
      <tizen:application id="i18ntestcs.wrti18ntizentests" package="i18ntestcs" required_version="2.2"/>
      <tizen:setting screen-orientation="landscape"/>
    </widget>
    

5. Add new cases to the test suite. 

#8 How to Contribute New Cases to Test Suite Package

To contribute new cases to test suite package, perform the following steps:

1. Design new test case according to WRT Spec and add new case information to **tests.xml**. For details, see "Appendix 1 Tests.full.xml and tests.xml."

- "Case name" should follow the test case naming convention. For details, see chapter 4 "Test Case Naming Convention".
- "Specs" field should follow the Spec coverage assertion rules. For details, see chapter **Error! Reference source not found.** "Test Case Classification (<testcase\> field in tests.xml)".
- "Component" field should comply with the WRT component name list.

2. Develop test script by following the test case coding style and put it under \<module\>.

Note:

- Each test should have an entry HTML file.
- The test script can be embedded into the HTML file or be used as separate JavaScript file.
- For details on how to use W3C test harness, see [testharness.js API document](https://github.com/w3c/testharness.js/blob/master/docs/api.md).

**Example**

    <meta charset='utf-8'>
    <title>Crosswalk_I18n_AppNameChinese_Test</title>
    <link rel="author" title="Intel" href="http://www.intel.com">

    <p>
      <strong>Test steps:</strong>
    </p>
    <ol>
      <li>install i18n_locales_chinese_tests wgt app </li>
      <li>Change the System Settings language to Chinese</li>
      <li>Check the web app name and launcher it </li>
    </ol>
    <p>
      <strong>Expected Output:</strong>
    </p>
    <ol>
      <li>The app can be install successfully</li>
      <li>The device language is set to Chinese successfully</li>
      <li>Web app name with Chinese and launch successfuly</li>
    </ol>

#9 How to Contribute pairwise Cases to Test Suite Package
- Install  AllPairs

  - Download AllPairs from here:
   
     http://sourceforge.net/projects/allpairs/
     
  - Copy metacomm folder to your suite:
     metacomm/
     
  - import metacomm in your python file:
    
    import metacomm.combinatorics.all_pairs2
   
  -  all_pairs sample:
  
     list=[[1,2],[3]]
     input_pair = all_pairs( list )
     for e, v in enumerate(input_pair):
         print e,v

....0 [1, 3]
....1 [2, 3]


#Appendix 1 Tests.full.xml and tests.xml
Each test suite package has two dedicated .xml files (tests.full.xml and tests.xml), which defines all test cases in the package.
Tests.xml is a simplified version of tests.full.xml; it contains the minimum required elements when running the tests.
Note: The .xml files must comply with the rules in the test\_definition.xsd file. For details, see  [https://github.com/testkit/testkit-lite/blob/master/xsd/test\_definition.xsd](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

Example:
```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite name="wrt-i18nmanu-tizen-tests" category="Crosswalk_I18n" launcher="xwalk">
    <set name="i18n" type="js">
      <testcase purpose="Validate if the web app can show 'Web' Test when settings language is set to English" type="Functional" status="approved" component="Crosswalk I18n" execution_type="manual" priority="P1" id="Crosswalk_I18n_TestEn">
        <description>
          <pre_condition>
            1.Make sure Crosswalk application is launched.
          </pre_condition>
          <test_script_entry>/opt/wrt-i18nmanu-tizen-tests/i18n/Crosswalk_I18n_TestEn.html</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>

Tests.xml Example.

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk_I18n" launcher="xwalk" name="wrt-i18nmanu-tizen-tests">
    <set name="i18n" type="js">
      <testcase component="Crosswalk I18n" execution_type="manual" id="Crosswalk_I18n_TestEn" purpose="Validate if the web app can show 'Web' Test when settings language is set to English">
        <description>
          <pre_condition>
            1.Make sure Crosswalk application is launched.
          </pre_condition>
          <test_script_entry>/opt/wrt-i18nmanu-tizen-tests/i18n/Crosswalk_I18n_TestEn.html</test_script_entry>
        </description>
      </testcase>
     </set>
  </suite>
</test_definition>
```
