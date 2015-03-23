define(function (require, exports, module) {
  var Base = require("pkg!pluginBase");
  var Mode = Base.Model.extend({
    defaults: {
      mode: []
    },
    obEvents: {
      "system:enter.mode": "enter",
      "system:exit.mode": "exit"
    },
    enter: function (mode, baseMode) {
      var modes = this.get("mode"),
        oldMode = modes[modes.length - 1],
        newMode = mode;
        

      // system can't enter a mode twice
      if (oldMode == newMode) return;

      var checkBaseMode = function (baseMode, callback) {
        if (!baseMode) return callback && callback();

        var lastMode = modes[modes.length - 1];

        if (lastMode != baseMode) {
          this.exit(lastMode);
          return checkBaseMode(baseMode, callback);
        }
        if (callback) return callback();
      }.bind(this);

      checkBaseMode(baseMode, function () {
        modes.push(mode);
        console.log(modes);
        this.emitAsync("system:change.mode", oldMode, newMode, 1);
      }.bind(this));

    },
    exit: function (mode) {
      var modes = this.get("mode"),
        oldMode = modes[modes.length - 1],
        newMode;

      // if current mode is't equal mode, system do nothing.
      if (oldMode != mode) return;


      modes.pop();
      newMode = modes[modes.length - 1];

      this.emit("system:change.mode", oldMode, newMode, 0);
    },
    is: function (mode) {
      var modes = this.get("mode");
      return modes[modes.length - 1] === mode;
    },

    mode: function () {
      var modes = this.get("mode");
      return modes[modes.length - 1];
    }
  });
  return new Mode();
});
