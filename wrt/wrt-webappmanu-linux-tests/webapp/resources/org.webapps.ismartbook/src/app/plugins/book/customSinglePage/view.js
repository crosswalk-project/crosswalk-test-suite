define(function (require, exports, module) {
  /**
   * Base of Plugin.
   * @type {Object}
   */
  var PluginBase = require("pkg!pluginBase");
  // var FPSmeter = require("pkg!fps");
  /**
   * System config.
   * @type {Object}
   */
  var config = PluginBase.config;
  /**
   * Book Page template function
   * @type {Function}
   */
  var pageTpl = require("tpl!./page");
  /**
   * Unit Class from unit.js
   * @type {Function}
   */
  var Unit = require("../unit");
  /**
   * Book Model.
   * @type {Function}
   */
  var BookModel = require("./model");
  /**
   * new Book Flip library.
   * @type {Function}
   */
  var BookFlip = require("./bookflip");

  var SinglePageView = PluginBase.View.extend({
    /**
     * id of View Dom.
     */
    id: "book",
    /**
     * initialize function
     */
    initialize: function () {
      this.$el.addClass("bb-bookblock").appendTo($("#book-stage"));
      this.model = new BookModel({});
      this.controller = config.get("controller");
    },
    /**
     * View Events
     */
    events: {
      // Disable mouse event if page-cover is disabled.
      "mousemove .page-cover.disable": "disable",
      "mouseover .page-cover.disable": "disable",
      "mouseout .page-cover.disable": "disable",
      "click .page-cover.disable": "disable",
      "mouseup .page-cover.disable": "disable",
      "mousedown .page-cover.disable": "disable",

      // Page Flip
      "click .page-nav-button ": "toPageWithPageId",
      "click .left-bottom-button ": function(){
        this.emitAsync("book:turn","prev");
      },
      "click .right-bottom-button, .right-top-button": function(){
        this.emitAsync("book:turn","next");
      }
    },
    /**
     * Intialize BookView when book end parse.
     * @param {Object} ebook
     */
    endInit: function (ebook) {
      // TODO  is this ebook equal config.get("ebook") ?
      ebook = this.ebook = config.get("ebook");

      // TODO opf  parse
      this.model.set({
        pageCount: ebook.pageCount(),
        title: ebook.get("ncx").title,
        controller: config.get("controller"),
        fullpath: ebook.get("fullPath") + "/OEBPS/",
        ncx: ebook.get("ncx")
      });

      // add Blank page;
      this.addBlankPages();

      this.$el.find(".page-nav-button").click(function(){
        "use strict";
        console.time("flip page");
        console.profile("flip page");
      });

      // set title
      this.setTitle();
    
      this.BookFlip = new BookFlip({
        onstart: this.beforeFlip.bind(this),
        onend: this.afterFlip.bind(this),
        item: ".page",
        activePage:config.get('start'),
        speed:config.get("speed")
      }, this.$el);

      this.$pageList = this.$el.find(".page-content");

      this.addPage(config.get('start'), function () {
        this.afterFlip(config.get('start')-1, config.get('start'));
        this.emitAsync("page:end.preload", ebook);
      }.bind(this));

    },
    /**
     * Disable mouse event if page-cover is disabled.
     * @param {jQEvent} e jquery mouse event
     * @returns {boolean}
     */
    disable: function (e) {
      e.stopPropagation();
      e.preventDefault();
      return false;
    },
    /**
     * Set Document title as book title.
     *
     */
    setTitle: function () {
      var title = this.model.get("title");
      document.title = title;
    },
    /**
     * Flip to next page.
     */
    next: function () {
      this.toPage("next");
     
    },
    /**
     * Flip to previous page .
     */
    prev: function () {
     this.toPage("prev");
    },
    /**
     * The entrance of jump page.
     * If page is a string, run `next` or `prev`.
     * If page is a number, book will flip to this number.
     * @param page
     * @returns {*}
     */
    toPage: function (page) {
      // FPSmeter.run(0.01);
      console.time("flip page");
      this.BookFlip.startFlip = new Date().getTime();
    
      if (page === "next" || page === "prev") {
        return this.BookFlip[page]();
      }

      this.BookFlip.jump(page);

    },
    /**
     * When book flip is done,
     * compare the new page range with  old page range, and find out which
     * pages need to be removed and which pages need to be added to the DOM.
     * Then trigger the book:turned event to tell other plugins the book
     * is flip to the new page.
     *
     * @param oldPage
     * @param newPage
     */
    afterFlip: function (oldPage, newPage) {
      var rangeLength, pageCount, min, max, oldRange, newRange
     // this.$el.removeClass("flip");

      // how many page contents will be loaded.
      rangeLength = this.model.get("rangeLength");

      // get the min and max page number.
      pageCount = this.model.get("pageCount");
      min = Math.max(newPage - parseInt(rangeLength / 2, 10), 1);
      max = Math.min(min + rangeLength, pageCount + 1);

      // get range of old page numbers ;
      oldRange = this.model.get("activePage");

      // get range of new page numbers;
      newRange = _.range(min, max);

      // Add page;
      _.difference(newRange, oldRange)
        .forEach(this.addPage.bind(this));

      // get page numbers which need to be removed;
      _.difference(oldRange, newRange)
        .forEach(this.removePage.bind(this));

      // Set the new range to model.activePage
      this.model.set("activePage", newRange);

      this.emitAsync("book:turned", newPage);

    },
    /**
     * Remove page content from dom,
     * and trigger event to let unit clear this pageUnit from its cache.
     * @param {number} page which page need to be removed.
     */
    removePage: function (page) {

      this.$pageList.eq(page).empty();
      this.emit("unit:clear.cache", page);

    },
    /**
     * Load page content with etb.js
     *
     * @param {Number} p the page number you want to add to page.
     * @param {Function} callback run it if page is  loaded  successful.
     */
    addPage: function (p, callback) {
      var ebook, loadEnd;

      ebook = config.get("ebook");
      /**
       * When etb.js give the page content,
       * insert it to book content area, and format it with controls.
       * @param err {error} etb can't get content of this page, or this page is not defined.
       * @param result {string} html content of this page .
       */
      loadEnd = function (err, result) {

        if (err) {
          throw Error("Book Page load Error");
        }

        this.setPageCache(p, result.content);

        // if callback is existed, run it .
        if (_.isFunction(callback)) {
          callback(p);
        }
      };
     
      // load page with ebook load function
      ebook.loadByPage(p, loadEnd.bind(this));
    },
    /**
     * Format page content with controls of ebook.
     * @param {number} p  the number which page the pageContent belong to.
     * @param {string} pageContent the html content of this page.
     */
    setPageCache: function (p, pageContent) {
      var $pageContent = this.$pageList.eq(p);
      $pageContent.html(pageContent);
      this.emit("unit:add", p, new Unit($pageContent, p));

    },
    addBlankPages: function () {
      var pageCount = this.model.get("pageCount");
      var points = this.model.get("ncx").points;
      var orders = this.model.get("ncx").orders;
      var modules = this.model.get("ncx").modules;
      var temp = {};
      var html = "";
      var page = {};
      var pageId;
      this.pages = [];
      var maxPage = pageCount + 1;

      for (var i = 0; i < maxPage; i++) {
        temp = {};
  
        temp.lastLeft = 0;
        temp.lastRight = 0;

        if (i == maxPage -1 ) {
          temp.lastRight = 1;
        }
        if (i == maxPage - 2 ) {
          temp.lastLeft = 1;
        }
        
        temp.num = i;
        temp.st = !this.controller;
        pageId = orders[i];
        if (pageId) {
          page = points[pageId];
          temp.module = page.module;
          temp.unit = page.unit;
          temp.id = page.id;
          temp.pages = modules[page.module][page.unit].pages;
          if (temp.module) {
            temp.lastLeft = 0;
          }
        }

        html += pageTpl(temp);

      }
      this.$el.append(html);

    },
    /**
     * Before book do flip animation,
     * stop all animations of controls,
     * and send message to client if this book is controller.
     *
     * @param  {number} oldPage the number of active page before flip.
     * @param  {number} newPage the numebr of active page after flip.
     */
    beforeFlip: function (oldPage, newPage) {

      // Send Message to client if this book is used by teacher.
      this.emit("sync:send", "turn", newPage);

      // if this book is not used by teacher, lock the page
      if (!this.controller) this.lockPage();
      // this.$el.addClass("flip");
      // Stop aniamtions of controls before book flip.
      this.emit("unit:stop", oldPage);

    },
    /**
     * When user click page buttons below bookmark,
     * we can get page number and emit book:turn event.
     *
     * @param  {jqEvent} evt jQuery click Event.
     */
    toPageWithPageId: function (evt) {
     console.time("click trigger");
      //console.time("flip page");
      var $target = $(evt.target);

      // If user click current page button, do nothing.
      if ($target.hasClass("current")) {
        return false;
      }

      var pageId = $target.data("page");
      var page = config.get("ebook").get("id2page")[pageId];

      // If doesn't find page number with page id, return ;
      if (!page) {
        return false;
      }

      // Emit book turn to reader.
      this.emitAsync("book:turn", page);
      return true;
    }
  });
  return SinglePageView;
});