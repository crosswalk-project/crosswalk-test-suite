self.onactivate = function(evt) {
  var result;
  self.clients.claim()
    .then(function(result) {
      result = result;
      return self.clients.matchAll();
    })
    .then(function(clients) {
      clients.forEach(function(client) {
        client.postMessage(result == undefined);
      });
    });
}
