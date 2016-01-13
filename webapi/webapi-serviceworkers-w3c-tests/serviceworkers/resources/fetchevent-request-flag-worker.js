var request = null;

self.onfetch = function(evt) {
  request = evt.request;
}

self.onmessage = function(evt) {
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      client.postMessage({
        mode: request.mode,
        credentials: request.credentials,
        redirect: request.redirect
      });
    });
  });
}
