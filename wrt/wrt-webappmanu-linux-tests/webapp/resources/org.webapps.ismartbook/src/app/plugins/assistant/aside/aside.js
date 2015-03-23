define(function (require, exports, module) {
  var Base = require("pkg!pluginBase");
  var Tpl = require("tpl!./aside");
  var ButtonView = require("../button/button");
  var iScroll = require("iscroll");

  var View = Base.View.extend({
    id: "assistant-aside",
    mode:"assistant",
    initialize: function (model) {
      this.$button = new ButtonView();
      this.model = model;
      
      this.$button.on("hide",this.show.bind(this));
      this.render();
      this.$content = this.$el.find(".content");
      this.$scroll = new iScroll(this.$content[0],{
          onScrollStart:this.disableGesture.bind(this),
          lockDirection: true,
          hScroll: false,
          hideScrollbar: true,
          fadeScrollbar: true
        });
    },
    disableGesture:function(e){
      e.stopPropagation();
      e.preventDefault();
    },
    modelEvents:{
      "change:content":"renderContent",
    },
    events:{
      "click .exit":"hide",
      "swipe":"disableGesture"
    },
    obEvents: {
      "book:zoom.in":"zoomin",
      "book:zoom.out":"zoomout",
      "system:change.mode":"modeChange",
      "book:turn":"hide",
    },
    renderContent:function(model,value){
      this.$content.find('div').html(value);
      this.$scroll.refresh();
    },  
    modeChange:function(oldMode,newMode){
      if (oldMode != this.mode && newMode != this.mode) return ;
      if (oldMode == this.mode && newMode != "toc") return this.hide();
      if (oldMode != "toc" && newMode == this.mode) return this.show();
    },
    zoomin:function(){
      this.$el.addClass("zoomin");
      this.$button.zoomin();
    },
    zoomout:function(){
      this.$el.removeClass("zoomin");
      this.$button.zoomout();
    },
    show: function () {
      this.$el.addClass("active");
      this.emit("system:enter.mode","assistant","reader");
    },
    hide: function () {
      this.$el.removeClass("active");
      this.$button.show();
      this.emit("system:exit.mode","assistent");
    },
    render: function () {
      this.$el.html(Tpl({}));
      this.$el.appendTo($("#reader-stage"));
    }
  });
  return View;
});
