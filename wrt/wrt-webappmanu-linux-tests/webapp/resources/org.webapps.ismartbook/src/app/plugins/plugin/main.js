define(function (require, exports, module) {

  var _ = require("underscore");
  var Base = require("pkg!pluginBase");

  var Plugins = Base.Model.extend({
    initialize: function (plugins) {
      this.plugins = plugins;
      this.cache = {};
      this.load();
    },
    load: function () {

      var plugins = this.plugins;
      var cache = this.cache;
      var end = this.end.bind(this);
      /**
       * Plugins" length  which is waiting for load
       * @type {Number}
       */
      var length = _.isArray(plugins) ? plugins.length : 0;

      // If config didn"t require any plugin
      // trigger end event directly
      if (!length) return this.end();


      /**
       * Loaded Plugin length
       * @type {Number}
       */
      var count = 0;

      // Instantiate Plugin  and bind it to Reader.Plugins.
      // the key is file name OR directory name if the plugin is packaged.
      this.plugins.forEach(function (item, i) {
        requirejs(["pkg!" + item], function (Plugin) {
          cache[item] = new Plugin();

          count++;
          if (count == length) return end();
        });
      });
    },
    /**
     * Trigger "plugin:end.init" event
     */
    end: function () {

      this.emitAsync("plugin:end.init");

    }
  });

  return Plugins;
});
