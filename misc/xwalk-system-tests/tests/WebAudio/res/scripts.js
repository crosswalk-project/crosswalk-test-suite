function getParameterByName(name) {
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
  var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
  var results = regex.exec(location.search);
  return results ? decodeURIComponent(results[1].replace(/\+/g, " ")) : null;
}

function goBackAutomatically() {
  setTimeout(function() {
    history.back();
  }, 1000);
}
