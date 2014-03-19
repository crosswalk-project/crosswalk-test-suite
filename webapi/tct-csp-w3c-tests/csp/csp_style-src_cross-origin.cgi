#!/bin/sh
echo "Content-Security-Policy:style-src http://127.0.0.1:8081"
echo "X-Content-Security-Policy:style-src http://127.0.0.1:8081"
echo "X-WebKit-CSP:style-src http://127.0.0.1:8081"
echo
echo '<!DOCTYPE html>
<!--
Copyright (c) 2013 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Hao, Yunfei <yunfeix.hao@intel.com>

-->

<html>
  <head>
    <title>CSP Test: csp_style-src_cross-origin</title>
    <link rel="author" title="Intel" href="http://www.intel.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#style-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="style-src http://127.0.0.1:8081"/>
    <meta charset="utf-8"/>
    <script src="../resources/testharness.js"></script>
    <script src="../resources/testharnessreport.js"></script>
    <link rel="stylesheet" type="text/css" href="http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/w3c/canvas-index.css"/>
    <link rel="stylesheet" type="text/css" href="http://127.0.0.1:8082/opt/tct-csp-w3c-tests/csp/support/w3c/a-green.css"/>
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
    <h3>ext-css:http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/w3c/canvas-index.css</h3>
    <div id="test-ext-a" class="a"></div>
    <div id="test-green"></div>
    <script>
        test(function() {
            var div = document.querySelector("h3");
            var fix = getComputedStyle(div)["display"];
            assert_equals(fix, "inline", "style setted incorrectly");
        }, document.title + "_allowed");

        test(function() {
            var div = document.querySelector("#test-ext-a");
            var fix = getComputedStyle(div)["color"];
            assert_not_equals(fix, "rgb(0, 128, 0)", "style setted incorrectly");
        }, document.title + "_blocked");

        test(function() {
            var div = document.querySelector("#test-blue");
            var fix = getComputedStyle(div)["backgroundColor"];
            assert_not_equals(fix, "rgb(0, 0, 255)", "style setted incorrectly");
        }, document.title + "_blocked_int");

        test(function() {
            var div = document.querySelector("#test-green");
            var fix = getComputedStyle(div)["backgroundColor"];
            assert_not_equals(fix, "rgb(0, 128, 0)", "style setted incorrectly");
        }, document.title + "_blocked_inline");
    </script>
  </body>
</html> '
