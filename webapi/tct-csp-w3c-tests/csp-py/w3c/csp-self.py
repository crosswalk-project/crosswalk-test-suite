def main(request, response):
    import simplejson as json
    f = file('config.json')
    source = f.read()
    s = json.JSONDecoder().decode(source)
    url1 = "http://" + s['host'] + ":" + str(s['ports']['http'][1])
    url2 = "http://" + s['host'] + ":" + str(s['ports']['http'][0])
    _CSP = "default-src 'self'  about: 'unsafe-inline'"
    response.headers.set("Content-Security-Policy", _CSP)
    response.headers.set("X-Content-Security-Policy", _CSP)
    response.headers.set("X-WebKit-CSP", _CSP)
    return """<!DOCTYPE html>
<html>
  <head>
    <title>XMLHttpRequest: abort() after send()</title>
    <script src="../../resources/testharness.js"></script>
    <script src="../../resources/testharnessreport.js"></script>
  </head>
  <body>
    <div id="log"></div>
    <script>
      var test = async_test()
      test.step(function() {
        var client = new XMLHttpRequest(),
            control_flag = false,
            result = [],
            expected = [1, 4] // open() -> 1, send() -> 1, abort() -> 4
        client.onreadystatechange = function() {
          test.step(function() {
            result.push(client.readyState)
            if(client.readyState == 4) {
              control_flag = true
              assert_equals(client.responseXML, null)
              assert_equals(client.responseText, "")
              assert_equals(client.status, 0)
              assert_equals(client.statusText, "")
              assert_equals(client.getAllResponseHeaders(), "")
            }
          })
        }
        client.open("GET", "../resources/delay.py?ms=2000", true)
        client.send(null)
        client.abort()
        assert_true(control_flag)
        assert_equals(client.readyState, 0)
        assert_array_equals(result, expected)
        test.done()
      })
    </script>
  </body>
</html> """
