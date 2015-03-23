define(function (require, exports, module) {
  var View = require("./view");
  var Model = require("./model");
  var Backbone = require("backbone");
  var observer = require("pkg!observer");
  var config = require("pkg!config");
  var $ = require("jquery");
  var _ = require("underscore");


  var mixin = function (view, mixin, custom) {
    if (custom) {
      if (custom.events && mixin.events) {
        mixin = _.clone(mixin);
        _.defaults(custom.events, mixin.events);
      }
      _.extend(mixin, custom);
    }
    var source = view.prototype || view;
    _.defaults(source, mixin);
    if (mixin.events) {
      if (source.events) {
        _.defaults(source.events, mixin.events);
      } else {
        source.events = mixin.events;
      }
    }
    if (mixin.initialize !== undefined) {
      var oldInitialize = source.initialize;
      source.initialize = function () {
        mixin.initialize.apply(this, arguments);
        oldInitialize.apply(this, arguments);
      };
    }
  };

  return {
    View: View,
    Events: Backbone.Events,
    Model: Model,
    Collection: Backbone.Collection,
    observer: observer,
    config: config,
    mixin: mixin,
    $: $
  };
});
