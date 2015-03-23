define(function(require,exports,module){
  "use strict";

  var Base, config, BookModel;
  /**
   * Base Object of plugin.
   * @type {Object}
   */
  Base = require("pkg!pluginBase");
  /**
   * Config of system
   * @type {Object}
   */
  config = Base.config;
  /**
   * BookModel
   * @type {Function}
   */
  BookModel = Base.Model.extend({
    defaults:{
      prevent:false,
      width:config.get("book-size")["1024"].width,
      height:config.get("book-size")["1024"].height,
      activePage:[0],
      pageCount:0,
      currentPage:0,
      rangeLength:5
    }
  });

  return BookModel;
});