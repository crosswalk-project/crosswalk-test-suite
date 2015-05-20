# Web Runtime Crosswalk Test Suite DeveloperGuide

## 1. Overview

This document is intended for developers who contribute WebAPI test cases development.

You are supposed to have gained the following knowledge:

- Where to download WebAPI test source codes and how to run them
- How to download and run Testkit-lite
- What is W3C test harness, which is called by Testkit-lite to support the execution of WebAPI tests

    Note: Testkit-lite is a test execution framework. For details, see [https://github.com/testkit/testkit-lite](https://github.com/testkit/testkit-lite).

## 2. Test Suite Source Layout

The layout of test source codes should:

- Meet the requirements of Testkit-lite
- Meet the requirements of W3C test harness
- Meet project requirements, for example, support different package formats so that tests can be executed on various platforms

The test suite source layout is detailed as follows:

<wrt-xxx-tizen-tests\>/

├── autogen

├── [common]/

├── configure.ac

├── config.xml.crx

├── config.xml.wgt

├── COPYING

├── icon.png

├── inst.sh.apk

├── inst.wgt.py

├── inst.sh.ivi

├── inst.sh.wgt

├── inst.sh.xpk

├── Makefile.am

├── manifest.json

├── pack.sh

├──[README]

├── resources/

├── testkit/

├── testapp/

├── testcase.xsl

├── testresult.xsl

├── tests.css

├── tests.xml

├── tests.full.xml

├── <testcasefolder\>/

├── <wrt-xxx-tizen-tests.spec\>

├── [utils]/

└── [data]/

- <wrt-xxx-tizen-tests\>: name of Web Runtime Crooswalk test package. The 'wrt-' prefix and the '-tests' suffix must be available, for example, wrt-manifest-tizen-tests.
- Documents:
  - README: an introduction of the test suite, and (optional) pre-/post-conditions.
  - COPYING: license and copying file

- Test-related files and folders:
  - <testcasefolder\>/: a serial of source files or directories for test cases that are well organized by components or features to be tested
  - <testapp\>/: a serial of source files or sample webapp for test cases.

- W3C test harness support:
  - [common]/: (optional) integrated from [https://github.com/w3c/web-platform-tests/tree/master/common](https://github.com/w3c/web-platform-tests/tree/master/common) to include common test functions
  - resources/: integrated from [https://github.com/w3c/testharness.js](https://github.com/w3c/testharness.js) to include W3C test harness as an API test framework

- Build/pack support:
  - autogen, configure.ac, and Makefile.am
  - pack.sh: script for generating a zip package
  - inst.wgt.py: script for installing the wgt package on Tizen IVI device.
  - inst.sh.wgt: script for installing the wgt package on Tizen mobile.
  - inst.sh.xpk: script for installing the xpk package on Tizen mobile.
  - config.xml.crx: configuration file for creating a .crx extension
  - config.xml.wgt: configuration file for creating a .wgt package
  - icon.png: Widget/Extension icon
  - manifest.json: manifest file for creating a .crx extension
  - <wrt-xxx-tizen-tests.spec\>: specification file including version and configuration for setting suite signature; please set src\_file to keep the source code files in packaged test suite and put specific files to be kept in whitelist. For Web Runtime Crosswalk, specifications, the 'wrt-' prefix and the '-tests' suffix must be available, for example, wrt-manifest-tizen-tests.spec.

- Installation/execution support:
  - testkit/: WRT test runner for executing WRT test suite. It is integrated from and updated with Testkit-lite. For details, see https://github.com/testkit/testkit-lite.

- Misc:
  - [utils]/: (optional) contains utilities and tools if any
  - [data]/: (optional) contains small-sized data files (Large-sized data such as media content requires a separate package.)
  - Small-sized data files (a few Kbytes) should be included into the tests. Large-sized files should be made available separately. Instructions on how to obtain the data files must be provided in the README file.
  - Test data must be publicly available.

The following files and folders are mandatory in :

- autogen
- config.ac
- config.xml.crx
- config.xml.wgt
- icon.png
- inst.wgt.py
- suite.json
- Makefile.am
- manifest.json
- pack.sh
- resources/
- testkit/
- testapp/
- testcase.xsl
- testresult.xsl
- tests.css
- tests.xml
- tests.full.xml
- <wrt-xxx-tizen-tests.spec\>

## 3. Test Case Coding Style

Refer to the `Coding_Style_Guide_CheatSheet.md`.

## 4. Test Case Naming Convention

**Template**

A test case should be named as per the following conventions:

- Use Feature name
- Use '\_' to connect words in file names

**Examples**

packagemgt\Crosswalk_XPK_Update_VersionOneToMultiLower.html

## 5. Test Case Folder Naming Convention

A test case folder should be named as per the following conventions:

- Allow only letter, digit, and hyphen in test case folder name.
- For folder name, please also use lower-case with '-' if necessary.
- Name <testcasefolder\> as a feature, component.

## 6. Test Case Classification (<testcase\> field in tests.xml)

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

## 7. How to Add New Test Suite to WRT
To add a new suite to wrt, perform the following steps:

1)Fork and clone the wrt project from

https://github.com/crosswalk-project/wrt

**Note** : you must sign up for the GitHub first.

2)Copy a test suite to the spec under testing, for example, "wrt-i18nmanu-tizen-tests".

3)Replace folder with real test case folder name in Makefile.am:

    commondir =  resources webrunner i18n
    SUBDIRS = $(commondir)
    docdir = /opt/wrt-i18nmanu-tizen-tests
    dist_doc_DATA = COPYING README tests.xml tests.full.xml

