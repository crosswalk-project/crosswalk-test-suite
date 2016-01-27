# Tests.xml definition and sample

Each test suite has two dedicated XML files, `tests.full.xml` and `tests.xml`.
They define all test cases in the test suite package. They are used as input of
[testkit-lite](https://github.com/testkit/testkit-lite) tool to run the tests. 
The elements of `tests.*.xml` are defined in [test definition 
schema](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).

## `tests.full.xml`

The `tests.full.xml` file shall contain all elements defined by [test definition
schema](https://github.com/testkit/testkit-lite/blob/master/xsd/test_definition.xsd).
There are several web test types and core test types in Crosswalk test suites, 
Different test types request different elements in XML.Following are `tests.full.xml`
 samples for different test type.

### Web Test Type

#### `js` type

JavaScript tests based on W3C testharness.

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

#### `ref` type

The [reftest](http://testthewebforward.org/docs/reftests.html)

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="W3C/HTML5 APIs" name="tct-audio-html5-tests">
    <set name="Audio-ref" type="ref" ui-auto="wd">
      <testcase component="W3C_HTML5 APIs/Media/HTML5 The audio element" execution_type="manual" id="audio_one_inside_image_not_show" priority="P3" purpose="Check that image content inside the audio element can not be shown." status="approved" type="compliance">
        <description>
          <test_script_entry test_script_expected_result="0">/opt/tct-audio-html5-tests/audio/w3c/audio_001-manual.htm</test_script_entry>
          <refer_test_script_entry timeout="90">/opt/tct-audio-html5-tests/audio/w3c/audio_content-ref.htm</refer_test_script_entry>
        </description>
        <specs>
          <spec>
            <spec_assertion category="Tizen W3C API Specifications" interface="HTMLAudioElement" section="Media" specification="HTML5 The audio element" usage="true"/>
            <spec_url>http://www.w3.org/TR/2012/WD-html5-20121025/media-elements.html#htmlmediaelement</spec_url>
            <spec_statement/>
          </spec>
        </specs>
      </testcase>
    </set>
  </suite>
</test_definition>
```
#### `wrt` type

The test contains test application named by `<set>`, which needs testkit-lite to support install/uninstall test Application. 

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Runtime" name="wrt-rt-linux-tests">
    <set name="connectsrccrossoriginmultixmlhttprequestallowedtwo" type="wrt">
     <testcase component="Crosswalk WRT/CSP" execution_type="auto" id="connectsrccrossoriginmultixmlhttprequestallowedtwo" priority="P1" purpose="Check if user agent is able to open second allowed external resource by xhr when connect-src is cross-origin." status="approved" type="compliance">
        <description>
          <pre_condition/>
          <post_condition/>
          <steps>
            <step order="1">
              <step_desc>Check if user agent is able to open second allowed external resource by xhr when connect-src is cross-origin.</step_desc>
              <expected>PASS</expected>
            </step>
          </steps>
          <test_script_entry test_script_expected_result="0">test_index.html</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

#### `qunit` type

The [qunit](https://qunitjs.com/) stype test

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="SIMD" name="webapi-simd-nonw3c-tests">
    <set name="webapi-simd-nonw3c-tests" type="qunit">
      <testcase component="Supplementary APIs/Experimental/SIMD" execution_type="auto" id="Float32x4_constructor" priority="P1" purpose="Check Float32x4 constructor (0, 2, 2)" status="approved" subcase="6" type="compliance">
        <description>
          <test_script_entry>/opt/webapi-simd-nonw3c-tests/simd/ecmascript_simd/src/index.html?testNumber=1</test_script_entry>
        </description>
        <specs>
          <spec>
            <spec_assertion category="SIMD" element_name="Float32x4" element_type="method" interface="SIMD" section="SIMD" specification="SIMD"/>
            <spec_url>https://github.com/johnmccutchan/ecmascript_simd/blob/master/README.md</spec_url>
            <spec_statement/>
          </spec>
        </specs>
      </testcase>
    </set>
  </suite>
</test_definition>
```

#### `nodeunit` type

The [nodeunit](https://github.com/caolan/nodeunit) style test, which load with nodeunit.js test runner

Example:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk App Tools" name="apptools-android-tests">
    <set name="common_module" type="nodeunit">
      <testcase component="Crosswalk App Tools/CLI" execution_type="auto" id="Crosswalk_create_no_sdk" priority="P2" purpose="Android - Validate if project is created fail without android sdk" status="approved" type="Functional">
        <description>
          <test_script_entry>/opt/apptools-android-tests/apptools/create_no_sdk.py</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

### Core Test Type 

#### `script` (default) type 

The script test which testkit-lite directly execute the script in `<test_script_entry>`. 

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk WRT" name="wrt-sharedmode-android-tests">
    <set name="android" type="script">
      <testcase component="Crosswalk WRT/Shared Mode" execution_type="auto" id="Crosswalk_ShareMode_Library_Install_test" priority="P1" purpose="Check install xwalk lib" status="approved" type="Functional">
        <description>
          <pre_condition>
          </pre_condition>
          <test_script_entry test_script_expected_result="0" timeout="180">/opt/wrt-sharedmode-android-tests/sharedmode/Crosswalk_ShareMode_Library_Install_test.sh</test_script_entry>
        </description>
        </testcase>
    </set>
  </suite>
</test_definition>
```

#### `pyunit` type

The [pyunit](https://docs.python.org/2/library/unittest.html) style test, which need to load the `pyunit` module.

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite category="Crosswalk App Tools" name="apptools-android-tests">
    <set name="CLI" type="pyunit">
      <testcase component="Crosswalk App Tools/CLI" execution_type="auto" id="Crosswalk_create_no_sdk" priority="P2" purpose="Android - Validate if project is created fail without android sdk" status="approved" type="Functional">
        <description>
          <test_script_entry>/opt/apptools-android-tests/apptools/create_no_sdk.py</test_script_entry>
        </description>
      </testcase>
    </set>
  </suite>
</test_definition>
```

#### `androidunit` type


The [androidunit](http://developer.android.com/training/testing/unit-testing/index.html) style test, which load with android unit test runner.

Example:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>
<test_definition>
  <suite name="webapi-embeddingapi-xwalk-tests" category="Android embedding APIs">
    <set name="EmbeddingApiTest" type="androidunit" location="device">
      <testcase component="Crosswalk APIs/Embedding API" execution_type="auto" id="v1.LoadTest" platform="android" priority="P1" purpose="Check if the load related methods are effective." status="approved" type="functional_positive" subcase="18">
        <description>
          <test_script_entry>org.xwalk.embedding.test.v1.LoadTest</test_script_entry>
        </description>
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
