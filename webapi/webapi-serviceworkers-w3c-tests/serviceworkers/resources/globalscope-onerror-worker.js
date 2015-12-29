var port;

self.onmessage = function(evt) {
  port = evt.data.port;
  throw new TypeError();
}

self.onerror = function(message, filename, lineno, colno) {
  port.postMessage({
    message: message,
    filename: filename,
    lineno: lineno,
    colno: colno
  });
}
