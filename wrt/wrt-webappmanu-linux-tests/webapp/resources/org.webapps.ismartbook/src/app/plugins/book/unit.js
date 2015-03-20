define(function (require, exports, module) {
  // modules 
  var base = require("pkg!pluginBase");
  var observer = base.observer;
  var Connect = require("./connect");
  var Controls = require("./controls");
  // cache 
  var PageCache = {};

  // start preload function
  observer.on("book:end.parse", function (ebook) {
    Connect.cache(ebook);
    Controls.cache(ebook);
  });



  /**
   * 将unit的内容缓存到对应的page
   * @param {Number} page 当前的页数
   * @param {Object} unit 控件对象
   */
  function addUnitCacheToPage(page, unit) {
    PageCache[page] = unit;
    Connect.registerSignal(unit);
    unit.initEnd();
  }
  // 绑定`unit:add`事件到addUnitCacheToPage
  observer.on("unit:add", addUnitCacheToPage);

  /**
   * 书本内部的控件交互
   * @param {Number} toPage 要传递到哪个page，主要是用来做交互的
   * @param {Object} msg    传递的消息
   * @param {Number} page   传递进来的page
   * @param {String} cid    Backbone生成的一个id
   */
  function Message(toPage, msg, page, cid) {
    PageCache[toPage].message(msg, page, cid);
  }
  observer.on("unit:message", Message);

  /**
   * 删除页面对应的cachen内容
   * @param  {Number} page 要删除的页数
   */
  function clearCache(page) {
    if (page && PageCache[page]) delete PageCache[page];
  }
  // 触发`unit:clear.cache` 的时候删除传递过来的缓存
  observer.on("unit:clear.cache", clearCache);

  /**
   * 将当前页面所有的控件全部停止下来
   * @param  {Number} page 页面数
   */
  function stopUnit(page) {
    _.each(PageCache, function (item) {
      if (item.page == page) item.stop();
    });
  }
  // 绑定函数到`unit:stop`上面
  observer.on("unit:stop", stopUnit);

  function turnedUnit(page) {
    _.any(PageCache, function (item) {
      if (item.page != page) return false;

      item.pageShow();
      return true;

    });
  }
  observer.on("book:turned", turnedUnit);


  /**
   * 将控件发出的同步内容通知到当前页面的各个控件
   * @param  {Object} data 从server端获取的内容
   */
  function syncUnitCommand(data) {
    if (data.page && PageCache[data.page]) {
      PageCache[data.page].message(data);
    }
  }
  // 绑定到`sync:cmd.unit`上
  observer.on("sync:cmd.unit", syncUnitCommand);



  /**
   * Unit类
   * 1. 渲染unit
   * 2. 渲染单独的Controls
   * @param {jQuery DOM} $content jQuery代码片段
   * @param {Number} page   页面页数
   */
  var Unit = function ($content, page) {
    this.page = page;
    this.cache = [];
    this.pageOb = _.extend({}, base.Events);
    Controls.render($content, page, this.cache, this.pageOb);
    return this;
  };
  /**
   * Unit 类的方法
   * @type {Object}
   */
  Unit.prototype = {
    /**
     * 将当前页面所有的控件行为都停止下来
     */
    stop: function () {
      this.cache.forEach(function (unit) {
        // 如果当前cache的这个对象有stop的话，就执行这个函数
        if (unit.stopAll) unit.stopAll();
        //unit.reset && unit.reset();
      });
    },
    /**
     * 给页面里面的所有控件传递信息
     * 调用的是unit的onMessage函数。
     * @param  {Object} msg  需要传递的信息
     * @param  {Number} page 当前的页面
     * @param  {String} cid  控件的cid，这个是Backbone在实例化控件的时候所产生的id值
     */

    message: function (msg, page, cid) {
      this.cache.forEach(function (unit) {
        if (unit.onMessage) unit.onMessage(msg, page, cid);
      });
    },
    /**
     * 触发当前页面所有缓存的控件的playAll函数
     * @return {[type]} [description]
     */

    play: function () {
      this.cache.forEach(function (unit) {
        if (unit.playAll) unit.playAll();
      });
      observer.trigger("unit:play", this.page);
    },
    pageShow: function () {
      this.cache.forEach(function (unit) {
        if (unit.systemPageShow) {
          unit.systemPageShow();
        }
      });
      this.pageOb.trigger("page:show.page");
    },
    initEnd: function () {
      this.cache.forEach(function (unit) {
        if (unit.pageInitEnd) unit.pageInitEnd();
      });
      this.pageOb.trigger("page:init.end", this.page);
    }
  };

  return Unit;
});
