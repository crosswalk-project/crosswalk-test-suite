self.onmessage = function(evt) {
  self.clients.matchAll().then(function(clients) {
    var scope = self.registration.scope;
    var scriptURL = self.registration.active.scriptURL;
    var message = {scope: scope, scriptURL: scriptURL};
    clients.forEach(function(client) {
      client.postMessage(message);
    });
  });
};

