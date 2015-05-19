# Cordova Test Suite Developer Guide

## 1. Overview

This document is intended for developers who contribute Cordova test cases development.

You are supposed to have gained the following knowledge:

- Where to download Cordova test source codes and how to run them
- How to download and run Testkit-lite

    Note: Testkit-lite is a test execution framework. For details, see [https://github.com/testkit/testkit-lite](https://github.com/testkit/testkit-lite).

## 2. Test Suite Source Layout

The layout of test source codes should:

- Meet the requirements of Testkit-lite
- Meet project requirements, for example, support different package formats so that tests can be executed on various platforms

The test suite source layout is detailed as follows:

&lt;cordova-xxx-tests&gt;/

├── autogen

├── [common]/

├── configure.ac

├── config.xml.crx

├── config.xml.wgt

├── COPYING

├── icon.png

├── inst.sh.apk

├── inst.sh.wgt

├── inst.sh.xpk

├── Makefile.am

├── manifest.json

├── pack.py

├── [README]

├── webrunner/

├── suite.json

├── testcase.xsl

├── testresult.xsl

├── tests.css

├── tests.xml

├── tests.full.xml

├── &lt;testcasefolder&gt;/

├── &lt;cordova-xxx-tests&gt;.spec

├── [utils]/

└── [data]/

- &lt;cordova-xxx-tests&gt;/: name of Cordova test package. The 'cordova-' prefix and the '-tests' suffix must be available, for example, cordova-feature-android-tests.
- Documents:
  - README: an introduction of the test suite, and (optional) pre-/post-conditions.
  - COPYING: license and copying file

- Test-related files and folders:
  - &lt;testcasefolder&gt;/: a serial of source files or directories for test cases that are well organized by components or features to be tested, e.g. sampleapp/xxx, webapp/xxx
  - full.xml & tests.xml: a mandatory file to describe all test cases for this test suite. For details, see "Appendix 2 Tests.full.xml and tests.xml."

- Build/pack support:
  - autogen, configure.ac, and Makefile.am
  - pack.py: script for generating a zip package, this py is maintained in crosswalk-test-suite/tools/.
  - inst.sh.apk: script for installing the apk package on Android mobile..
  - inst.sh.wgt: script for installing the wgt package on Tizen mobile.
  - inst.sh.xpk: script for installing the xpk package on Tizen mobile.
  - config.xml.crx: configuration file for creating a .crx extension
  - config.xml.wgt: configuration file for creating a .wgt package
  - icon.png: Widget/Extension icon
  - manifest.json: manifest file for creating a .crx extension
  - &lt;cordova-xxx-tests&gt;.spec: specification file including version and configuration for setting suite signature; please set src\_file to keep the source code files in packaged test suite and put specific files to be kept in whitelist. For Cordova specifications, the 'cordova-' prefix and the '-tests' suffix must be available, for example, cordova-feature-android-tests.spec.

- Installation/execution support:
  - webrunner/: web test runner for executing Cordova test suite. It is integrated from and updated with Testkit-lite. For details, see https://github.com/testkit/testkit-lite.

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
- inst.sh.apk
- inst.sh.wgt
- inst.sh.xpk
- Makefile.am
- manifest.json
- pack.py
- webrunner/
- testcase.xsl
- testresult.xsl
- tests.css
- tests.xml
- tests.full.xml
- &lt;cordova-xxx-tests&gt;.spec

## 3. Test Case Coding Style

Refer to the `Coding_Style_Guide_CheatSheet.md`.

## 4. Test Case Naming Convention

**Template**

[SpecShortName]\_&lt;APIInterface&gt;\_&lt;ShortDescriptionForTestPurpose&gt;

A test case should be named as per the following conventions:

- [SpecShortName] is optional, mostly for similar specifications, e.g. Crosswalk
- &lt;APIInterface&gt; and &lt;ShortDescriptionForTestPurpose&gt;  are mandatory.
- Use lowercase, except API name and constant defined in spec
- Use descriptive names (e.g. ftp\_file\_send); Do not use numbers as tests name (e.g. \_001, \_002)
- Use '\_' to connect words in file names (do not use @&- in case name, though W3C prefer '-' to '\_')

**Examples**

Crosswalk\_Cordova\_webapp\_install.html

remote\_debug\_breakpoints.html


## 5. Test Case Folder Naming Convention

A test case folder should be named as per the following conventions:

- Allow only letter, digit, and hyphen in test case folder name.
- For folder name, please also use lower-case with '-' if necessary.
- Name &lt;testcasefolder&gt; as a spec, component or sub-component, for example, webapp/, feature/.

## 6. Test Case Classification (&lt;testcase\\&gt; field in tests.xml)

**Template**

    <testcase purpose="" type="" status="" component="" execution_type="" priority="" id=""\>

Test case created should be classified by the following rules:

- Purpose: test assertion; should be unique in whole tests.xml (no duplicate test case).
- Type: currently only support 'compliance'.
- Status: test case status
  - designed: test case is just designed but notready for review.
  - ready: test case is ready for review.
  - approved: test case is reviewed and qualified to be released; currently only use this status when merge tests into test suites.

- Component: should comply with the Cordova component name list. Such as Cordova_Feature
- Execution\_type:
  - auto:
  - manual:

- Priority: P0/P1/P2/P3
  - P0: use cases for feature to be tested, API use cases; P0 tests will be used in sanity testing.
  - P1: feature verification tests, API and its attribute presence and normal usage; P0+P1 tests will be used in feature verification testing.
  - P2: positive tests of extended feature tests, API parameter combination tests.
  - P3: negative tests of extended feature tests, API spec descriptive statement tests, complicated use cases, stress tests; P0+P1+P2+P3 tests will be used in full-pass testing.
  - Attribute & Method Coverage - cover each attribute or method at least once by using normal values to ensure the presence of all defined attributes and methods. P0+P1 tests are full tests of Attribute & Method Coverage.
  - Parameter Coverage - a superset of Attribute & Method coverage, which covers each parameter using minimum, maximum, normal, and error conditions of each range of values, parameter combination for the APIs with more than one parameter, and all return codes. P0+P1+P2 tests are full tests of Parameter Coverage.
  - Statement Coverage - a superset of parameter coverage, which covers testable statement, including common usage, error code (exceptions), code examples, and etc testable descriptive statements in each specification document. P0+P1+P2+P3 tests are full tests of Statement Coverage.

- Id: test case identification should be unique in whole tests.xml (no duplicate test case); can be simply as test case name without extension.

**Example**

    <testcase purpose="Validate 'cordova_mobile_spec' app can be installed successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Feature_install"\>


## 8. How to Add New Test Suite to Cordova
To add a new suite to Cordova, perform the following steps:

1) Fork and clone the crosswalk-test-suite project from

  [https://github.com/crosswalk-project/crosswalk-test-suite](https://github.com/crosswalk-project/crosswalk-test-suite)

  **Note** : you must sign up for the GitHub first.

2) Copy a test suite to the spec under testing, for example, "cordova-feature-android-tests".

