define(function (require, exports, module) {
  var Plugin = require("pkg!pluginBase");
  var config = Plugin.config;

  var Model = Plugin.Model.extend({
    defaults: {
      width: 0,
      height: 0,
      left: 0,
      right: 0,
      activePage: 0
    },
    init: function () {
      var toc = config.get("ebook").get("ncx");
      var length = _.size(toc.points);
      this.set("length", length);
      this.set("fullPath", config.get("ebook").get("fullPath") + "/" + config.get("ebook").get("opfRoot"));
      this.set("toc", toc);
    }
  });
  return Model;
});
