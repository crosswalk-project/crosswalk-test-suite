var presentationWindow = null;

function closePresentationWindow() {
  if (presentationWindow !== null)
    presentationWindow.close();
  reset();
}

function reset() {
  var msg = document.getElementById("message");
  msg.innerHTML = "Received message: N/A";
  var result = document.getElementById("result");
  result.innerHTML = "Result: N/A";
}

function showSucceed(w) {
  var e = document.getElementById("result");
  e.innerHTML = "Result: OK";

  presentationWindow = w;
  presentationWindow.postMessage("I am from opener window", "*");
}

function showError(e) {
  var elem = document.getElementById("result");
  elem.innerHTML = "Result: " + e.name;
}

function requestShow() {
  navigator.presentation.requestShow("display/contents.html", showSucceed, showError);
}

function init() {
  var e = document.getElementById("available");
  e.innerHTML = navigator.presentation.displayAvailable ?
                "Display Availability: true" : "Display Availability: false";

  navigator.presentation.addEventListener("displayavailablechange", function() {
    e.innerHTML = navigator.presentation.displayAvailable ?
                  "Display Availability: true" : "Display Availability: false";
    if (!navigator.presentation.displayAvailable) {
      var button = document.getElementById("available");
      button.disabled = true;
    }
  });
}

window.onmessage = function(evt) {
  var e = document.getElementById("message");
  e.innerHTML = "Received message: " + evt.data;
}
