define(function(require, exports, module) {

  
  var template = require('tpl!./label');

  return {
    template: template,
    css: './renders/label.css',

    render: function(data) {
      this.addClass(this.css);
      this.$el.html(this.template(data));
    }
  };
});