define(function (require, exports, module) {
  "use strict";
  var PluginBase, TocModel, tpl, iScroll, View, _, systemMode;

  PluginBase = require("pkg!pluginBase");

  TocModel = require("./model");

  tpl = require("tpl!./toc");

  iScroll = require("iscroll");

  _ = require("underscore");

  systemMode = require("pkg!systemMode");

  View = PluginBase.View.extend({
    itemWidth: 0,
    id: "toc",
    mode: "toc",
    initialize: function () {
      this.model = new TocModel({});
      this.model.set("state", 0);
      this.$el.appendTo($("body"));
      this.emit("system:register.end", "init", "toc:end.init");
    },
    init: function () {
      this.model.init();
      this.emitAsync("toc:end.init");
    },
    events: {
      "click .toc-button": "toggle",
      "click .toc-page": "toPage"
    },
    obEvents: {
      "system:change.mode": "modeChange",
      "book:end.preload": "init",
      "book:turned": "activePage",
      "gesture:swipe":"swipe"
    },
    modelEvents: {
      "change:state": "toggle",
      "change:toc": "render"
    },

    swipe:function(dir,evt){
      
    },
    modeChange: function (oldMode, newMode) {
      if (newMode !== this.mode && oldMode !== this.mode) {return ;}

      if (newMode === this.mode) {return this.show();}

      if (oldMode === this.mode)  {return this.hide();}

    },
    toggle: function () {
      if (this.el.classList.add("active")) {return this.hide();}
      return this.show();
    },
    show: function () {
      this.el.classList.add("active");
      this.emit("book:disable.action");
      this.emit("book:zoom.in");

    },
    hide: function () {
      this.el.classList.remove("active");
      this.emit("book:enable.action");
      this.emit("book:zoom.out");
    },
    toPage: function (evt) {
      if (this.$list.moved) return;
      var page = evt.currentTarget.dataset.page;
      page = this.model.get("toc").orders.indexOf(page) + 1;
      this.activePage(page, 250);
      this.emitAsync("book:turn", page, true);
    },
    activePage: function (page, scrollTimeOut) {

      if (!page) return;

      var activePage = this.model.get("activePage");
      if (page === activePage) {return ;}

      var length = this.model.get("length");

      if (page == "prev") {
        activePage = activePage && (activePage - 1) <= 1 ? 1 : activePage - 1;
      } else if (page == "next") {
        activePage = activePage && (activePage + 1) >= length ? length : activePage + 1;
      } else if (_.isNumber(page) && page >= 1 && page <= length) {
        activePage = page;
      }

      this.model.set("activePage", activePage);
      this.$el.find(".current").removeClass("current");
      this.$page.eq(activePage - 1).addClass("current");
      if (!scrollTimeOut) scrollTimeOut = 0;
      this.$list.scrollToElement(this.$el.find(".current")[0], scrollTimeOut, true);
    },
    render: function () {
      var data = {};
      data.toc = _.extend({}, this.model.get("toc").points);

      var tmp = [];
      // make sure content"s length is bigger than the sum of items" length 
      var count = 1;

      _.each(data.toc, function (item) {
        tmp.push(item);
        count++;
      });

      data.toc = tmp;

      data.fullPath = this.model.get("fullPath");

      var html = tpl(data);
      this.$el.html(html);

      // set content length 
      var $firstItem = this.$el.find(".toc-page").first();
      var itemWidth = $firstItem.width();
      itemWidth += parseInt($firstItem.css("margin-left"), 10);
      this.$el.find(".toc-content").width(itemWidth * count);
      this.$page = this.$el.find(".toc-page");
      this.$list = new iScroll(this.$el[0], {
        lockDirection: true,
        vScroll: false,
        hideScrollbar: true,
        fadeScrollbar: true,
        bounce: true,
        useTransition: true
      });

      this.activePage(1);
    }

  });
  return View;
});