3) Replace feature with real test case folder name in Makefile.am:

    commondir = webrunner
    SUBDIRS = feature $(commondir)
    docdir = /opt/cordova-feature-android-tests
    dist_doc_DATA = COPYING README tests.xml tests.full.xml

4) Replace feature with the name of the real test suite and replace feature with real test case folder name used in configure.ac:

    AC_INIT([cordova-feature-android-tests], [6.35.1.2], [zhiqiang.zhang@intel.com])
    AM_INIT_AUTOMAKE([-Wall -Werror foreign])
    AC_CONFIG_FILES([Makefile \
    feature/Makefile \
    webrunner/Makefile])
    AC_OUTPUT

5) Update config.xml.crx:

    <widget xmlns="http://www.w3.org/ns/widgets">
    </widget>

6) Update config.xml.wgt:

    <widget id='http://tizen.org/test/cordova-feature-android-tests' xmlns='http://www.w3.org/ns/widgets' xmlns:tizen='http://tizen.org/ns/widgets'>
      <access origin="*"/>
      <icon src="icon.png" height="117" width="117"/>
      <name>cordova-feature-android-tests</name>
      <tizen:application id="cordovatest.CordovaFeatureAndroidTests" package="cordovatest" required_version="2.2"/>
      <tizen:setting screen-orientation="landscape"/>
    </widget>

7) Update manifest.json:

    {
        "xwalk_version": "0.0.1",
        "name": "cordova-feature-android-tests",
        "xwalk_description": "cordova-feature-android-tests",
        "start_url": "index.html",
        "icons": [{ "src": "icon.png", "sizes": "128x128"}]
    }

8) Customize the .spec file based on the cordova-feature-android-tests.spec file.

9) Add new cases to the test suite. For details, see chapter 9 "How to Contribute New Cases to Test Suite Package."

## 9 How to Contribute New Cases to Test Suite Package

To contribute new cases to test suite package, perform the following steps:

1) Design new test case according to Cordova Spec and add new case information to **tests.xml**. For details, see "Appendix 1 Tests.full.xml and tests.xml."

- "Case name" should follow the test case naming convention. For details, see chapter 4 "Test Case Naming Convention".
- "Specs" field should follow the Spec coverage assertion rules. For details, see chapter **Error! Reference source not found.** "Test Case Classification (<testcase\> field in tests.xml)".
- "Component": should comply with the Cordova component name list. Such as Cordova_Feature

2) Develop test script by following the test case coding style and put it under <testcasefolder\>.

Note:

- Each test should have an entry HTML file.
- The test script can be embedded into the HTML file or be used as separate JavaScript file.


**Example**

    <meta charset='utf-8'>
    <title>Cordova Test: Mobile Spec - Install</title>
    <link rel="author" title="Intel" href="http://www.intel.com">
    <p><strong>Test steps:</strong></p>
    <ol>
      <li>Install the Cordova app on Android OS using the following command: "adb install -r cordova_mobile_spec-debug.apk"</li>
      <li>Check if the installation woks fine</li>
    </ol>
    <p><strong>Expected Output:</strong></p>
    <ol>
      <li>The 'cordova_mobile_spec' app can begin to install</li>
      <li>No errors occur and the 'cordova_mobile_spec' app can be intalled successfully</li>
    </ol>


