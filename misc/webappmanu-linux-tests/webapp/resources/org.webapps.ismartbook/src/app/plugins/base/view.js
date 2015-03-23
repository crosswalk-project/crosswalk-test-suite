define(function(require, exports, module) {
  var Backbone = require("./backbone.extend"),
    $ = Backbone.$,
    observer = require("pkg!observer"),
    config = require("pkg!config"),
    fullPath = config.get("ebook").get("fullPath") + "/OEBPS/",
    number = 0,
    disableClick = 0,
    time = 1000;

  function setDisableClick() {
    disableClick = 1;
    setTimeout(function() {
      disableClick = 0;
    }, 10);
  }

  observer.on("book:turn", setDisableClick);
  observer.on("gesture:swipe", setDisableClick);
  observer.on("gesture:pinchin", setDisableClick);
  observer.on("gesture:pinchout", setDisableClick);



  /**
   * 扩展的Backbone.View的内容
   * @class
   * @type {Object}
   */
  var View = Backbone.View.extend({
    constructor: function($el, data, page, pageOb) {
      var itemId = $el[0].dataset.id;

      if (page) {
        this.page = page;
      }
      if (pageOb) {
        this.pageOb = pageOb;
      }

      this.itemId = itemId || "subItem-" + (number + 1);

      this.setElement($el[0], false);

      View.__super__.constructor.apply(this, [$el, data]);
      this.registerOnPage(pageOb);
      this.registerOnModel();
    },
    registerEvents: function(attrName, obj, namespace) {
      var events = this[attrName];
      var eventName;
      if (!events || !obj) return;
      this.unRegisterEvents(obj);
      for (var key in events) {
        var method = events[key];
        if (!_.isFunction(method)) method = this[events[key]];
        if (!method) throw new Error(attrName + " Bind : Method '" + events[key] + "' does not exist");
        method = _.bind(method, this);
        eventName = namespace ? namespace + ":" + key : key;
        this.listenTo(obj, eventName, method);
      }
    },
    unRegisterEvents: function(obj) {
      if (obj && obj.off) {
        obj.off(null, null, this);
      }
    },
    registerOnModel: function() {
      this.registerEvents("modelEvents", this.model);
    },
    registerOnPage: function(pageOb) {
      this.registerEvents("pageEvents", pageOb, "page");
    },
    delegateEvents: function(events) {
      var delegateEventSplitter = /^(\S+)\s*(.*)$/,
        keys;
      if (!(events || (events = _.result(this, 'events')))) return this;
      this.undelegateEvents();

      keys = Object.keys(events);

      keys.forEach(function(key) {
        var fn, match, eventName, method;

        fn = events[key];
        if (!_.isFunction(fn)) fn = this[events[key]];
        if (!fn) return;

        match = key.match(delegateEventSplitter);
        eventName = match[1], selector = match[2];

        fn = _.bind(fn, this);

        if (eventName == "click") {
          method = function(e) {
            if (disableClick) {
              e.stopPropagation();
              e.preventDefault();
              return false;
            }
            fn(e);
          }.bind(this);

        } else {
          method = fn;
        }

        eventName += ".delegateEvents" + this.cid;
        if (selector === "") {
          this.$el.on(eventName, method);
        } else {
          this.$el.on(eventName, selector, method);
        }

      }.bind(this));

      return this;
    },
    systemDisable: function() {
      return disableClick;
    },
    initialize: function($el, config, page) {},
    /**
     * 发送信息到其他控件来通知其他控件进行一些操作
     * @message unit:message
     * @param  {Object} msg    需要传递的内容
     * @param  {Number} toPage 传递内容去哪个页面
     */
    send: function(msg, toPage) {
      var itemId = this.itemId;
      var page = this.page;
      observer.trigger("unit:message", toPage, msg, page, cid);
    },
    /**
     * 接收传递进来的消息的函数
     * 同步的内容和发送消息的内容最终都会由其他控件的这个结构
     * @param  {Object} msg  传递过来的对象，控件通过这个对象来判断是否是它自己的所需要的内容
     * @param  {Number} page 是哪个页面的内容
     * @param  {String} cid  对方控件的cid，由Backbone来生成
     */
    onMessage: function(msg, page) {},
    /**
     * 停止控件的行为
     * 如果控件有一些动画行为、视频、音频，最好是定义这个函数来停止自己关联的媒体。
     * 避免翻页的时候视频和音频还在不断的播放
     */
    stopAll: function() {},
    /**
     * 播放控件的行为
     */
    playAll: function() {},
    /**
     * 添加自己的样式
     * @param {String} style 样式相对的控件目录的位置
     */
    addClass: function(style) {
      // 通过this.name获取到当前的控件的目录，拼接出来样式的绝对路径
      // 将href作为一个查找条件，看看页面里面是否已经有，如果没有的话则增加这个样式
      var href;

      if (/^http\:\/\//.test(style)) {
        href = style;
      } else {
        href = fullPath + "./controls/" + this.controlName + "/" + style;
      }


      var $link = $("link[href='" + href + "']");
      if ($link.size()) return;
      $("<link>").attr("href", href).attr("rel", "stylesheet").appendTo($("head"));
    },
    /**
     * 发送同步信息，用来做两个终端的操作联动
     * @param  {Object} data 需要发送的操作相关的信息
     */
    sync: function(data) {
      if (this.isSubItem()) return false;

      data.page = this.page;
      data.itemId = this.itemId;
      observer.trigger("sync:send", "unit", data);
    },
    isSubItem: function() {
      return !this.pageOb ? true : false;
    },
    emit: function(name) {
      var isSubItem = this.isSubItem();
      var args = Array.prototype.slice.call(arguments, 1);
      name = !isSubItem ? "page:" + name : name;
      args.splice(0, 0, name, this.itemId);

      if (isSubItem) {
        this.trigger.apply(this, args);
        return;
      }

      this.pageOb.trigger.apply(this.pageOb, args);
    },
    show: function() {
      var method = this.$el[0].dataset.show;
      this._clearAnimationClass();
      if (!method) {
        this.$el.show();
      } else {
        this.$el.show();
        this.$el.addClass('animated ' + method);
        this._timer = setTimeout(function() {
          this._clearAnimationClass();
        
        }.bind(this), time);
      }


      this.emit("show." + this.controlName, this.itemId);
    },
    _clearAnimationClass: function() {
      if (this._timer) {
        clearTimeout(this._timer);
        this._timer = null;
      }

      var elData = this.$el[0].dataset;
      var showMethod = elData.show || '';
      var hideMethod = elData.hide || '';
      var classes = ['animated', showMethod, hideMethod].join(' ');
      this.$el.removeClass(classes);
    },
    hide: function() {
      var method = this.$el[0].dataset.hide;
      this._clearAnimationClass();
      if (!method) {
        this.$el.hide();
      } else {
        this.$el.addClass('animated ' + method);
        this._timer = setTimeout(function() {
          this._clearAnimationClass();
          this.$el.hide();
        }.bind(this), time);
      }

      this.emit("hide." + this.controlName, this.itemId);
    },
    /* unused */
    pageInitEnd: function() {}

  });

  return View;
});