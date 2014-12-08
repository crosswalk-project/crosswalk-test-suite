function getScrollTop() {
  return f_scrollTop();
}

function f_scrollTop() {
  return f_filterResults (
    $(window) ? $(window).scrollTop() : 0,
    document.documentElement ? document.documentElement.scrollTop : 0,
    document.body ? document.body.scrollTop : 0
  );
}

function f_filterResults(n_win, n_docel, n_body) {
  var n_result = n_win ? n_win : 0;
  if (n_docel && (!n_result || (n_result > n_docel)))
    n_result = n_docel;
  return n_body && (!n_result || (n_result > n_body)) ? n_body : n_result;
}

function setScrollTop() {
  $(window) ? $(window).scrollTop(0): 0;
  document.documentElement ? document.documentElement.scrollTop = 0 :0;
  document.body ? document.body.scrollTop = 0 : 0;
}

function goTopEx() {
  $node = $('#goTopBtn');

  if (getScrollTop() > 0) {
    $node.show();
  } else {
    $node.hide();
  }

  $(window).scroll(function () {
    if (getScrollTop() > 0) {
      $node.show();
    } else {
      $node.hide();
    }
  });

  $node.click(function () {
    setScrollTop();
  });
}

