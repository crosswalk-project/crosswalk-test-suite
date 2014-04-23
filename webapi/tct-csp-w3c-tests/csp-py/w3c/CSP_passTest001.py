def main(request, response):
    response.headers.set("Content-Type", "text/javascript")
    return """
(function ()
{
	test(function() {assert_true(true)}, "assert_true with true");
})(); """
