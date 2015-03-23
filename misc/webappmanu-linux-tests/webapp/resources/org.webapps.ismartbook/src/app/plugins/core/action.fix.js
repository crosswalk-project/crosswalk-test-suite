define(function (require, exports, module) {
  // 如果在iframe里面，当翻页或者操控的时候，鼠标拖出iframe之后，系统不会触发mouseleave事件
  // 这个就是为了做一层兼容用的
  window.leaveDetect = function () {
    $(document).trigger("mouseleave");
  };
  return true;
});
