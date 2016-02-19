# SIMD.js Test Suite

## Introduction

This test suite is for checking compliance with SIMD.js specification:
* https://tc39.github.io/ecmascript_simd/

As of Crosswalk 17, SIMD (Single Instruction Multiple Data) implementation was
witched to upstream Chromium M46; see
* https://crosswalk-project.org/jira/browse/XWALK-4222

## Test development

It is better to submit new test cases and/or bug fixing patches to upstream
ecmascript_simd at https://github.com/tc39/ecmascript_simd, and then integrate
them back to this test suite. If the submission is rejected by upstream, it is
not suitable to this test suite either.

In practically, however, submissions to upstream take more time to be reviewed.
It is acceptable to create tests here and then submit them to upstream. When
upstream handles the submissions, we can then update this test suite accordingly.

The test cases in this test suite are based on [QUnit](http://qunitjs.com)
testing framework. You can add test file to [simd](./simd/) sub-directory like
this.

```
<!DOCTYPE html>
<meta charset='utf-8'>
<title>SIMD Test: float32x4</title>
<link rel="author" title="Intel" href="http://www.intel.com">
<link rel="help" href="https://tc39.github.io/ecmascript_simd/">
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
```

Then add the test cases to `tests.full.xml` and re-generate `tests.xml` file.
See the [Tests XML Definition and
Sample](../../doc/Tests_XML_Definition_and_Sample.md#qunit-type) document for
details.

## Authors

* Xu, Kang <kangx.xu@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2016 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
