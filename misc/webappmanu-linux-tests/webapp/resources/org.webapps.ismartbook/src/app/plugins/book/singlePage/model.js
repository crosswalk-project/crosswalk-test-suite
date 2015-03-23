define(function(require,exports,module){
  var PluginBase = require('pkg!pluginBase');
  var config = PluginBase.config;

  // TODO  add size ;
  var SinglePageModel = PluginBase.Model.extend({
    defaults:{
      prevent:false,
      width:config.get('book-size')['1024']['width'],
      height:config.get('book-size')['1024']['height'],
      activePage:[0,1],
      pageCount:0,
    }
  });

  return SinglePageModel;
});