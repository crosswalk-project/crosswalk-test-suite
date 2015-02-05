# Web Test Suite SIMD DeveloperGuide

## 1. Overview

This document is intended for developers who contribute SIMD test cases development.

You are supposed to have gained the following knowledge:

- Where to download WebAPI test source codes and how to run them
- How to download and run Testkit-lite
- What is QUnit, which can be used by Testkit-lite to support the execution of SIMD tests

    Note: Testkit-lite is a test execution framework. For details, see [https://github.com/testkit/testkit-lite](https://github.com/testkit/testkit-lite).

## 2. Test Suite Source Layout

The layout of test source codes should:

- Meet the requirements of Testkit-lite
- Meet the requirements of QUnit
- Meet project requirements, for example, support different package formats so that tests can be executed on various platforms

The test suite source layout is detailed as follows:

<webapi-simd-nonw3c-tests\>/

├── autogen

├── configure.ac

├── config.xml.crx

├── config.xml.wgt

├── COPYING

├── icon.png

├── inst.sh.apk

├── inst.sh.ivi

├── inst.sh.wgt

├── inst.sh.xpk

├── Makefile.am

├── manifest.json

├── pack.sh

├──[README]

├── resources/

├── testcase.xsl

├── testresult.xsl

├── tests.css

├── tests.xml

├── tests.full.xml

├── simd/

├── webapi-simd-nonw3c-tests.spec


- webapi-simd-nonw3c-tests: name of SIMD test package. The 'webapi-' prefix and the '-tests' suffix must be available.
- Documents:
  - README: an introduction of the test suite, and (optional) pre-/post-conditions.
  - COPYING: license and copying file

- Test-related files and folders:
  - simd/: a serial of source files or directories for SIMD test cases that are well organized by components or features to be tested
  - full.xml & tests.xml: a mandatory file to describe all test cases for this test suite. For details, see "Appendix 1 Tests.full.xml and tests.xml."

- QUnit support:
  - simd/ecmascript_simd/src/external/: integrated from [http://qunitjs.com] to include common test functions

- Build/pack support:
  - autogen, configure.ac, and Makefile.am
  - pack.sh: script for generating a zip package
  - inst.sh.apk: script for installing the apk package on Android mobile.
  - inst.sh.ivi: script for installing the xpk package on Tizen IVI device.
  - inst.sh.wgt: script for installing the wgt package on Tizen mobile.
  - inst.sh.xpk: script for installing the xpk package on Tizen mobile.
  - config.xml.crx: configuration file for creating a .crx extension
  - config.xml.wgt: configuration file for creating a .wgt package
  - icon.png: Widget/Extension icon
  - manifest.json: manifest file for creating a .crx extension
  - webapi-simd-nonw3c-tests.spec: specification file including version and configuration for setting suite signature; please set src\_file to keep the source code files in packaged test suite and put specific files to be kept in whitelist. For WebAPI specifications, the 'webapi-' prefix and the '-tests' suffix must be available.



The following files and folders are mandatory in :

- autogen
- config.ac
- config.xml.crx
- config.xml.wgt
- icon.png
- inst.sh.apk
- inst.sh.ivi
- inst.sh.wgt
- inst.sh.xpk
- Makefile.am
- manifest.json
- pack.sh
- resources/
- testcase.xsl
- testresult.xsl
- tests.css
- tests.xml
- tests.full.xml
- webapi-simd-nonw3c-tests.spec

## 3. How to Contribute New Cases to SIMD

To contribute new cases to SIMD, perform the following steps:

1)Design new test case according to SIMD Spec and add new case information to **tests.xml**. For details, see "Appendix 1 Tests.full.xml and tests.xml."

- "Case name" should follow the test case naming convention. For details, see chapter 4 "Test Case Naming Convention".
- "Specs" field should follow the Spec coverage assertion rules. For details, see chapter **Error! Reference source not found.** "Test Case Classification (<testcase\> field in tests.xml)".
- "Component" field should comply with the WebAPI component name list. For details see "Appendix 3 WebAPI Component Name List".
- "subcase" should be the number of sub-case in the test case, A assert judge sentence would be treat as one sub-case.

**Example**

      test("Check if the zero function of float32x4 can change the parameter to 0.0", function() {
        var z1 = SIMD.float32x4.zero();
        equal(0.0, z1.x, "the value of z1.x should be 0.0");
        equal(0.0, z1.y, "the value of z1.y should be 0.0");
        equal(0.0, z1.z, "the value of z1.z should be 0.0");
        equal(0.0, z1.w, "the value of z1.w should be 0.0");
      });

There are 4 sub-case in this case.

2)Develop test script by following the test case coding style and put it under <simd\>.

