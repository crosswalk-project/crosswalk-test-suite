define(function(require,exports,module){
  var io  =require("./socket.io");
  var Base = require("pkg!pluginBase");
  var server  = Base.config.get("socket");
  var Model  = Base.Model.extend({
    initialize:function(){
      if (!Base.config.get("opsync")) return ;

      this.socket = io.connect(server);

      this.socket.on("cmd",function(command){
        if (command.type == "goto") {
          console.log(command);
          Base.observer.trigger("book:turn",command.page);
        };
      })
    },

  })
  return Model;
});