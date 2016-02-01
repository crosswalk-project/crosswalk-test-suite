# App-tools Test Suite Developer Guide

## Overview

This document is intended for those who want to make test contributions to App-tools test suite.

Please formiliarize yourself with the following knowledge:

- Basic knowledge in [web test suite developer guide](./Web_Test_Suite_Developer_Guide.md)
- [PyUnit](http://pyunit.sourceforge.net/pyunit.html), the standard unit testing framework for Python. It is called by testkit-lite to support the test execution.
- [Crosswalk-app-tools](https://github.com/crosswalk-project/crosswalk-app-tools) is forthcoming packaging tool for creating Crosswalk applications. It is used to build web applications, and provide feedback for future improvements.

## Test Case File Template

Auto tests are all designed with python language, the file template looks likes this:
```xml
class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def subcase1(self):

    def subcase2(self):

    def subcase3(self):

if __name__ == '__main__':
    unittest.main()
```

- "def" represents one subcase, and it requires a blank line between each subcases
- Similar test points can be put in one test case file
- One test case file may includes one or multiple subcases

## Subcase Naming Convention

**Template**

test\_shortDescriptionForTestPurpose

- The first letter of each word is lowercase, and connect with "_"

**Examples**

test_activity_name_normal

test_update_app_version

## How to Add a New Test Suite for App-tools?

The best method to add a new test suite is to copy a simliar existing test suite and then update related test scripts.

1. Fork and clone the App-tools project from </br>
   https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/apptools
1. Copy a simliar existing test suite, e.g. `apptools-ios-tests` to the place you want to make a new test suite, and rename it.
1. Update `manifest.json` and `suite.json`.
1. Rename `<test-case-sub-directory>`.
1. Create new test cases (see next section) and update `tests*.xml` files.
1. Update README to introduce the test suite, and precondition for App-tools on test host.
1. Package the test suite and run the test cases.
1. Submit your changes in a pull request.

## How to Contribute New Cases for App-tools?

1. Design new test case according to the specification and/or feature requirement, and add new case information to `tests.full.xml`. The `tests.xml` can be converted from `tests.full.xml` by [xmlsimplifier](https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/tools/xmlsimplifier).
1. Develop test script following the [test case naming convention](./Web_Test_Suite_Developer_Guide.md#Test-case-naming-convention) and [test case coding style](./Web_Test_Suite_Developer_Guide.md#test-case-coding-style), and put it under `<test-case-sub-directory>`.

Note:

- Each test should have an entry HTML file/Python script.
- The test script can be embedded into the HTML/Python file or be used as separated JavaScript/Python file.
- Set `<set type='pyunit'>` in `tests*.xml` for PyUnit test.
