def main(request, response):
    import simplejson as json
    f = file('config.json')
    source = f.read()
    s = json.JSONDecoder().decode(source)
    url1 = "http://" + s['host'] + ":" + str(s['ports']['http'][1])
    url2 = "http://" + s['host'] + ":" + str(s['ports']['http'][0])
    _CSP = "default-src 'self'"
    response.headers.set("Content-Security-Policy", _CSP)
    response.headers.set("X-Content-Security-Policy", _CSP)
    response.headers.set("X-WebKit-CSP", _CSP)
    return """<!DOCTYPE html>
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
	<script src="CSP_passTest001.py"></script>
        <script>
		test(function() {assert_true(true)}, "assert_true with false from unsafe inline script");
	</script>
</body>
<html> """
