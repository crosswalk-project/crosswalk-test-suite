#!/bin/sh
echo "Content-type: text/javascript"
echo '
(function ()
{
	test(function() {assert_true(true)}, "assert_true with true");
})(); '
