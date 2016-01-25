# Tests.xml definition and sample

Each test suite has two dedicated XML files, `tests.full.xml` and `tests.xml`.
They define all test cases in the test suite package. They are used as input of
[testkit-lite](https://github.com/testkit/testkit-lite) tool to run the tests.

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
