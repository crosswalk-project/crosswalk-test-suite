define(function (require, exports, module) {

  var Backbone = require("backbone");
  var observer = require("pkg!observer");

  return Backbone.View.extend({
    constructor: function () {
      Backbone.View.apply(this, arguments);
      this.registerOnObserver();
      this.registerOnModel();
    },
    registerOnObserver: function () {
      this.registerEvents("obEvents", observer);
    },
    registerEvents: function (attrName, obj) {
      var events = this[attrName];
      if (!events) return;
      for (var key in events) {
        var method = events[key];
        if (!_.isFunction(method)) method = this[events[key]];
        if (!method) throw new Error(attrName + " Bind : Method \"" + events[key] + "\" does not exist");
        method = _.bind(method, this);
        obj.on(key, method);
      }
    },
    registerOnModel: function () {
      this.registerEvents("modelEvents", this.model);
    },
    emit: function () {
      observer.trigger.apply(observer, arguments);
    },
    emitAsync: function () {
      var args = arguments;
      setZeroTimeout(function () {
        observer.trigger.apply(observer, args);
      });
    }
  });
});
