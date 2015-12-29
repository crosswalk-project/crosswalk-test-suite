self.onmessage = function(evt) {
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      client.postMessage(self.clients instanceof Clients);
    });
  });
};
