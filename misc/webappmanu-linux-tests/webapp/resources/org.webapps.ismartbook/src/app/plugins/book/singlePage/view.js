define(function(require,exports,module){

  var PluginBase = require('pkg!pluginBase');
  var config = require('pkg!config');
  var Tpl = require('text!./page.tpl');
  var Unit = require('../unit');
  var Handlebars = require('handlebars');
  var pageTpl = Handlebars.compile(Tpl);
  var Model = require('./model');
  var jQuery = require('jquery');
  require('./turn');


  var SinglePageView = PluginBase.View.extend({
    id:'book',
    initialize:function(){
      this.$el.appendTo($('#book-stage'));
      this.model = new Model({});
    }
    , events:{
      'click':'clickAction',
      'turning':'turningAction',
      'start':'startAction',
      'end':'endAction',
      'turned':'turnedAction',
      'mousemove .page-cover.disable':'disable',
      'mouseover .page-cover.disable':'disable',
      'mouseout .page-cover.disable':'disable',
      'click .page-cover.disable':'disable',
      'mouseup .page-cover.disable':'disable',
      'mousedown .page-cover.disable':'disable',
    }
    , endInit:function(ebook){
     
      var ebook = this.ebook = config.get('ebook');
      console.log(ebook.get('ncx').title);
      // TODO opf  parse
      this.model.set({
        pageCount : ebook.pageCount(),
        title     : ebook.get('ncx').title,
        controller: config.get('controller'),
        fullpath  : ebook.get('fullpath')+'/OEBPS/'
      });

      this.addBlankPages();
      // set title
      this.setTitle();
      
      this.$el.turn({acceleration: true,})
              .turn('size',this.model.get('width'),this.model.get('height'))
              .turn('page',1);
      this.addPage(1);

      this.trigger('book:end.init',ebook);
    }
    , unlockPage:function(data){
      if (this.controller) 
        return ;
      this.$el.find('.p'+data.page).find('.page-cover').removeClass('disable');

    }
    , lockPage:function(page){
       $('.page-cover').addClass('disable');
    }
    , disable:function(e){
        e.stopPropagation();
        e.preventDefault();
    }
    , setTitle:function(){
      var title =  this.model.get('title');
      document.title = title;
    }
    , toPage:function(page){
      switch(page){
        case 'next':
          this.$el.turn('next');
          break;
        case 'prev':
          this.$el.turn('previous');
          break;
        default:
          page = parseInt(page);
          this.$el.turn('page',page);
          break;
      }

    }
    , startAction:function(){
      IS_START = 1;
    }
    , turnedAction:function(e,page){
      
      IS_START = 0;
      var min = page - 2,
          max = min + 5,
          $pageContent,
          pageCount = this.model.get('pageCount'),
          activePage = this.model.get('activePage'),
          m1, m2;

      if (min < 1) min = 1;
      if (max > pageCount) max = pageCount;

      for(var p = min; p <= max; p++) {
        if (p >= activePage[0] && p <= activePage[1]) {
          this.trigger('unit:stop',p);
        } else {
          
          this.addPage(p);
        }
      }

      for(var p = Math.max(activePage[0], 1); p <= activePage[1]; p++) {
        if (p >= min && p <= max) {
          this.trigger('unit:stop',p);
        } else {
          
          this.trigger('unit:clear.cache',p);
          this.trigger('anno:clear.cache',p);
          $('.p' + p + ' > .page-content').empty();
        }
      }
      if (this.controller) {
        this.trigger('page:turned',page);
      };
      
      this.model.set('activePage',[min,max]);
      if (!this.controller) {
        this.lockPage();
      }
    }
    , addPage:function(p){
      var ebook = config.get('ebook');

      ebook.loadByPage(p, function(err, result) {
          if (err) return  console.log(err);
          
          var $pageContent = this.$el.find('.p' + p + ' > .page-content');
          
          
          var content = result.content.replace(/{{bookFullPath}}/g,this.fullpath);
          $pageContent.html(content);
          this.setPageCache(p,$pageContent);
          this.setHighlight(p,$pageContent);
        }.bind(this));
    }
    , setPageCache:function(p,$pageContent){
      this.trigger('unit:add',p,new Unit($pageContent,p));

    }
    , setHighlight:function(p,$pageContent){
      this.trigger('anno:add',p,$pageContent);
    }
    , endAction:function(){
      IS_START = 0;
    }
    , addBlankPages:function(){
      var pageCount = this.model.get('pageCount');
      var temp = {};
      var html = '';
      this.pages = [];
      for(var i = 0; i < pageCount; i++){
        temp = {};
        temp.last = 0;
        temp.num = i+1;    
        temp.st = !this.controller;
        html += pageTpl(temp);
      }
      this.$el.append(html);

    }
    , clickAction:function (e){
      var $src = $(e.target);
      
      if (this.model.get('prevent')) return false;

      if (!$src.hasClass('page') 
          && $src.attr('id') !== 'book' 
          && !$src.parents('.page').length  ) return false;
    }
    , turningAction:function (e, page){
      var self = this;
      this.trigger('sync:send','turn',page);
      
      this.model.set('prevent',true);

      setTimeout(function(){self.model.set('prevent',false)},1000);
    }
    , modeChange:function(mode){
      if (mode !== 'READ' ) 
        this.model.set('disabled',true);
      this.model.set('disabled',false);
    }
  });
  return SinglePageView ;
});