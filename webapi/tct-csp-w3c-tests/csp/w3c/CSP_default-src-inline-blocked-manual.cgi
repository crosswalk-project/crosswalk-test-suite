#!/bin/sh
echo "Content-Security-Policy: default-src 'self'"
echo "X-Content-Security-Policy: default-src 'self'"
echo "X-WebKit-CSP: default-src 'self'"
echo
echo '<!DOCTYPE html>
<html>
<head>
<title>CSP Test: default-src 'self' about: 'unsafe-inline'</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta descriptionn="Content-Security-Policy Test: default-src 'self' about: 'unsafe-inline'" />
<link rel="author" title="abarth" />
<link rel="match" href="../reference/csp_default-src-inline-blocked-ref.html"/>
<script src="../../resources/testharness.js"></script>
<script src="../../resources/testharnessreport.js"></script>
</head>
<body>
<script src="resources/pass.js"></script>
<script>
test(function() {assert_true(false)}, "Inline scripts run (1 of 3)");
</script>
<iframe style="display:none" src="javascript:parent.test(function() {parent.assert_true(false)};"></iframe>
<img style="display:none"
     onerror="test(function() {assert_true(false)})"
     src="about:blank">
</body>
</html> '
