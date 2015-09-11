# Test Auto Generator

## Introduction

This is a tool to automatically generate test cases for checking existence of
Typed Array attributes existence.

## Source Code

* `data.yaml`: test cases data.
* `gentest.py`: script to create test cases using template and data.
* `template.html`: test case template.
* `template-dataview.html`: alternative test case template for DataView
interface.

## How to Generate Tests

```sh
python gentest.py
```

## Authors

* Xie, Yunxiao <yunxiaox.xie@intel.com>
* Wang, Chunyan <chunyanx.wang@intel.com>

## LICENSE

Copyright (c) 2014 Intel Corporation.
Except as noted, this software is licensed under BSD-3-Clause License.
Please see the COPYING file for the BSD-3-Clause License.
