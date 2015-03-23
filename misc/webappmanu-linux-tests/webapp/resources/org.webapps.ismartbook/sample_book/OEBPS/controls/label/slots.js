define(function(require, exports, module) {
  var slots = {
    setText: function(text) {
      this.clearText();
      this.$text.find('li').html(text);
    },
    
    clearText: function() {
      this.$text.find('li').html('');
    }
  };
  return slots;
});