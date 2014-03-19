#!/bin/sh
echo "Content-Security-Policy:default-src http://127.0.0.1:8081 https://www.tizen.org 'unsafe-inline'"
echo "X-Content-Security-Policy:default-src http://127.0.0.1:8081 https://www.tizen.org 'unsafe-inline'"
echo "X-WebKit-CSP:default-src http://127.0.0.1:8081 https://www.tizen.org 'unsafe-inline'"
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
    <title>CSP Test: csp_default-src_cross-origin_multi_script</title>
    <link rel="author" title="Intel" href="http://www.intel.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#default-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="default-src http://127.0.0.1:8081 https://www.tizen.org 'unsafe-inline'"/>
    <meta charset="utf-8"/>
    <script src="http://127.0.0.1:8081/opt/tct-csp-w3c-tests/resources/testharness.js"></script>
    <script src="http://127.0.0.1:8081/opt/tct-csp-w3c-tests/resources/testharnessreport.js"></script>
  </head>
  <body>
    <div id="log"></div>
    <script src="http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/test81.js"></script>
    <script src="http://127.0.0.1:8083/opt/tct-csp-w3c-tests/csp/support/test83.js"></script>
    <script src="support/csp.js"></script>
    <script>
        test(function() {
            assert_true(typeof X != "number", "attribute defined internal");
        }, document.title + "_blocked");

        test(function() {
            assert_true(typeof getVideoURI == "function", "Function getVideoURI is defined");
        }, document.title + "_allowed_one");

        test(function() {
            assert_true(typeof q == "object", "Function getVideoURI is defined");
        }, document.title + "_allowed_two");
    </script>
  </body>
</html> '
