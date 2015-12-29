importScripts("../../resources/testharness.js");
importScripts("../w3c/cache-storage/resources/test-helpers.js");

test(function() {
  var event = new FetchEvent("FetchEvent");
  assert_equals(event.type, "FetchEvent", "FetchEvent type");
  assert_false(event.isReload);
  assert_equals(event.request, null, "the initial request value");
}, "FetchEvent constructor with type.");

test(function() {
  var url = new URL("blank-iframe.html", location).toString();
  var req = new Request(url);
  var event = new FetchEvent("FetchEvent", {request: req, isReload: true});
  assert_equals(event.type, "FetchEvent", "FetchEvent type");
  assert_true(event.isReload, "the initial value is set true");
  assert_equals(event.request.url, url, "the initial request value");
}, "FetchEvent constructor with initial FetchEventInit.");