## Appendix 1 Tests.full.xml and tests.xml
Each test suite package has two dedicated .xml files (tests.full.xml and tests.xml), which defines all test cases in the package.
Tests.xml is a simplified version of tests.full.xml; it contains the minimum required elements when running the tests.
Note: The .xml files must comply with the rules in the test\_definition.xsd file. For details, see  [https://github.com/testkit/testkit-lite/blob/master/xsd/test\_definition.xsd](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

Tests.full.xml Example:

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
    <test_definition>
      <suite name="cordova-feature-android-tests" category="Cordova_Feature" launcher="xwalk">
        <set name="Feature" type="js">
          <testcase purpose="Validate if 'cordova_mobile_spec' app icon display normally" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Mobile_Spec_Icon">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec.apk' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Icon.html</test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app can be installed successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Mobile_Spec_Install">
            <description>
              <pre_condition>
                1. Make sure the 'cordova_mobile_spec.apk' package has existed in the local;
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Install.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app can be uninstalled successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Mobile_Spec_Uninstall">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec.apk' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
               <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Uninstall.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec'  app can be launched successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Mobile_Spec_Launch">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
               <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Launch.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app can be closed successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Mobile_Spec_Close">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec' app is launched;
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Close.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app could debug by remote host" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Remote_Debug_Connection">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' is installed.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Connection.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app could be checked by remote debug" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P1" id="CrossWalk_Cordova_Remote_Debug_CheckInfo">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app info is  shown in the spection page.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_CheckInfo.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate 'cordova_mobile_spec' app could be added Breakpoints by remote debug" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P1" id="CrossWalk_Cordova_Remote_Debug_Breakpoints">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app info is  shown in the spection page.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Breakpoints.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate CrossWalk viewed webpage could be modified by remote debug" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P1" id="CrossWalk_Cordova_Remote_Debug_Modification">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app lanunched by remote debug mode.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Modification.html </test_script_entry>
            </description>
          </testcase>
          <testcase purpose="Validate Cordova debug apk could be packed successfully" type="Functional" status="approved" component="Cordova_Feature" execution_type="manual" priority="P0" id="CrossWalk_Cordova_Remote_Debug_Pack">
            <description>
              <pre_condition>
                1. Make sure 'crosswalk-cordova-version-arm.apk' is download to local
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Pack.html </test_script_entry>
            </description>
          </testcase>
        </set>
      </suite>
    </test_definition>

Tests.xml Example.

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
    <test_definition>
      <suite category="Cordova_Feature" launcher="xwalk" name="cordova-feature-android-tests">
        <set name="feature" type="js">
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Mobile_Spec_Icon" purpose="Validate if 'cordova_mobile_spec' app icon display normally">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec.apk' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Icon.html</test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Mobile_Spec_Install" purpose="Validate 'cordova_mobile_spec' app can be installed successfully">
            <description>
              <pre_condition>
                1. Make sure the 'cordova_mobile_spec.apk' package has existed in the local;
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Install.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Mobile_Spec_Uninstall" purpose="Validate 'cordova_mobile_spec' app can be uninstalled successfully">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec.apk' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Uninstall.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Mobile_Spec_Launch" purpose="Validate 'cordova_mobile_spec'  app can be launched successfully">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec' app is installed;
                2. Make sure there some webapps are available.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Launch.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Mobile_Spec_Close" purpose="Validate 'cordova_mobile_spec' app can be closed successfully">
            <description>
              <pre_condition>
                1. Make sure 'cordova_mobile_spec' app is launched;
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Mobile_Spec_Close.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Remote_Debug_Connection" purpose="Validate 'cordova_mobile_spec' app could debug by remote host">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' is installed.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Connection.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Remote_Debug_CheckInfo" purpose="Validate 'cordova_mobile_spec' app could be checked by remote debug">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app info is  shown in the spection page.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_CheckInfo.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Remote_Debug_Breakpoints" purpose="Validate 'cordova_mobile_spec' app could be added Breakpoints by remote debug">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app info is  shown in the spection page.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Breakpoints.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Remote_Debug_Modification" purpose="Validate CrossWalk viewed webpage could be modified by remote debug">
            <description>
              <pre_condition>
                1. Make sure 'mobilespec-debug.apk' app lanunched by remote debug mode.
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Modification.html </test_script_entry>
            </description>
          </testcase>
          <testcase component="Cordova_Feature" execution_type="manual" id="CrossWalk_Cordova_Remote_Debug_Pack" purpose="Validate Cordova remote debug apk could be packed successfully">
            <description>
              <pre_condition>
                1. Make sure 'crosswalk-cordova-version-arm.apk' is download to local
              </pre_condition>
              <test_script_entry>/opt/cordova-feature-android-tests/feature/CrossWalk_Cordova_Remote_Debug_Pack.html </test_script_entry>
            </description>
          </testcase>
        </set>
      </suite>
    </test_definition>

