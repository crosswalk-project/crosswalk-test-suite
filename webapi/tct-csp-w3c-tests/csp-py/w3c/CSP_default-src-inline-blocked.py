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
<title>CSP Test: default-src 'self' about: 'unsafe-inline'</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta descriptionn="Content-Security-Policy Test: default-src 'self' about: 'unsafe-inline'" />
<link rel="author" title="abarth" />
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
</html> """
