self.onmessage = function(evt) {
  var port = evt.data.port;
  var clientIds = [];
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      clientIds.push(client.id);
    });
    port.postMessage(clientIds);
  });
}
