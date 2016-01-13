self.onmessage = function(evt) {
  var port = evt.data.port;
  var message = [];
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      message.push(client.url);
    });
    port.postMessage(message);
  });
}
