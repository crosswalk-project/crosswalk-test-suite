importScripts("../../resources/testharness.js");
importScripts("../w3c/cache-storage/resources/test-helpers.js");

self.onmessage = function(evt) {
  var port = evt.data.port;
  self.clients.matchAll()
    .then(function(clients) {
      var client = clients[0];
      client.navigate("about:blank");
    }).catch(function(ex) {
      port.postMessage(ex.name);
    });
}
