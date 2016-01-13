self.onmessage = function(evt) {
  var port = evt.data.port;
  port.postMessage("ping");
}
