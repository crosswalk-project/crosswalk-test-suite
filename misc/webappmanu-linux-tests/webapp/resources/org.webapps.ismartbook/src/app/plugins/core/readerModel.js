define(function (require, exports, module) {
  var observer = require("pkg!observer");
  var config = require("pkg!config");
  var PluginBase = require("pkg!pluginBase");

  /**
   * ReaderModel
   * @type {[type]}
   */
  var ReaderModel = PluginBase.Model.extend({
    defaults: {
      Ebook: {},
      observer: observer,
      config: config,
      register: {
        "init": [],
        "preload": []
      },
      triggered: {
        "init": [],
        "preload": []
      },
      endEvent: {
        "init": "book:end.init",
        "preload": "book:end.preload"
      }
    },
    initialize: function () {
      var self = this;

      // 监听插件的注册end preload 事件。
      observer.on("system:register.end.preload",
      this.addEndEvent.bind(this, 'preload'));

      // 监听插件的注册end init 事件。
      observer.on("system:register.end.init",
      this.addEndEvent.bind(this, 'init'));

      var hash = window.location.hash;
      //get start page from hash
      config.set('start',hash ? parseInt(hash.replace('#',''),10):1);
    },
    obEvents: {
      "system:register.end": "addEndEvent"
    },
    addEndEvent: function (type, eventName) {

      list = this.get("register")[type];

      // 检查事件是否有重复
      if (list.indexOf(eventName) > -1) {
        throw (new Error(type + "endEvent :" + eventName + " is already added"));
      }

      // 将事件写到事件表里面去
      list.push(eventName);

      // 监听注册该事件的触发情况
      observer.on(eventName, this.checkEventsEnd.bind(this, type, eventName));
    },
    checkEventsEnd: function (type, eventName) {

      // 获取事件列表
      var list = this.get('register')[type];

      // 已经触发的事件列表
      var triggered = this.get('triggered')[type];

      // 在所有事件都触发完之后系统需要触发的事件
      var endEvent = this.get("endEvent")[type];
      var ebook;

      // 检查事件是否执行了两遍
      if (triggered.indexOf(eventName) > -1) {
        throw (new Error(eventName + " runs twice"));
      }

      triggered.push(eventName);

      //检查如果长度相等，并且没有差异，则执行对应的end 事件
      if (triggered.length != list.length || _.difference(list, triggered).length !== 0) {
        return;
      }

      // 因为书本不会再执行 end 事件，所以取消注册的事件以及注册事件的函数。
      list.push("system:regsiter.end." + type);

      list.forEach(function (item) {
        observer.off(item);
      });

      //异步触发 end event
      this.emitAsync(endEvent);
    }
  });

  return ReaderModel;
});
