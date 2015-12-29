self.onmessage = function(e) {
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      client.postMessage("PASS");
      });
    });
};