4)Replace folder with real test case folder name used in configure.ac:

    AC_INIT([wrt-i18nmanu-tizen-tests], [6.34.1.2], [zhiqiang.zhang@intel.com])
    AM_INIT_AUTOMAKE([-Wall -Werror foreign])

    AC_CONFIG_FILES([Makefile \
    i18n/Makefile \
    resources/Makefile webrunner/Makefile])
    AC_OUTPUT

5)Update config.xml.wgt:

    <widget id='http://tizen.org/test/wrt-i18nmanu-tizen-tests' xmlns='http://www.w3.org/ns/widgets' xmlns:tizen='http://tizen.org/ns/widgets' version='1.0.0.1'>
      <access origin="*"/>
      <icon src="icon.png" height="117" width="117"/>
      <name>wrt-i18nmanu-tizen-tests</name>
      <tizen:application id="i18ntestcs.wrti18ntizentests" package="i18ntestcs" required_version="2.2"/>
      <tizen:setting screen-orientation="landscape"/>
    </widget>


6)Add new cases to the test suite.

## 8 How to Contribute New Cases to Test Suite Package

To contribute new cases to test suite package, perform the following steps:

1)Design new test case according to WRT Spec and add new case information to **tests.xml**. For details, see "Appendix 1 Tests.full.xml and tests.xml."

- "Case name" should follow the test case naming convention. For details, see chapter 4 "Test Case Naming Convention".
- "Specs" field should follow the Spec coverage assertion rules. For details, see chapter **Error! Reference source not found.** "Test Case Classification (<testcase\> field in tests.xml)".
- "Component" field should comply with the WRT component name list.

2)Develop test script by following the test case coding style and put it under <testcasefolder\>.

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

## 9 How to Contribute pairwise Cases to Test Suite Package

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


## Appendix 1 Tests.full.xml and tests.xml
Each test suite package has two dedicated .xml files (tests.full.xml and tests.xml), which defines all test cases in the package.
Tests.xml is a simplified version of tests.full.xml; it contains the minimum required elements when running the tests.
Note: The .xml files must comply with the rules in the test\_definition.xsd file. For details, see  [https://github.com/testkit/testkit-lite/blob/master/xsd/test\_definition.xsd](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

Tests.full.xml Example:

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
    <test_definition>
      <suite name="wrt-i18nmanu-tizen-tests" category="Crosswalk_I18n" launcher="xwalk">
        <set name="i18n" type="js">
          <testcase purpose="Validate if the web app can show 'Web' Test when settings language is set to English" type="Functional" status="approved" component="Crosswalk I18n" execution_type="manual" priority="P1" id="Crosswalk_I18n_TestEn">
            <description>
              <pre_condition>
                Make sure Crosswalk application is launched.
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
                Make sure Crosswalk application is launched.
              </pre_condition>
              <test_script_entry>/opt/wrt-i18nmanu-tizen-tests/i18n/Crosswalk_I18n_TestEn.html</test_script_entry>
            </description>
          </testcase>
         </set>
      </suite>
    </test_definition>

