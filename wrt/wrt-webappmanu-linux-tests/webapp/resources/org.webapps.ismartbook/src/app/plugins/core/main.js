define(function (require, exports, module) {
  "use strict";
  // 获取相关依赖

  //plugin relative
  var Plugins = require("pkg!plugin");
  var PluginBase = require("pkg!pluginBase");

  // system relative
  var ReaderModel = require("./readerModel");

  var systemMode = require("pkg!systemMode");

  //jquery 
  require("hammer.event");

  // Fix some aciton for book
  require("./action.fix");
  var test = 0;
  /**
   * Reader 类
   */
  var Reader = PluginBase.View.extend({
    el: "#reader-stage",
    initialize: function () {
      var config, plugins;

      this.model = new ReaderModel({});

      // 初始化主题
      //this.initTheme();

      config = this.model.get("config");

      // init plugins
      plugins = _.union(config.get("system_plugin"), config.get("plugins"));

      // initilize systemMode to reader;
      systemMode.enter("reader");
      this.Plugins = new Plugins(plugins);
      test++;
    },
    obEvents: {
      "book:end.init": "hideStartup"
    },
    events: {
      "swipe": "swipeEvent"
    },
    swipeEvent: function (evt) {
      if (evt.target.id !== this.el.id) return;
      console.timeEnd("gesture:swipe");
      this.emit("gesture:swipe", evt.originalEvent.gesture.direction, evt);
      var dir  = evt.originalEvent.gesture.direction;

      if (dir === "up" && !systemMode.is("toolbar")){
       
         systemMode.enter("toc","reader");
         evt.preventDefault();
         return false;
       }

      if(dir === "down" && systemMode.is("toc")){
        
        systemMode.exit("toc");
        evt.preventDefault();
        return false;
      }

       if (dir === "up" && systemMode.is("toolbar")){         
        systemMode.exit("toolbar");
        evt.preventDefault();
        return false;
       }

      if(dir === "down" && !systemMode.is("toc")){
        systemMode.enter("toolbar","reader");
        evt.preventDefault();
        return false;
         
      }

    },

    hideStartup: function () {
      var $leftpages = $('#book .left-page');
      
      var config = this.model.get('config');
      if ($leftpages.length < config.get('start')) {
        config.set('start',1);
      }
   
      $("#startup .left-page").html($leftpages.eq(config.get('start')-1).html());

      var initEnd = function () {
        $("body").addClass("init-end");
        setTimeout(openCover, 1000);
      }.bind(this);

      var openCover = function () {

        $("body").removeClass("init-end init");
        setTimeout(function () {
          $("#startup").remove();
        }, 20);
        this.emitAsync("book:resize.mask", 1);

      }.bind(this);

      setZeroTimeout(initEnd);
    }
    //,
    // initTheme: function () {
    //   var config = this.model.get("config");
    //   // 加载 Reader 的样式文件 
    //   var theme = config.get("theme");
    //   $("<link/>").attr("rel", "stylesheet").attr("href", "app/themes/" + theme + "/css/main.css").appendTo($("head"));
    // }
  });



  return Reader;
});
