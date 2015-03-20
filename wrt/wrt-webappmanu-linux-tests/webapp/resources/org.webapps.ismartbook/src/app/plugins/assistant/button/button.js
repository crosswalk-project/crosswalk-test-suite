define(function (require, exports, module) {
  var Base = require("pkg!pluginBase");

  var Tpl = require("tpl!./button");


  var View = Base.View.extend({
    id: "assistant-button",
    initialize: function (model) {
      this.model = model;
      this.$el.appendTo($("#reader-stage"));
      this.render();
    },

    events:{
      "click":"hide"
    },
    zoomin:function(){
      this.$el.addClass("zoomin");
    },
    zoomout:function(){
      this.$el.removeClass("zoomin");
    },
    show: function () {
      this.$el.removeClass("active");
    },
    hide: function () {
      this.trigger("hide");
      this.$el.addClass("active");
    },
    render: function () {
      this.$el.html(Tpl({}));
    }
  });
  return View;
});
