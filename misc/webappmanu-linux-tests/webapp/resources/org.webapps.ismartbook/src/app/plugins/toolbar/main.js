define(function (require, exports, module) {

  var PluginBase = require("pkg!pluginBase");
  var template = require("tpl!./toolbar");
  var systemMode = require("pkg!systemMode");



  var View = PluginBase.View.extend({
    id: "toolbar",
    mode: "toolbar",
    template: template,
    initialize: function () {
      this.render();
    },
    events: {
      "click .bookmark,.annotation,.dict,.search": "callTool",
      "click .close": "close"
    },
    obEvents: {
      "system:change.mode": "modeChange",
      "gesture:swipe":"swipe"
    },
    callTool: function (evt) {
      var data = evt.currentTarget.dataset.value;
      //调出annotation tool
      if(data == "annotation"){
        systemMode.enter("toolAnnotation");
      }
      //end
      this.emit("system:call.tool", data);
    },
    close: function () {
      if (!window.close) return;

      if (window.parent) {
        window.parent.opener = null;
        window.parent.close();
        return;
      }

      window.close();

    },
    swipe:function(dir,evt){      
      
    },
    modeChange: function (oldMode, newMode) {
      
      if (newMode != this.mode && oldMode != this.mode) return;

      if (newMode === this.mode) return this.show();

      if (oldMode === this.mode) return this.hide();
    },
    show: function () {

      this.$el.addClass("active");
      this.emit("book:disable.action");
    },
    hide: function () {
      this.$el.removeClass("active");
      this.emit("book:enable.action");
    },
    render: function () {
      this.$el.html(this.template()).appendTo($("body"));
    }

  });
  return View;
});
