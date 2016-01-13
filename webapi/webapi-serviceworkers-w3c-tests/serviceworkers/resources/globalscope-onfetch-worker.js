onfetch = function(evt) {
  var response = null;
  if(evt.request.url.indexOf("?string") > 0) {
    response = new Response("Test string");
  } else if(evt.request.url.indexOf("?blob") > 0) {
    response = new Response(new Blob(["Test blob"]));
  } else {
    response = new Response();
  }
  evt.respondWith(response);
};
