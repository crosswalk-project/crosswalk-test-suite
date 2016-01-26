# Tests.xml definition and sample

Each test suite has two dedicated XML files, `tests.full.xml` and `tests.xml`. 
They define all test cases in the test suite package. They are used as input of
[testkit-lite](https://github.com/testkit/testkit-lite) tool to run the tests. 
The elements of `tests.*.xml` are defined in [test definition schema](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

## `tests.full.xml`

The `tests.full.xml` file shall contain all elements defined by [test definition
schema](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

Example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="W3C/HTML5 APIs" name="tct-2dtransforms-css3-tests">
    <set name="2DTransforms" type="js">
      <testcase component="W3C_HTML5 APIs/DOM, Forms and Styles/CSS Transforms" execution_type="auto" id="2dtransform_property_exist" priority="P1" purpose="Test 2dtransform property existence" status="approved" type="compliance" subcase="4">
        <description>
          <test_script_entry>/opt/tct-2dtransforms-css3-tests/2dtransforms/2dtransform_property_exist.html</test_script_entry>
        </description>
        <specs>
          <spec>
            <spec_assertion category="Tizen W3C API Specifications" element_name="perspective-origin" element_type="property" interface="CSS" section="DOM, Forms and Styles" specification="CSS 2D Transforms"/>
            <spec_url>http://www.w3.org/TR/2012/WD-css3-transforms-20120911/</spec_url>
            <spec_statement/>
          </spec>
        </specs>
      </testcase>
    </set>
  </suite>
</test_definition>
```

## `tests.xml`

The `tests.xml` file is a simplified version of the `tests.full.xml` file. It
contains minimum required elements for running the tests, such as `id`,
`execution_type`, `purpose`, `subcase`, `onload_delay` , `component` for a test
case. One can use the
[xmlsimplifier](https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/tools/xmlsimplifier)
tool to generate `tests.xml` from `tests.full.xml` file.

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="W3C/HTML5 APIs" name="tct-2dtransforms-css3-tests">
    <set name="2DTransforms" type="js">
      <testcase component="W3C_HTML5 APIs/DOM, Forms and Styles/CSS Transforms" execution_type="auto" id="2dtransform_property_exist" purpose="Test 2dtransform property existence" subcase="4">
        <description>
          <test_script_entry>/opt/tct-2dtransforms-css3-tests/2dtransforms/2dtransform_property_exist.html</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

# Tests.xml samples for supporting different test type
##Web Test Type 
### "js" type
The regular auto js tests

Example

refer to [tests.xml](##tests.xml)

### "ref" type
The reference style web test case

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="W3C/HTML5 APIs" name="tct-audio-html5-tests">
  ...
    <set name="Audio-ref" type="ref" ui-auto="wd">
      <testcase component="W3C_HTML5 APIs/Media/HTML5 The audio element" execution_type="manual" id="audio_one_inside_image_not_show" purpose="Check that image content inside the audio element can not be shown.">
        <description>
          <test_script_entry test_script_expected_result="0">/opt/tct-audio-html5-tests/audio/w3c/audio_001-manual.htm</test_script_entry>
          <refer_test_script_entry timeout="90">/opt/tct-audio-html5-tests/audio/w3c/audio_content-ref.htm</refer_test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```
### "wrt" type
The test contains test application, need testkit-lite to support install/uninstall test Apps by test set name. 

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Runtime" name="wrt-rt-linux-tests">
    <set name="connectsrccrossoriginmultixmlhttprequestallowedtwo" type="wrt">
      <testcase component="Crosswalk WRT/CSP" execution_type="auto" id="connectsrccrossoriginmultixmlhttprequestallowedtwo" priority="P1" purpose="Check if user agent is able to open second allowed external resource by xhr when connect-src is cross-origin.">
        <description>
          <test_script_entry test_script_expected_result="0">test_index.html</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

### "qunit" type
The qunit style test

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="SIMD" name="webapi-simd-nonw3c-tests">
    <set name="webapi-simd-nonw3c-tests" type="qunit">
      <testcase component="Supplementary APIs/Experimental/SIMD" execution_type="auto" id="Float32x4_constructor" purpose="Check Float32x4 constructor (0, 2, 2)" subcase="6">
        <description>
          <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=1</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```
### "nodeunit" type
The test load with node js unit test runner

Example:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
    <set name="common_module" type="nodeunit">
      <testcase component="Crosswalk App Tools/Common Module" execution_type="auto" id="Crosswalk_android_platform" purpose="Android - Validate if Crosswalk version is valid or invalid">
        <description>
          <test_script_entry>/opt/apptools-android-tests/tools/crosswalk-app-tools/android/test/android-platform.js</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```
##Core Test Type 
### "script" type
The test case with directly script execution entry

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk WRT" name="wrt-sharedmode-android-tests">
    <set name="android" type="script">
      <testcase component="Crosswalk WRT/Shared Mode" execution_type="auto" id="Crosswalk_ShareMode_Library_Install_test" purpose="Check install xwalk lib">
        <description>
          <test_script_entry test_script_expected_result="0" timeout="180">/opt/wrt-sharedmode-android-tests/sharedmode/Crosswalk_ShareMode_Library_Install_test.sh</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

### "pyunit" type
The test load with pyunit test module.

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk App Tools" name="apptools-android-tests">
    <set name="CLI" type="pyunit">
      <testcase component="Crosswalk App Tools/CLI" execution_type="auto" id="Crosswalk_create_no_sdk" purpose="Android - Validate if project is created fail without android sdk">
        <description>
          <test_script_entry>/opt/apptools-android-tests/apptools/create_no_sdk.py</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```
### "androidunit" type
The test load with android unit test runner

Example:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite name="webapi-embeddingapi-xwalk-tests" category="Android embedding APIs">
    <set name="EmbeddingApiTest" type="androidunit" location="device">
      <testcase component="Crosswalk APIs/Embedding API" execution_type="auto" id="v1.LoadTest" purpose="Check if the load related methods are effective." subcase="18">
        <description>
          <test_script_entry>org.xwalk.embedding.test.v1.LoadTest</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```