Note:

- Each test should have an entry HTML file.
- The test script can be embedded into the HTML file or be used as separate JavaScript file.
- For details on how to use QUnit, see http://qunitjs.com.

**Example**

    <!DOCTYPE html>
    <meta charset='utf-8'>
    <title>SIMD Test: float32x4</title>
    <link rel="author" title="Intel" href="http://www.intel.com">
    <link rel="help" href="https://github.com/johnmccutchan/ecmascript_simd/blob/master/README.md">
    <link rel="stylesheet" href="ecmascript_simd/src/external/qunit.css">
    <script src="ecmascript_simd/src/external/qunit.js"></script>
    <div id="qunit"></div>
    <div id="qunit-fixture"></div>
    <script>

      test("Check if the zero function of float32x4 can change the parameter to 0.0", function() {
        var z1 = SIMD.float32x4.zero();
        equal(0.0, z1.x, "the value of z1.x should be 0.0");
        equal(0.0, z1.y, "the value of z1.y should be 0.0");
        equal(0.0, z1.z, "the value of z1.z should be 0.0");
        equal(0.0, z1.w, "the value of z1.w should be 0.0");
      });

      test("Check if the splat function of float32x4 can change the parameter to specified value", function () {
        var z2 = SIMD.float32x4.splat(5.0);
        equal(5.0, z2.x, "the value of z2.x should be 5.0");
        equal(5.0, z2.y, "the value of z2.y should be 5.0");
        equal(5.0, z2.z, "the value of z2.z should be 5.0");
        equal(5.0, z2.w, "the value of z2.w should be 5.0");
      });

    </script>



## Appendix 1 Tests.full.xml and tests.xml
SIMD has two dedicated .xml files (tests.full.xml and tests.xml), which defines all test cases in the package.
Tests.xml is a simplified version of tests.full.xml; it contains the minimum required elements when running the tests.
Note: The .xml files must comply with the rules in the test\_definition.xsd file. For details, see  [https://github.com/testkit/testkit-lite/blob/master/xsd/test\_definition.xsd](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

Tests.full.xml Example:

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
    <test_definition>
      <suite name="webapi-simd-nonw3c-tests" launcher="xwalk" category="SIMD">
        <set name="webapi-simd-nonw3c-tests">
          <testcase purpose="Check float32x4 constructor (0, 2, 2)" type="compliance" status="approved" component="WebAPI/Supplementary API Reference/SIMD" execution_type="auto" priority="P1" subcase="2" id="float32x4_constructor">
            <description>
              <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=1</test_script_entry>
            </description>
            <specs>
              <spec>
                <spec_assertion element_type="method" element_name="float32x4" interface="SIMD" specification="SIMD" section="SIMD" category="Supplementary API Specifications"/>
                <spec_url>https://github.com/johnmccutchan/ecmascript_simd/blob/master/README.md</spec_url>
                <spec_statement/>
              </spec>
            </specs>
          </testcase>
          <testcase purpose="Check float32x4 scalar getters (0, 4, 4)" type="compliance" status="approved" component="WebAPI/Supplementary API Reference/SIMD" execution_type="auto" priority="P1" subcase="4" id="float32x4_scalar_getters">
            <description>
              <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=2</test_script_entry>
            </description>
            <specs>
              <spec>
                <spec_assertion element_type="method" element_name="float32x4" interface="SIMD" specification="SIMD" section="SIMD" category="Supplementary API Specifications"/>
                  <spec_url>https://github.com/johnmccutchan/ecmascript_simd/blob/master/README.md</spec_url>
                <spec_statement/>
              </spec>
            </specs>
          </testcase>
         </set>
      </suite>
    </test_definition>

Tests.xml Example.

    <?xml version="1.0" encoding="UTF-8"?>
    <?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
    <test_definition>
      <suite category="SIMD" launcher="xwalk" name="webapi-simd-nonw3c-tests">
        <set name="webapi-simd-nonw3c-tests">
          <testcase component="WebAPI/Supplementary API Reference/SIMD" execution_type="auto" id="float32x4_constructor" purpose="Check float32x4 constructor (0, 2, 2)" subcase="2">
            <description>
              <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=1</test_script_entry>
            </description>
          </testcase>
          <testcase component="WebAPI/Supplementary API Reference/SIMD" execution_type="auto" id="float32x4_scalar_getters" purpose="Check float32x4 scalar getters (0, 4, 4)" subcase="4">
            <description>
              <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=2</test_script_entry>
            </description>
          </testcase>
         </set>
      </suite>
    </test_definition>

