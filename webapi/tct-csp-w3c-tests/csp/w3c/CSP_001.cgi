#!/bin/sh
echo "Content-Security-Policy: default-src *"
echo "X-Content-Security-Policy: default-src *"
echo "X-WebKit-CSP: default-src *"
echo
echo '<!DOCTYPE html>
<html>
	<head>
		<title>CSP Test: default-src: *</title>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
		<meta descriptionn="Content-Security-Policy Test: default-src: *" />
		<link rel="author" title="bhill@paypal-inc.com" />
		<script src="../../resources/testharness.js"></script>
		<script src="../../resources/testharnessreport.js"></script>
		<script src="CSP_passTest001.cgi"></script>
	</head>
	<body>
		<div id=log></div>
	</body>

	<script>
		test(function() {assert_true(false)}, "assert_true with false from unsafe inline script");
	</script>
</html> '
