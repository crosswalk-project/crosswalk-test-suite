/**
 * Observer 类
 * 用来做控件之间的消息中转。
 * 所有的API 均继承于Backbone.Event 
 * @class
 * @author William Ge<weix.ge@intel.com>
 * @see http://backbonejs.org/#Events
 *
 */
define(function (require, exports, module) {
  var Backbone = require("backbone");
  var _ = require("underscore");
  return _.extend({}, Backbone.Events);
});
