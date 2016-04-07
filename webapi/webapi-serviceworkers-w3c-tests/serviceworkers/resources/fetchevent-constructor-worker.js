importScripts("../../resources/testharness.js");
importScripts("../w3c/cache-storage/resources/test-helpers.js");

var url = new URL("blank-iframe.html", location).toString();

test(function() {
  var req = new Request(url);
  var event = new FetchEvent("FetchEvent", {request: req});
  assert_equals(event.type, "FetchEvent", "FetchEvent type");
  assert_false(event.isReload);
  assert_equals(event.request.url, url, "the initial request url");
  assert_equals(event.clientId, null, "the initial clientId");
}, "FetchEvent constructor with type.");

test(function() {
  var req = new Request(url);
  var event = new FetchEvent("FetchEvent", {request: req, isReload: true, clientId: "client-id-value"});
  assert_equals(event.type, "FetchEvent", "FetchEvent type");
  assert_true(event.isReload, "isReload is set to true");
  assert_equals(event.request.url, url, "request url");
  assert_equals(event.clientId, "client-id-value", "clientId value");
}, "FetchEvent constructor with initial FetchEventInit.");
