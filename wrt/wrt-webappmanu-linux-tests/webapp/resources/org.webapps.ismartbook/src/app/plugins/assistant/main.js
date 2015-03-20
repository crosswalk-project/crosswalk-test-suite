define(function (require, exports, module) {
  var Base = require("pkg!pluginBase");
  var AssistantModel = require("./model");
  var AsideView = require("./aside/aside");
  var Overview = require("./overview/overview");

  var View = Base.View.extend({
    initialize: function () {
      this.model = new AssistantModel({});
      this.$aside = new AsideView(this.model);
      this.$overview = new Overview(this.model);
      this.emit("system:register.end", "preload", "assistant:end.preload");
    }
  });
  return View;
});
