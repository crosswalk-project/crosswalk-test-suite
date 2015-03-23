define(function (require, exports, module) {
  var Plugin = require("pkg!pluginBase");


  var View = Plugin.View.extend({
    id: "bookMask",
    initialize: function (config) {
      this.$el.appendTo($("#book-stage"));

    },
    obEvents: {
      "book:disable.action": "show",
      "book:enable.action": "hide",
      "book:zoom.in": "addZoom",
      "book:zoom.out": "removeZoom"
    },
    removeZoom: function () {
      this.$el.removeClass("zoom");
    },
    addZoom: function () {
      this.$el.addClass("zoom");
    },
    show: function () {
      this.$el.addClass("active");
    },
    hide: function () {
      this.$el.removeClass("active");
    }
  });
  return View;
});
