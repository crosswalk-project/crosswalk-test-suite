self.onmessage = function(evt) {
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      var isClient = client instanceof Client;
      var message = {isClient: isClient, url: client.url};
      client.postMessage(message);
    });
  });
};
