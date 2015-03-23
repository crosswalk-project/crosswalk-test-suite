define(function(require, exports, module) {
  var Base = require('base');
  var LabelModel = Base.Model.extend ({
    defaults: {
      type: 'default',
      size: 16,
      family: 'Arial',
      color: 'black'
    }
  });
  return LabelModel;
});