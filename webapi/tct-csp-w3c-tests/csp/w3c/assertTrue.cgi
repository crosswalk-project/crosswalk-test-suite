#!/bin/sh
echo
echo "//Prevent Caching"
echo "Expires: Mon, 26 Jul 1997 05:00:00 GMT"
echo "Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT"
echo "Cache-Control: no-store, no-cache, must-revalidate"
echo "Cache-Control: post-check=0, pre-check=0", false
echo "Pragma: no-cache"
echo "Content-Type: text/javascript"
echo
echo
echo 'print("(function () { test(function() {assert_true(" . $_GET["varName"] . ")}, \"assert_true with varName\"); })();");'
echo
echo

