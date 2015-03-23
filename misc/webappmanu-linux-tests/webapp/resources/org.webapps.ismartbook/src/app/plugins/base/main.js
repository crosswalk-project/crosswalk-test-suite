/**
 * 控件基础类
 * 在Backbone.View上增加一些控件常用的方法
 * @class
 * @return {Object} 一个基础类，控件可以在这个基础上继续扩展。
 */
define(function (require, exports, module) {
  "use strict";

  var Base, Backbone, config;
  // 定义一个Base Object
  Base = {};

  // // 加载所需要的模块
  Backbone = require("./backbone.extend");

  config = require("pkg!config");

  // 赋值基础类
  Base.View = require("./view");
  Base.Model = require("./model");
  Base.Collection = require("./collection");
  Base.Storage = require("pkg!storage");


  /**
   * 书本的内容，控件可以通过这个类来获取到所有书本的相关信息
   * @type {Object}
   * @class
   * @todo 这个是有必要的么？
   */
  Base.ebook = config.get("ebook");

  /**
   * 书本的全路径
   * @type {String}
   * @example `http://localhost/book/OEBPS`
   */
  Base.fullPath = Base.ebook.get("fullPath") + "/OEBPS/";


  /**
   * 书本是不是控制端，如果为0则为学生端的。方便控件层面针对两个不通的终端做交互限制
   * @type {Boolen}
   */
  Base.controller = config.get("controller");

  return Base;
});
