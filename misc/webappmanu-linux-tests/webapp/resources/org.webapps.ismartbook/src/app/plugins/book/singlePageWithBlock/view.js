define(function(require,exports,module){

  var PluginBase = require("pkg!pluginBase");
  var config = require("pkg!config");
  var pageTpl = require("tpl!./page");
  var Unit = require("../unit");
  

  var Model = require("./model");
  var cssUrl = require.toUrl("./bookblock.css");
  var jQuery = require("jquery");


  var SinglePageView = PluginBase.View.extend({
    id:"book",
    initialize:function(){
      this.$el.appendTo($("#book-stage")).addClass("bb-bookblock");
      this.model = new Model({});
      this.controller = config.get("controller");
    }
    , events:{
      "click":"clickAction",
      "start":"startAction",
      "end":"endAction",
      "mousemove .page-cover.disable":"disable",
      "mouseover .page-cover.disable":"disable",
      "mouseout .page-cover.disable":"disable",
      "click .page-cover.disable":"disable",
      "mouseup .page-cover.disable":"disable",
      "mousedown .page-cover.disable":"disable",
      "click .page-nav-button":"gotoPage",
      "click .left-bottom-button":"prev",
      "click .right-bottom-button,.right-top-button":"next"
    }
    , endInit:function(ebook){
     
      var ebook = this.ebook = config.get("ebook");
      // TODO opf  parse
      this.model.set({
        pageCount : ebook.pageCount(),
        title     : ebook.get("ncx").title,
        controller: config.get("controller"),
        fullpath  : ebook.get("fullPath")+"/OEBPS/",
        ncx   : ebook.get("ncx")
      });
      
      this.addBlankPages();
      // set title
      this.setTitle();
      
      this.bb = this.$el.bookblock({
        onEndFlip:this.turnedAction.bind(this),
        onBeforeFlip:this.turningAction.bind(this),
        speed:100000,
        item:".page",
        easing:'ease',
        shadows:0
      });
      this.addPage(1,function(){
        this.turnedAction(0,0);
        this.emitAsync("page:end.preload",ebook);
      }.bind(this));

    }
    , unlockPage:function(data){
      if (this.controller) 
        return ;
      this.$el.find(".p"+data.page).find(".page-cover").removeClass("disable");
    }
    , lockPage:function(page){
       $(".page-cover").addClass("disable");
    }
    , disable:function(e){
        e.stopPropagation();
        e.preventDefault();
    }
    , setTitle:function(){
      var title =  this.model.get("title");
      document.title = title;
    }
    , next:function(){
      this.bb.next();
    }
    , prev:function(){
      this.bb.prev();
    }
    , toPage:function(page){

      switch(page){
        case "next":
          this.bb.next();
          break;
        case "prev":
          this.bb.prev();
          break;
        default:
          page = parseInt(page);
          this.bb.jump(page);
          break;
      }
  
    }
    , startAction:function(){
      IS_START = 1;
    }
    , turnedAction:function(old,page,isLimit){
      
      IS_START = 0;
      var min = page - 2,
          max = min + 5,
          $pageContent,
          pageCount = this.model.get("pageCount"),
          activePage = this.model.get("activePage"),
          m1, m2;

      if (min < 1) min = 1;
      if (max > pageCount) max = pageCount;

      for(var p = min; p <= max; p++) {
        if (p >= activePage[0] && p <= activePage[1]) {
          this.emit("unit:stop",p);
        } else {
       
          this.addPage(p);
        }
      }

      for(var p = Math.max(activePage[0], 1); p <= activePage[1]; p++) {
        if (p >= min && p <= max) {
          this.emit("unit:stop",p);
        } else {
          
          this.emit("unit:clear.cache",p);
          this.emit("anno:clear.cache",p);
          $(".p" + p + " .page-content").empty();
        }
      }

      this.model.set("activePage",[min,max]);
      if (!this.controller) {
        this.lockPage();
      }

      this.emitAsync("book:turned",page+1);
      
    }
    , addPage:function(p,callback){
      var ebook = config.get("ebook");
     
      ebook.loadByPage(p, function(err, result) {
          if (err) return  console.log(err);
          
          var $pageContent = this.$el.find(".p" + p + " .page-content");
          
          
          var content = result.content.replace(/{{bookFullPath}}/g,this.fullpath);
          $pageContent.html(content);
          this.setPageCache(p,$pageContent);
          callback && callback(p);
        }.bind(this));
    }
    , setPageCache:function(p,$pageContent){
      this.emit("unit:add",p,new Unit($pageContent,p));

    }
    , endAction:function(){
      IS_START = 0;
    }
    , addBlankPages:function(){
      var pageCount = this.model.get("pageCount");
      var points = this.model.get("ncx").points;
      var orders = this.model.get("ncx").orders;
      var modules = this.model.get("ncx").modules;
      var temp = {};
      var html = "";
      var page = {};
      this.pages = [];
      for(var i = 0; i < pageCount; i++){
        temp = {};
        temp.last = 0;
        temp.num = i+1; 
        temp.st = !this.controller;
        page = points[orders[i]];
        temp.module = page.module;
        temp.unit = page.unit;
        temp.id = page.id;
        temp.pages = modules[page.module][page.unit].pages;
        console.log(temp);
        html += pageTpl(temp);
      }
      this.$el.append(html);

    }
    , clickAction:function (e){
      var $src = $(e.srcElement);
      
      if (this.model.get("prevent")) return false;

      if (!$src.hasClass("page") 
          && $src.attr("id") !== "book" 
          && !$src.parents(".page").length  ) return false;
    }
    , turningAction:function (e, page){
      
      this.emit("sync:send","turn",page);
      this.model.set("prevent",true);
      setTimeout(function(){
          this.model.set("prevent",false);
        }.bind(this)
      ,1000);
    }
    , gotoPage:function(evt){
      var $target = $(evt.target);
      if ($target.hasClass("current")) return ;
      var pageId = $target.data("page");
      var page = config.get("ebook").get("id2page")[pageId];
      if (page) {
        this.emit("book:turn",page);
      };

    }
    , modeChange:function(mode){
      if (mode !== "READ" ) 
         return this.model.set("disabled",true);
      this.model.set("disabled",false);
    }
  });
  return SinglePageView ;
});