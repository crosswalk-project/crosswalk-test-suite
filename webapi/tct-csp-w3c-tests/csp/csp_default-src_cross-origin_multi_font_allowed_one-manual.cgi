#!/bin/sh
echo "Content-Security-Policy: default-src http://127.0.0.1:8081 http://127.0.0.1:8082; style-src 'unsafe-inline'"
echo "X-Content-Security-Policy: default-src http://127.0.0.1:8081 http://127.0.0.1:8082; style-src 'unsafe-inline'"
echo "X-WebKit-CSP: default-src http://127.0.0.1:8081 http://127.0.0.1:8082; style-src 'unsafe-inline'"
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
    <title>CSP Test: csp_default-src_cross-origin_multi_font_allowed_one</title>
    <link rel="author" title="Intel" href="http://www.intel.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#default-src"/>
    <link rel="match" href="reference/csp_default-src_none_font_blocked_int-ref.html"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="default-src http://127.0.0.1:8081 http://127.0.0.1:8082; style-src 'unsafe-inline'"/>
    <meta charset="utf-8"/>
    <style>
        @font-face {
            font-family: Canvas;
            src: url("http://127.0.0.1:8081/opt/tct-csp-w3c-tests/csp/support/w3c/CanvasTest.ttf");
        }
        #test {
            font-family: Canvas;
        }
    </style>
  </head>
  <body>
    <p>Test passes if the two lines are different in font</p>
    <div id="test">1234 ABCD</div>
    <div>1234 ABCD</div>
 </body>
</html> '
