define(function (require, exports, module) {
  var Storage = require("pkg!storage");
  var Base = require("pkg!pluginBase");



  var Model = Base.Model.extend({
    defaults: function () {
      return {
        content: ""
      };
    },
    obEvents: {
      "book:end.parse": "preload",
      "book:turned": "loadContent"
    },
    getName: function (id) {
      return "assistant-" + id;
    },
    loadContent: function (page) {
      var id = this.page2id[page - 1];
      id = this.getName(id);
      Storage.local.get([id], function (obj) {
        if (!obj[id]) {
          obj[id] = "";
        }

        this.set("content", obj[id]);
      }.bind(this));
    },
    preload: function (ebook) {
      this.ebook = ebook;
      this.page2id = this.ebook.get("spine");
      var self = this;
      var assistants = this.ebook.get("ncx").assistants;
      var list = Object.keys(assistants);

      // 如果没有任何的助手内容，直接返回。
      if (!list.length) {
        return this.emitAsync("assistant:end.preload");
      }

      var len = list.length - 1;
      var fullPath = this.ebook.get("fullPath") + "/" + this.ebook.get("opfRoot") + "/";
      var check = function () {

        len--;
        if (len < 0) return self.emitAsync("assistant:end.preload");
        load(list[len], assistants[list[len]]);
      };

      var load = function (id, url) {

        $.get(fullPath + url, function (data) {
          if (!data) return check();
          id = "assistant-" + id;
          var obj = {};
          obj[id] = data;
          Storage.local.set(obj, check);
        });
      };

      load(list[len], assistants[list[len]]);

    }
  });

  return Model;
});
