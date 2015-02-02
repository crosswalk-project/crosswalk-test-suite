$(document).ready(function() {
  document.addEventListener('deviceready', function() {
    if(!window.sessionStorage) {
      alert('Error! Your platform does not support sessionStorage.');
    }
    var sstorage = window.sessionStorage;
    if(sstorage.getItem("RBCount") == null) {
      sstorage.setItem("RBCount", 0);
    } 
    if(parseInt(sstorage.getItem("RBCount")) > 512) {
      $('#count').html("successfully! Counting is over!");
      sstorage.removeItem("RBCount");
      var urlArr = window.location.href.split('/');
      var pagename = urlArr[urlArr.length - 1];
      var urlatt = window.location.href.substring(0, window.location.href.indexOf(pagename)) + "index.html?tid=BridgeReload";
      window.location.href = urlatt;
    } else {
      $('#count').html(sstorage.getItem("RBCount"));
      sstorage.setItem("RBCount", parseInt(sstorage.getItem("RBCount")) + 1);
      var urlArr = window.location.href.split('/');
      var pagename = urlArr[urlArr.length - 1];
      if(pagename == "page1.html") {
        window.location = 'page2.html';
      } else {
        window.location = 'page1.html';
      }
    }
  });
});
