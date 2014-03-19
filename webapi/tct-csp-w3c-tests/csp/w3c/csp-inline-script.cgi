#!/bin/sh
echo "Content-Security-Policy: default-src 'self'"
echo "X-Content-Security-Policy: default-src 'self'"
echo "X-WebKit-CSP: default-src 'self'"
echo
echo '<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
	<meta description="Content-Security-Policy Test: default-src: *" />
	<link rel="author" title="tanvi@mozilla.com" />
	<title> No inline script </title>
	<script src="../../resources/testharness.js"></script>
	<script src="../../resources/testharnessreport.js"></script>
</head>

<body>
	<div id=log></div>
	<script src="CSP_passTest001.cgi"></script>
        <script>
		test(function() {assert_true(true)}, "assert_true with false from unsafe inline script");
	</script>
</body>
<html> '
