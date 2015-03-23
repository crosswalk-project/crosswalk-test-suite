define(function (require, exports, module) {
  var Base = require("pkg!pluginBase");

  var Tpl = require("tpl!./overview");


  var View = Base.View.extend({
    id: "assistant-overview",
    initialize: function (model) {
      this.model = model;
      this.$el.appendTo($("#reader-stage"));
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
    events:{
      "swipe":"disableGesture"
    },
    disableGesture:function(e){
      e.stopPropagation();
      e.preventDefault();
    },
    modelEvents:{
      "change:content":"renderContent"
    },
    obEvents: {
      "system:change.mode":"modeChange"
    },
    renderContent:function(model,value){
      this.$content.find('div').html(value);
      setZeroTimeout(function(){
        this.$scroll.refresh();
      }.bind(this));
    },
    modeChange:function(oldMode,newMode,isEnter){
      
      if (oldMode == "toc") return this.hide();
      if (newMode == "toc") return this.show();
    },  
    show: function () {
      this.$el.addClass("active");
    },
    hide: function () {
      this.$el.removeClass("active");
    },
    render: function () {
      this.$el.html(Tpl({}));
    }
  });
  return View;
});
