define(function (require, exports, module) {

  // modules
  var observer = require("pkg!observer");
  var url = require("./lib/url");
  var $ = require("jquery");

  // 在所有控件初始化之后，注册 系统的preload 事件
  observer.on("plugin:end.init", function () {
    observer.trigger("system:register.end", "preload", "controls:end.cache");
  });

  // 书本的路径
  // @example http://localhost/book/OEBPS
  var fullPath;

  // 当前requirejs的全路径
  // @example http://localhost/reader/src/app
  var baseUrl = url.realpath(require.toUrl(""));
  // baseUrl 到 fullPath 的相对路径
  // @example ../../book/OEBPS
  var relativePath;

  // contorls 的缓存
  var ControlsCache = {};

  // controls.json 的缓存

  var ControlsName = [];

  // 每页controls-data.json的缓存
  var ControlsDataCache = {};

  var endEvents = [];

  // 在Book:start.init的时候执行回调函数
  // 这个是整个Reader渲染的第三个阶段，在这之前已经由etb.js将书本的内容都解析出来了
  // 这个阶段获取的是Reader自定义的一些东西，以及
  var cache = function (ebook) {

    // 设置当前环境里面的全局变量fullPath为书本的路径
    // @example http://localhost/book/OEBPS/
   
    fullPath = ebook.get("fullPath") + "/OEBPS/";

    fullPath = url.realpath(fullPath) + "/";
  

    // 设置相对路径
    relativePath = url.relative(baseUrl, fullPath);
   
    var style = ebook.get("manifest").style;

    // 如果书本有id为style的css文件,则增加这个文件到当前文档里面。
    // 这个css可以放一些书本通用的样式。
    if (style) {
      $("head").append("<link href='" + fullPath + " / " + style + "' rel='stylesheet '>");
    }

    loadView(ebook);
    loadData(ebook);
  };

  function loadView(ebook) {
    var path = ebook.resolvePath("controls");

    ebook.read(path, function (data) {

      // check data type and data length
      if (!_.isString(data)) return;
      var tmpName = JSON.parse(data);
      ControlsName = _.union(tmpName);
      
      if (ControlsName.length !== tmpName.length) {
        console.warn("control name isn't unique, please check it in controls.json");
      }
      if (!_.isArray(ControlsName) || !ControlsName.length) {
        return end(1);
      }

      _.each(ControlsName, preloadView);
    });
  }

  function end(item) {
    if (item === 1) return observer.trigger("controls:end.cache");

    endEvents.push(item);
    if (endEvents.length == 2) observer.trigger("controls:end.cache");

  }

  function preloadView(name) {
    var url = [];

    // 获取到对应路径下面的main.js 
    url.push("controlsPath/" + name + "/main");

    // 在requirejs里面，任何以`.js`结尾 / `/`开头 / 包含`http`,`https`
    // 都会被认为是在请求一个已经定义好的module，
    // 而这个时候请求的module里面如果再使用了`require("./subfile")`这样的内容
    // 则不会正确的增加`.js`的结尾，这将导致在非apache环境下请求文件失败。
    // 
    // 增加设置paths.controlsPath，将相对路径写上去，然后在url里面使用controlsPath来
    // 代替原来的http开头的路径，这样可以解决上面请求文件的扩展不正确的问题。
   
    requirejs({

      paths: {
        "controlsPath": fullPath + "controls"
      }
    }, url, function (view) {
      // cache view to local
      view.prototype.controlName = name;
      ControlsCache[name] = view;

      // 当所有控件都已经加载完成了，通知系统`controls:end.cache`
      if (_.size(ControlsCache) == _.size(ControlsName)) {
        end("controls:end.cahce.controls");
      }
    });
  }

  function loadData(ebook) {
    var ncx = ebook.get("ncx").points;
    var files = 0;
    var check = function () {
      if (files == _.size(ControlsDataCache)) {
        end("controls:end.cahce.data");
      }
    };
    var temp = [];
    // find all links of config files; 
    _.each(ncx, function (item) {
      var obj = {};

      if (item.controls) {
        obj.url = item.content;
        obj.controls = item.controls;
        files++;
        temp.push(obj);
      }

    });

    if (files === 0) {
      end("controls:end.cahce.data");
      return;
    }

    // load controls data
    _.each(temp, function (item) {

      var page = ebook.url2page(item.url);
      ebook.loadByURL(item.controls, function (err, result) {

        if (err) return;

        ControlsDataCache[page] = JSON.parse(result.content);
        return check();
      });
    });
  }


  /**
   * 单个控件渲染函数
   * 1. 找到页面里面有data-control的dom
   * 2. 如果有的话，找到这个data-control的设置作为控件的名称查找相关控件
   * 3. 将控件实例化并保存到页面的controls里面
   * @param  {jQuery Object} $content HTML片段
   * @param  {Number} page    当期所处理的是第几页
   * @param  {Array} controls   当前处理的页面的controls对象
   */
  var PageRender = function ($content, page, controls, pageOb) {
    var $controls = $content.find("[data-control]");
    var dataCache = ControlsDataCache[page];

    if (!$controls.length) return;

    $controls.each(function renderControl(i, item) {
      var name, itemId, data = {}, system;

      // get control information
      // @example <div data-control="control-name" data-id="itemId"></div>
      name = item.dataset.control;
      itemId = item.dataset.id;

      // check control is cached or not.
      if (!ControlsCache[name]) {
        console.error("Didn't cache this control : " + name);
        return;
      }


      if (dataCache && dataCache[itemId] && _.isObject(dataCache[itemId])) {
        // we use object just for data, and there is no function in object.
        // So in this case, JSON parse/stringify is faster than jQuery.extend.
        // @testcase http://jsperf.com/object-deep-clone
        data = JSON.parse(JSON.stringify(dataCache[itemId]));
      }
      if (dataCache && dataCache.system && _.isObject(dataCache.system)) {
        data.system = JSON.parse(JSON.stringify(dataCache.system));
      }

      // Add more information for Base.View.constructor
      data.itemId = itemId;
      data.fullPath = fullPath;
      controls.push(new ControlsCache[name]($(item), data, page, pageOb));
    });
  };

  return {
    render: PageRender,
    cache: cache,
    ControlsCache: ControlsCache
  };
});
