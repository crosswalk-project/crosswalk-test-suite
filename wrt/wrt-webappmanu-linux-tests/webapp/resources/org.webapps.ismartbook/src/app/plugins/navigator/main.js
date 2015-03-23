define(function (require, exports, module) {
  var PluginBase = require("pkg!pluginBase");
  var PageModel = require("./model");

  var Tpl = require("tpl!./page");

  var View = PluginBase.View.extend({
    id: "nav",
    initialize: function () {
      this.emit("system:register.end", "init", "navigator:end.init");

      this.model = new PageModel({});
      this.model.set("page", 1);

      this.$el.appendTo($("#book-stage"));
    },
    events: {
      "click .nav-text,.nav-arrow": "toggle",
      "click .nav-button button": "gotoPage"
    },

    modeChange: function (oldMode, newMode) {

      // from toc to reader/assistant, navigator need exist;
      if (oldMode == "toc" && (newMode == "reader" || newMode == "assistant")) return this.show();

      // from any to toc , navigator always needs hide.
      if (newMode == "toc") return this.hide();

      // from reader to assistant, if this is actived, it needs to be deactived;
      if (newMode == "assistant") return this.deactive();
    },
    init: function () {
      this.model.init();

      var data = this.model.toJSON();
      this.render(data);

      this.$hundred = this.$el.find("[name=hundred]");
      this.$ten = this.$el.find("[name=ten]");
      this.$single = this.$el.find("[name=single]");

      this.changePage(1);
      this.emitAsync("navigator:end.init");
    },
    obEvents: {
      "system:change.mode": "modeChange",
      "book:end.preload": "init",
      "book:turned": "changePage",
      "book:turn": "deactive"
    },
    toggle: function () {
      if (this.$el.hasClass("active")) return this.deactive();
      return this.active();
    },
    active: function () {
      this.$el.addClass("active");
    },
    deactive: function () {
      this.$el.removeClass("active");
    },
    show: function () {
      this.$el.removeClass("hide");
    },
    hide: function () {

      this.deactive();
      this.$el.addClass("hide");
    },
    gotoPage: function () {

      this.deactive();

      var hundred = this.$hundred.size() ? this.$hundred.val() : 0;
      var ten = this.$ten.size() ? this.$ten.val() : 0;
      var single = this.$single.size() ? this.$single.val() : 0;
      var page = this.model.getNumber([hundred, ten, single]);

      this.emit("book:turn", page);
    },
    changePage: function (page) {
      var numbers = this.model.parseNumber(page);

      this.$hundred.val(numbers[0]);
      this.$ten.val(numbers[1]);
      this.$single.val(numbers[2]);

      this.$page.html(page);
      console.timeEnd('render new page');
      console.log('-----------------------------');

    },
    render: function (data) {
      this.$el.html(Tpl(data));
      this.$page = this.$el.find(".nav-page");
    }

  });
  return View;
});
