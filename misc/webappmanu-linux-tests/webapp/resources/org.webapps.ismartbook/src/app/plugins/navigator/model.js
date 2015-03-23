define(function (require, exports, module) {
  var Plugin = require("pkg!pluginBase");
  var config = Plugin.config;

  var Model = Plugin.Model.extend({
    defaults: {
      hundred: 0,
      ten: 0,
      single: 0,
      maxHundred: 0,
      maxTen: 0,
      maxSingle: 0,
      page: 0
    },
    init: function () {
      var numbers = this.parseNumber(config.get("ebook").get("pageCount"));

      this.set("hundred", numbers[0]);
      this.set("ten", numbers[1]);
      this.set("single", numbers[2]);

      this.set("maxHundred", this.maxHundred());
      this.set("maxTen", this.maxTen());
      this.set("maxSingle", this.maxSingle());
    },
    parseNumber: function (number) {
      var single = parseInt(number % 10, 10),
        ten = parseInt((number / 10) % 10, 10),
        hundred = parseInt((number / 100) % 10, 10);
      return [hundred, ten, single];
    },
    getNumber: function (numbers) {
      var page = 0;

      if (_.isArray(numbers)) {
        page += numbers[0] * 100;
        page += numbers[1] * 10;
        page += numbers[2] * 1;
      } else {
        page = parseInt(page, 10);
      }

      if (!page) page = 1;

      return page;
    },
    setPage: function (page) {
      page = parseInt(page, 10);
      this.set("page", page);
      return page;
    },
    hasHundred: function () {
      return !!this.get("hunred");
    },
    hasTen: function () {
      return this.get("ten") || this.get("hundred");
    },
    maxHundred: function () {
      return this.get("hundred");
    },
    maxTen: function () {
      return this.get("hundred") ? 9 : this.get("ten");
    },
    maxSingle: function () {
      return this.get("maxTen") ? 9 : this.get("single");
    }
  });
  return Model;
});
