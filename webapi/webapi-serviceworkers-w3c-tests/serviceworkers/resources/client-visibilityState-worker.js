self.onmessage = function(evt) {
  var port = evt.data.port;
  var visibilityStates = [];
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      visibilityStates.push(client.visibilityState);
    });
    port.postMessage(visibilityStates);
  });
}
