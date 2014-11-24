#!/bin/sh
echo "Content-Security-Policy-Report-Only: media-src 'none'; script-src 'self' 'unsafe-inline'"
echo "X-Content-Security-Policy-Report-Only: media-src 'none'; script-src 'self' 'unsafe-inline'"
echo "X-WebKit-CSP-Report-Only: media-src 'none'; script-src 'self' 'unsafe-inline'"
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
    <title>CSP Test: csp_ro_media-src_none_video_blocked_ext</title>
    <link rel="author" title="Samsung" href="http://www.Samsung.com"/>
    <link rel="help" href="http://www.w3.org/TR/2012/CR-CSP-20121115/#media-src"/>
    <meta name="flags" content=""/>
    <meta name="assert" content="media-src *; script-src 'self' 'unsafe-inline'"/>
    <meta charset="utf-8"/>
    <script src="../resources/testharness.js"></script>
    <script src="../resources/testharnessreport.js"></script>
  </head>
  <body>
    <div id="log"></div>
    <video id="m"></video>
    <script>
        var t = async_test(document.title);
        var m = document.getElementById("m");
        m.src = "http://127.0.0.1:8083/opt/tct-csp-w3c-tests/csp/support/red-green.theora.ogv";
        window.setTimeout(function() {
            t.step(function() {
                assert_false(m.currentSrc == "",
                    "video.currentSrc should not be empty even use the not allowed external audio resource in report only mode");
            });
            t.done();
        }, 0);
    </script>
  </body>
</html> '
