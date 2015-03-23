define(function(require, exports, module) {

  var Base = require('base')
    , LabelModel = require('./model')
    , Slot = require('./slots')
    , Render = require('./renders/render');
    
  var view = Base.View.extend ({
    mixins: [Slot, Render],

    initialize: function($el, data) {
      this.model = new LabelModel ({
        type: data.type,
        bgColor: data.bgColor,
        size: data.size,
        family: data.family,
        color: data.color
      });
      
      this.render(data);

      this.$label = $el.find('.label');
      this.$content = $el.find('.content');
      this.$text = $el.find('.text');

      this.width = $el.width();
      this.height = $el.height();

      switch (this.model.get('type')) {
        case 'decals': this.setupDecals();
                       break;
        case 'paster': this.setupPaster();
                       break;
        case  'basic': this.setupBasic();
                       break;              
             default : this.setupDefault();
      };

      this.setupCommon();
      
    },

    events: {
      'click .label': 'handleClick'
    },

    setupBasic: function() {
       this.$label.addClass('type-basic');
    },

    setupDecals: function() {
      this.$label.addClass('type-decals');
    },

    setupPaster: function() {
      this.$label.addClass('type-paster');
      this.$label.css({'width':this.width-14, 'height':this.height-14});
      this.$content.css({'width': this.width-16, 'height':this.height-16});
      this.$label.css('background', this.model.get('bgColor'));
    },
    
    setupDefault: function() {
      this.$label.addClass('type-default');
      this.$content.css('background', this.model.get('bgColor'));
    },

    setupCommon: function() {
      this.$label.css({'color':this.model.get('color'), 'font-size':this.model.get('size'), 'font-family':this.model.get('family')});
      if (this.model.get('align')) {
        this.$label.css('text-align', this.model.get('align'));
      }
    },

    handleClick: function() {
      this.emit("click.label", this.itemId);
      // this.emit("click.label", '<strong>Change</strong> the <em>Text</em>.');
    }
  });
  return view ;
});