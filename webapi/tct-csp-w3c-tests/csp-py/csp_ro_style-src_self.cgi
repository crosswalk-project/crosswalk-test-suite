#!/bin/sh
echo "Content-Security-Policy-Report-Only:style-src 'self'"
echo "X-Content-Security-Policy-Report-Only:style-src 'self'"
echo "X-WebKit-CSP-Report-Only:style-src 'self'"
echo
echo '<!DOCTYPE html>

<!--
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:
        Ran, Wang <ran22.wang@samsung.com>
-->

<html>
  <head>
    <title>CSP Test: csp_ro_style-src_self</title>
    <link rel="author" title="Samsung" href="http://www.Samsung.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#style-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="style-src 'self'"/>
    <meta charset="utf-8"/>
    <script src="../resources/testharness.js"></script>
    <script src="../resources/testharnessreport.js"></script>
    <link rel="stylesheet" type="text/css" href="http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/canvas-index.css"/>
    <link rel="stylesheet" type="text/css" href="support/blue-100x100.css"/>
    <style>
      #test-green {
        background-color: green;
      }
    </style>
  </head>
  <body>
    <div id="log"></div>
    <div id="test-blue"></div>
    <div id="test-green"></div>
    <h3>ext-css:http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/canvas-index.css</h3>
    <script>
        test(function() {
            var div = document.querySelector("h3");
            var fix = getComputedStyle(div)["display"];
            assert_equals(fix, "inline", "style setted correctly");
        }, document.title + "_blocked");

        test(function() {
            var div = document.querySelector("#test-green");
            var fix = getComputedStyle(div)["backgroundColor"];
            assert_equals(fix, "rgb(0, 128, 0)", "style setted correctly");
        }, document.title + "_blocked_inline");
    </script>
  </body>
</html> '
