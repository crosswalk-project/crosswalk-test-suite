/**
 * Book Parser 
 * @author <weix.ge@intel.com>
 * @version 0.1.0
 * @description 解析书本。部分函数会从ETB的解析函数里面分离出来放到这个插件里面
 */

define(function (require, exports, module) {
  var EBook = require("etb");
  var PluginBase = require("pkg!pluginBase");


  var BookModel = PluginBase.Model.extend({
    obEvents: {
      // plugin:end.init is already async ,
      // so here call `parse` function directly
      "plugin:end.init": "parse"
    },

    parse: function () {

      var path = PluginBase.config.get("path");
      var endParse = this.endParse.bind(this);
      var opt = {
        complete: endParse,
        useCache:true
      };
      if (PluginBase.config.get("dev")) {
        opt.useCache = false;
      }
      this.set("ebook", new Ebook(path, opt));
    },

    endParse: function (ebook) {
      this.set("ebook",ebook);
      // 将局部变量里面的ebook　保存到config里面
      PluginBase.config.set("ebook", ebook);
      this.emitAsync("book:end.parse", ebook);
    
      // this.destroy();
    }
  });

  return BookModel;
});
