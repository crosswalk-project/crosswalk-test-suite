self.onfetch = function(evt) {
  var response = new Response("response");
  evt.respondWith(response);
};

