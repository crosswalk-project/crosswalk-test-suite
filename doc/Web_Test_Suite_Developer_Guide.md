# Web Test Suite Developer Guide

## Overview

This document is intended for those who want to make test contributions to this
repository, especially to the WebAPI, Runtime and Cordova test suites.

Please formiliarize yourself with the following knowledge:

- [Git and GitHub](https://help.github.com/).
- [Testkit-lite](https://github.com/testkit/testkit-lite), a test execution
  framework for test suites in this repository.
- W3C [testharness.js](https://github.com/w3c/testharness.js), a framework for
  writing low-level tests of browser functionality in javascript. It is called
  by testkit-lite to support the test execution.

## Test suite source layout

The layout of test source code is designed to meet requirements of
`testkit-lite`, `testharness.js` and Crosswalk Project for supporting different
package formats for various platforms, such as Android, Windows, Linux (Deepin),
iOS, etc.

A typical test suite source layout looks like this:

```
<package-name>
  |- <test-case-sub-directory>
  |- [resources]
  |- [webrunner]
  |- COPYING
  |- icon.png
  |- inst.*.py
  |- README.md
  |- suite.json
  |- tests.full.xml
  |- tests.xml
  |- testcase.xsl
  |- testresult.xsl
  |- tests.css
```

Where,

- `<package-name>`: name of the test suite package, usually in
  `<type>-<module>-<category>-tests` format. See the [package and web
  application naming convention](#package-and-web-application-naming-convention)
  section for details.
- `<test-case-sub-directory>`: a serial of source files or directories for test
  cases that are well organized by components or features to be tested. See the
  [test case sub-directory naming convention](#test-case-sub-directory-naming-convention)
  section for details.
- `[resources]`: optional, [testharness.js](https://github.com/w3c/testharness.js)
  test framework resources. The resources are built into test suite package if
  specified in `suite.json`. See integrated source code
  [here](./../tools/resources/testharness).
- `[webrunner]`: a [web test runner](https://github.com/testkit/webrunner)
  supporting `testkit-lite` to run the tests. See integrated source code
  [here](./../tools/resources/webrunner).
- `COPYING`: license and copying file.
- `icon.png`: icon image for the test suite package as web application.
- `inst.*.py`: scripts to install built test suite package.
- `README.md`: a brief introduction of the test suite, and pre-/post-conditions
  (optional).
- `suite.json`: a package specification file, which provides the test suite
  package's architecture in different package types. It will be parsed by the
  pack tool (`pack.py`) when build web test suite package.
- `tests.full.xml`, `tests.xml`: files to describe all test cases for this test
  suite. See [Appendix 1](#appendix-1-testsfullxml-and-testsxml) for details.
- `testcase.xsl`, `testresult.xsl`, `tests.css`: XSLT style for test case and
  test result, used by `tests.full.xml`, `tests.xml`, etc.

## Package and web application naming convention

Typically package name is in `<type>-<module>-<category>-tests` format.

- `<type>`:
  - `tct`: test suites leveraged from Tizen Compliance Tests.
  - `webapi`: test suites checking compliance with Crosswalk Web API
    specifications.
  - `embedding`: test suites checking compliance with Crosswalk Embedding API
    specifications.
  - `wrt`: test suites checking compliance with web runtime core specification.
  - `cordova`: test suites checking cordova-plugin-crosswalk-webview.
  - `usecase`: test suites verifying Crosswalk features from end user's
    perspective.
  - `stability`: test suite checking stability.
- `<module>`: abbreviation of Web API specification or function component.
- `<category>`: origination of the API specifications or features:
  - `w3c`: standard specifications from W3C.
  - `css3`: W3C CSS3 specifications.
  - `html5`: W3C HTML5 specification.
  - `nonw3c`: supplementary API specifications from other standard orgnizations
    or browser engines other than W3C.
  - `wrt`: Crosswalk runtime core specification.
  - `andriod`: Crosswalk Project for Andriod specific features.
  - `xwalk`: other Crosswalk Web APIs, or Crosswalk features common for any
     platform.
  - `external`: Crosswalk external APIs, such as App Security API.

### Web application name after test suite packaging

Web application name is the `name` field in `manifest.json`
which is used for the application name showing on the screen after
installation, for both test suite application and sub-test application.

The `<module>` above will be used as the web application name for each test
suite. In case of duplicate names, `<module>-<category>` is to be used.

To make life easy, keep the current being application names for sub-tests,
e.g. use-case test cases.

## Test case naming convention

**Template**

`[SpecShortName]_<WebAPIInterface>_<short_description_for_test_purpose>`

- `[SpecShortName]` is optional, mostly for similar specifications,
  e.g. Selectors API Level 1, Selectors API Level 2.
- `<WebAPIInterface>` and `<short_description_for_test_purpose>` are mandatory.
- Use lowercase, except API name and constant defined in specification.
- Use descriptive names (e.g. `ftp_file_send`). Avoid numbers as tests name
  (e.g. `_001`, `_002`).
- Use `_` to connect words in file names; do not use `@&-` in case name, though
  W3C prefer `-` to `_`.

**Examples**

- `bluetooth_BluetoothAdapter_discoverDevices_exists.html` or
  `BluetoothAdapter_discoverDevices_exists.html`
- `webaudio_cancelScheduledValues_exists.html`

## Test case sub-directory naming convention

- Allow only letter, digit, and hyphen `-` in test case directory name.
- Always use lower-case letter with `-` if necessary.
- Use specification short name for `<test-case-sub-directory>`, component,
  for example, `audio`, `htmltemplates`.

## Test case coding style

See the [coding style guide cheatsheet](./Coding_Style_Guide_CheatSheet.md)
documentation.

## Test case classification

`<testcase\>` field in `tests.full.xml` files.

**Template**

```xml
<testcase purpose="" type="" status="" component="" execution_type="" priority="" id=""\>
```

Test cases will be classified by the following rules:

- `purpose`: test assertion; should be unique in whole `tests.xml` files in this
  repository; (no duplicate test case).
- `type`: currently only support `compliance` for web tests.
- `status`: test case status.
  - `designed`: test case is just designed but not ready for review.
  - `ready`: test case is ready for review.
  - `approved`: test case is reviewed and qualified to be released; currently
    only use this status when merge tests into test suites.
- `component`: should comply with the component name list. See [Appendix 2
  WebAPI Component Name List](#Appendix-2-WebAPI-specification-name-list).
- `execution_type`:
  - `auto`: automation tests.
  - `manual`: manual tests.
- `priority`: test case priority.
  - `P0`: use cases for features to be tested from end user point of view;
    P0 tests will be used for sanity testing.
  - `P1`: feature verification tests, API and its attribute presence and normal
    usage; P0+P1 tests will be used for feature verification testing.
  - `P2`: positive tests of extended feature tests, API parameter combination
    tests.
  - `P3`: negative tests of extended feature tests, API spec descriptive
    statement tests, complicated use cases, stress tests; P0+P1+P2+P3 tests
    will be used for full-pass testing.
  - **Attribute and Method Coverage**: cover each attribute or method at least
    once by using normal values to ensure the presence of all defined
    attributes and methods. P0+P1 tests are full tests of Attribute and Method
    Coverage.
  - **Parameter Coverage**: a superset of Attribute & Method coverage, which
    covers each parameter using minimum, maximum, normal, and error conditions
    of each range of values, parameter combination for the APIs with more than
    one parameter, and all return codes. P0+P1+P2 tests are full tests of
    Parameter Coverage.
  - **Statement Coverage**: a superset of parameter coverage, which covers
    testable statement, including common usage, error code (exceptions),
    code examples, and etc testable descriptive statements in each
    specification. P0+P1+P2+P3 tests are full tests of Statement Coverage.
- `id`: test case identification should be unique in whole tests.xml files
  in this repository; no duplicate test case. It can be simply as test case
  name without extension.

## Specification coverage assertion rules

`<specs\>` field in `tests.full.xml` files.

**Template**

```xml
<specs>
  <spec>
    <spec_assertion element_type="" element_name="" interface="" specification="" section="" category=""/>
    <spec_url></spec_url>
    <spec_statement></spec_statement>
  </spec>
</specs>

<specs>
  <spec>
    <spec_assertion usage= "" interface="" specification="" section="" category=""/>
    <spec_url></spec_url>
    <spec_statement></spec_statement>
  </spec>
</specs>
```

Specification coverage assertion should obey the following rules:

- `spec_assertion` element is mandatory.
  - `element_type`: `attribute` or `method`; only need for P0/P1/P2 test cases.
  - `element_name`: attribute/method name defined in `specification` field
    comes together with `element_type`.
  - `usage`: `true` if P3 test cases based on statement.
  - `interface`: interface name defined in `specification`.
  - `specification`: standard specification; mostly the 3rd part of [Appendix 2
    WebAPI Component Name List](#Appendix-2-WebAPI-specification-name-list)
  - `section`: the 2nd part of [Appendix 2 WebAPI Component Name
    List](#Appendix-2-WebAPI-specification-name-list).
    - UI
    - Content(documents,graphics,multimedia)
    - CSS3
    - Device/OSIntegration
    - Network & Communication
    - Storage
    - Performance
    - ExtraHTML5
  - `category`: the 1st part of [Appendix 2 WebAPI Component Name
    List](#Appendix-2-WebAPI-specification-name-list)
    - W3C HTML5 API Specifications
    - Supplementary API Specifications
- `spec_url` is mandatory, an URL to public specification section being tested.
- `spec_statement` is optional, statements in spec being tested.
   It must be copied from the specification document.

**Examples**

```xml
<specs>
  <spec>
    <spec_assertion element_type="attribute" element_name="screenY" interface="Touch" specification="Touch Events version 1" section="Device" category="Tizen W3C API Specifications"/>
    <spec_url>http://www.w3.org/TR/2013/WD-touch-events-20130124/#idl-def-Touch</spec_url>
    <spec_statement/>
  </spec>
</specs>

<specs>
  <spec>
    <spec_assertion element_type="attribute" element_name="clientY" interface="Touch" specification="Touch Events version 1" section="Device" category="Tizen W3C API Specifications"/>
    <spec_url>http://www.w3.org/TR/2013/WD-touch-events-20130124/#idl-def-Touch</spec_url>
    <spec_statement/>
  </spec>
</specs>
```

## How to add a new test suite?

The best method to add a new test suite is to copy a simliar existing test suite
and then update related test scripts.

1. Fork this reposistory and clone your forked repository to local system, and
   make a new branch. See http://testthewebforward.org/docs/configuration.html
1. Copy a simliar existing test suite, e.g. `webapi-style-css3-tests` to the
   place you want to make a new test suite, and rename it.
1. Update `manifest.json`.
1. Rename `<test-case-sub-directory>`.
1. Create new test cases (see next section) and update `tests*.xml` files.
1. Package the test suite and run the test cases.
1. Submit your changes in a pull request.

## How to contribute new cases?

1. Design new test case according to the specification and/or feature
   requirement, and add new case information to `tests.full.xml`.
1. Develop test script following the
   [test case naming convention](#Test-case-naming-convention) and
   [test case coding style](#test-case-coding-style), and put it under
   `<test-case-sub-directory>`.

Note:

- Each test should have an entry HTML file.
- The test script can be embedded into the HTML file or be used as separated
  JavaScript file.

## Appendix 1 `tests.full.xml` and `tests.xml`

See the [tests.xml definition and sample](./Tests_XML_Definition_and_Sample.md)
documentation.

## Appendix 2 WebAPI specification name list

- W3C API Specifications:DOM Forms:HTML5 Forms
- W3C API Specifications:DOM Forms:Selectors API Level 1
- W3C API Specifications:DOM Forms:Selectors API Level 2
- W3C API Specifications:DOM Forms:WOFF File Format 1.0
- W3C API Specifications:DOM Forms:DOM/JS related HTML5 Enhancements
- W3C API Specifications:CSS3:Media Queries
- W3C API Specifications:CSS3:CSS 2D Transforms
- W3C API Specifications:CSS3:CSS 3D Transforms Module Level 3
- W3C API Specifications:CSS3:CSS Animations Module Level 3
- W3C API Specifications:CSS3:CSS Transitions Module Level 3
- W3C API Specifications:CSS3:CSS Colors Module Level 3
- W3C API Specifications:CSS3:CSS Backgrounds and Borders Module Level 3
- W3C API Specifications:CSS3:CSS Flexible Box Layout Module
- W3C API Specifications:CSS3:CSS Multi-column Layout Module
- W3C API Specifications:CSS3:CSS Text Module Level 3
- W3C API Specifications:CSS3:CSS Basic User Interface Module Level 3
- W3C API Specifications:CSS3:CSS Fonts Module Level 3
- W3C API Specifications:Device:Touch Events version 1
- W3C API Specifications:Device:DeviceOrientation Event
- W3C API Specifications:Device:Battery Status API
- W3C API Specifications:Device:Vibration API
- W3C API Specifications:Device:HTML5 Browser state
- W3C API Specifications:Device:Screen Orientation API
- W3C API Specifications:Device:Network Information API
- W3C API Specifications:Graphics:HTML5 canvas element
- W3C API Specifications:Graphics:HTML5 2D Canvas Context
- W3C API Specifications:Graphics:HTML5 SVG
- W3C API Specifications:Media:HTML5 Audio Element
- W3C API Specifications:Media:HTML5 Video Element
- W3C API Specifications:Media:getUserMedia
- W3C API Specifications:Media:Web Audio API
- W3C API Specifications:Media:HTML Media Capture
- W3C API Specifications:Communication:The WebSocket API
- W3C API Specifications:Communication:XMLHttpRequest Level 2
- W3C API Specifications:Communication:HTML5 session history
- W3C API Specifications:Communication:Server-Sent Events
- W3C API Specifications:Communication:Web Messaging
- W3C API Specifications:Storage:Web Storage
- W3C API Specifications:Storage:File API
- W3C API Specifications:Storage:File API Directories and System
- W3C API Specifications:Storage:File API Writer
- W3C API Specifications:Storage:HTML5 Application Cache
- W3C API Specifications:Storage:Indexed Database API
- W3C API Specifications:Storage:Web SQL Database
- W3C API Specifications:Security:Cross-Origin Resource Sharing
- W3C API Specifications:Security:HTML5 iframe element
- W3C API Specifications:Security:Content Security Policy 1.0
- W3C API Specifications:UI:Clipboard API and events
- W3C API Specifications:UI:HTML5 Drag and drop
- W3C API Specifications:Performance:Web Workers
- W3C API Specifications:Performance:Page Visibility
- W3C API Specifications:Performance:Animation Timing Control
- W3C API Specifications:Performance:Navigation Timing
- W3C API Specifications:Location:Geolocation API
- Supplementary API Specifications:Typed Arrays - Khronos
- Supplementary API Specifications:WebGL - Khronos
- Supplementary API Specifications:Fullscreen API - Mozilla
- Supplementary API Specifications:viewport Metatag - Apple

## Appendix 3 WebAPI component name list

Used by `component` field in `tests.full.xml` and `tests.xml` files.

- WebAPI/Communication/HTML5 The session history of browsing contexts
- WebAPI/Communication/HTML5 Web Messaging
- WebAPI/Communication/Server-Sent Events
- WebAPI/Communication/The WebSocket API
- WebAPI/Communication/XMLHttpRequest Level 2
- WebAPI/Device/Battery Status API
- WebAPI/Device/Device Orientation Event Specification
- WebAPI/Device/HTML5 Browser state
- WebAPI/Device/The Network Information API
- WebAPI/Device/The Screen Orientation API
- WebAPI/Device/Touch Events version 1
- WebAPI/Device/Vibration API
- WebAPI/DOM, Forms and Styles/CSS 2D Transforms
- WebAPI/DOM, Forms and Styles/CSS 3D Transforms Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Animations Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Backgrounds and Borders Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Basic User Interface Module Level 3 (CSS3 UI)
- WebAPI/DOM, Forms and Styles/CSS Color Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Flexible Box Layout Module
- WebAPI/DOM, Forms and Styles/CSS Fonts Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Multi-column Layout Module
- WebAPI/DOM, Forms and Styles/CSS Style Attribute
- WebAPI/DOM, Forms and Styles/CSS Text Module Level 3
- WebAPI/DOM, Forms and Styles/CSS Transforms Module Level 1
- WebAPI/DOM, Forms and Styles/CSS Transitions Module Level 3
- WebAPI/DOM, Forms and Styles/DOM/JavaScript related HTML5 Enhancements
- WebAPI/DOM, Forms and Styles/HTML5 Forms
- WebAPI/DOM, Forms and Styles/Media Queries
- WebAPI/DOM, Forms and Styles/Selectors API Level 1
- WebAPI/DOM, Forms and Styles/Selectors API Level 2
- WebAPI/EXTERNAL/App Security API
- WebAPI/Graphics/HTML5 SVG
- WebAPI/Graphics/HTML5 The canvas element
- WebAPI/JavaScript/Promises
- WebAPI/Location/Geolocation API Specification
- WebAPI/Media/getUserMedia
- WebAPI/Media/HTML5 The audio element
- WebAPI/Media/HTML5 The video element
- WebAPI/Media/HTML Media Capture
- WebAPI/Media/Web Audio API
- WebAPI/Networking/WebRTC
- WebAPI/Performance and Optimization/High Resolution Time
- WebAPI/Performance and Optimization/Navigation Timing
- WebAPI/Performance and Optimization/Page Visibility
- WebAPI/Performance and Optimization/Resource Timing
- WebAPI/Performance and Optimization/Timing control for script-based animations
- WebAPI/Performance and Optimization/User Timing
- WebAPI/Performance and Optimization/Web Workers
- WebAPI/Responsive Design/CSS Device Adaptation
- WebAPI/Runtime(short-term)/App URI
- WebAPI/Runtime(short-term)/Runtime
- WebAPI/Screen Presentation APIs/WebScreen
- WebAPI/Security/Content Security Policy
- WebAPI/Security/Cross-Origin Resource Sharing
- WebAPI/Security/HTML5 The iframe element
- WebAPI/Storage/File API
- WebAPI/Storage/File API: Directories and System
- WebAPI/Storage/File API: Writer
- WebAPI/Storage/HTML5 Application caches
- WebAPI/Storage/Indexed Database API
- WebAPI/Storage/Web SQL Database
- WebAPI/Storage/Web Storage
- WebAPI/Supplementary API Reference/Fullscreen APIMozilla
- WebAPI/Supplementary API Reference/SIMD
- WebAPI/Supplementary API Reference/Typed Arrays - Khronos
- WebAPI/Supplementary API Reference/WebGL - Khronos
- WebAPI/System-level APIs/Contacts Manager
- WebAPI/System-level APIs/Device Capabilities
- WebAPI/System-level APIs/Messaging
- WebAPI/System-level APIs/Raw Sockets
- WebAPI/UI/HTML5 Drag and drop
- WebAPI/UI/HTML5 telephone, email and URL state of input element
- WebAPI/UI/Web Notifications
- WebAPI/UI/Web Speech
- WebAPI/W3C\_EXTRAHTML5/Attributes
- WebAPI/W3C\_EXTRAHTML5/Base64
- WebAPI/W3C\_EXTRAHTML5/Browsers
- WebAPI/W3C\_EXTRAHTML5/Dom
- WebAPI/W3C\_EXTRAHTML5/ForeignContent
- WebAPI/W3C\_EXTRAHTML5/Rendering
- WebAPI/W3C\_EXTRAHTML5/Semantics
- WebAPI/W3C\_EXTRAHTML5/Xhtml5
- WebAPI/Web Components/HTML Imports
- WebAPI/Web Components/HTML Templates
- WebAPI/Web Components/Shadow DOM
