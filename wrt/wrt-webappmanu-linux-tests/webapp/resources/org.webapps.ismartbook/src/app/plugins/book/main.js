define(function (require, exports, module) {
  var base = require("pkg!pluginBase");
  var config = require("pkg!config");
  // var singlePage = require("./singlePageWithBlock/view");
  // var singlePage = require("./singlePage/view");
  var singlePage = require("./customSinglePage/view");
  // var FPSmeter = require("pkg!fps");

  var BookView = base.View.extend({
    el: "#book-stage",
    initialize: function () {
      this.BookView = new singlePage();
      this.emit("system:register.end", "init", "page:end.preload");
    },
    obEvents: {
      // "system:enter.mode": "modeChange",
      "book:zoom.in": "zoomIn",
      "book:zoom.out": "zoomOut",

      "sync:cmd.turn": "toPage",
      "sync:cmd.page.endable": "unlockPage",
      "sync:cmd.page.disable": "lockPage",

      "book:turn": "toPage",
      "book:turned": "removeAnimation",
      "book:end.preload": "endInit",
      "gesture:swipe":"swipe"
    },
    swipe:function(dir,evt){
      if (dir === "left"){
        console.time("flip page");
        console.profile("flip page");
        this.emit("book:turn","next");
        return ;
      }

      if (dir === "right"){
        console.time("flip page");
        console.profile("flip page");
        this.emit("book:turn","prev");
        return ;
      }

    },
    toPage: function (page, force) {
     
      console.timeStamp("flip page");
      /* zoom mode doesn"t  turn page */
      if (!force && this.$el.hasClass("zoom")) return;
     // this.$el.addClass("flip");
      this.BookView.toPage(page);
    },
    removeAnimation: function () {
     // this.$el.removeClass("flip");
    },
    unlockPage: function () {
      this.BookView.unlockPage();
    },
    lockPage: function () {
      this.BookView.lockPage();
    },
    zoomIn: function () {
      this.$el.addClass("zoom");
    },
    zoomOut: function () {
      this.$el.removeClass("zoom");
    },
    endInit: function (ebook) {
      this.BookView.endInit(ebook);
    }
  });

  return BookView;
});
