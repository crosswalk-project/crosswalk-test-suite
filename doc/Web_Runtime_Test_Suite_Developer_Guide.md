# Web Runtime Test Suite Developer Guide

## Overview

This document is intended for those who want to make test contributions to Web Runtime test suite.

Please formiliarize yourself with the following knowledge:

- Basic knowledge in [web test suite developer guide](./Web_Test_Suite_Developer_Guide.md)
- [PyUnit](http://pyunit.sourceforge.net/pyunit.html), the standard unit testing framework for Python. It is called by testkit-lite to support the test execution.


## How to add new test suite for Web Runtime?
The best method to add a new test suite is to copy a simliar existing test suite and then update related test scripts.

1. Fork and clone the wrt project from

   https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/wrt

2. Copy a simliar existing test suite, e.g. `wrt-upgrademanu-android-tests`, and rename it following `wrt-<suitename>-<platform>-tests`.

3. Update `manifest.json`.

4. Rename `<test-case-sub-directory>`.

5. Create new test cases (see next section) and update `tests*.xml` files.

6. Package the test suite and run the test cases.

7. Submit your changes in a pull request.


## How to contribute new cases for Web Runtime?

1. Design new test case according to the specification and/or feature requirement, and add new case information to `tests.full.xml`.
   The `tests.xml` can be converted from `tests.full.xml` by [xmlsimplifier](https://github.com/crosswalk-project/crosswalk-test-suite/tree/master/tools/xmlsimplifier).

2. Develop test script following the requirement [test case naming convention](./Web_Test_Suite_Developer_Guide.md#Test case naming convention)
   and [test case coding style](./Web_Test_Suite_Developer_Guide.md#test-case-coding-style), and put it under `<test-case-sub-directory>`.

Note:

- Each test should have an entry HTML file/Python script.
- The test script can be embedded into the HTML/Python file or be used as separated JavaScript/Python file.
- Set `<set type='pyunit'>` in `tests*.xml` for PyUnit test.


## How to contribute pairwise cases for Web Runtime?

- Install  AllPairs

1. Download AllPairs from here:

   http://sourceforge.net/projects/allpairs/

2. Copy metacomm folder to your suite:
   metacomm/

3. import metacomm in your python file:

  import metacomm.combinatorics.all_pairs2

4. all_pairs sample:

       ```
        list=[[1,2],[3]]
        input_pair = all_pairs( list )
        for e, v in enumerate(input_pair):
            print e,v

        ....0 [1, 3]
        ....1 [2, 3]
       ```

