/**
 * EBook Parser
 *
 * @author William <weix.ge@intel.com>
 */
(function(GLOBAL, undefined) {

  /** global mixin function **/

  function mixin(target, source) {
    if (typeof target !== 'object')
      target = {};
    for (var i in source) {
      if (source.hasOwnProperty(i)) target[i] = source[i];
    }
    return target;
  }
  var xml_special_to_escaped_one_map = {
    '&': '&amp;',
    '"': '&quot;',
    '<': '&lt;',
    '>': '&gt;'
  };

  var escaped_one_to_xml_special_map = {
    '&amp;': '&',
    '&quot;': '"',
    '&lt;': '<',
    '&gt;': '>'
  };

  var encodeXml = function (string) {
    return string.replace(/([\&"<>])/g, function(str, item) {
      return xml_special_to_escaped_one_map[item];
    });
  };

  var decodeXml = function (string) {
    return string.replace(/(&quot;|&lt;|&gt;|&amp;)/g,
      function(str, item) {
        return escaped_one_to_xml_special_map[item];
      });
  }
  var Storage = {},
    isObject = function(obj) {
      return obj === Object(obj);
    },
    isString = function(obj) {
      return Object.prototype.toString.call(obj) == '[object String]';
    },
    isArray = function(obj) {
      return Array.isArray(obj);
    },

    // check env 
    isApp = window.chrome && chrome.storage && chrome.storage.local ? 1 : 0,

    // default local is a javascript Object.
    local = {
      _data: {},
      getItem: function(item) {
        return this._data[item] || null;
      },
      setItem: function(item, value) {
        this._data[item] = value;
        return value;
      },
      removeItem: function(item) {
        delete this._data[item];
        return null;
      },
      clear: function() {
        this._data = {};
        return null;
      }
    };
  if (!isApp) {
    // set local as localStorage or sessionStorage if localStorage can be used.
    try {
      localStorage.getItem("test");
      local = localStorage;
    } catch (e) {

    }
  };


  var isSync = 0,
    // port w3c api to chrome storage api.
    w3cLocal = {

      get: function(arr, callback) {
        var ret = {};

        if (isString(arr)) {
          arr = [arr];
        }

        if (!isArray(arr) && isObject(arr)) {
          arr = Object.keys(arr);
        }

        arr.forEach(function(item) {

          ret[item] = local.getItem(item);
          if (ret[item]) {
            ret[item] = JSON.parse(ret[item]);
          }
        });

        if (callback) return callback(ret);
      },

      set: function(obj, callback) {
        var keys = Object.keys(obj);

        keys.forEach(function(item) {
          local.setItem(item, JSON.stringify(obj[item]));
        });
        if (callback) return callback();
      },

      clear: function(callback) {
        local.clear();
        if (callback) return callback();
      },

      remove: function(arr, callback) {

        if (isString(arr)) {
          arr = [arr];
        }

        arr.forEach(function(item) {
          local.removeItem(item);
        });

        if (callback) return callback();
      }
    };

  Storage.local = isApp ? chrome.storage.local : w3cLocal;
  var fileProtocols = ["file", "filesystem", "http", "https", "chrome-extension"];

  /**
   * Ebook Parser main function
   * @param {String} path    bookPath
   * @param {Object} options
   *                  * [Bool] useCache
   *                      *
   */

  function Ebook(path, options) {
    // Set Attrs
    this._attrs = {};
    this._loaded = {};
    var opt = this.options = {};

    if (typeof options === 'object') mixin(opt, options);
    // clear cache
    if (!opt.useCache) this.clearCache();

    // TODO deep copy prototype attrs
    mixin(this._attrs, this.__proto__._attrs);


    // Set Path and FullPath
    this.set('bookPath', path);
    this.setFullPath();

    this.extendWithType();
  }

  /**
   * Register functions to Ebook prototype ;
   * @param  {String} type    mimetype, like 'application/epub+zip'
   * @param  {Object} options callback Functions and default attrs
   */
  Ebook.register = function(type, options) {
    var parsers = this.prototype._parsers;

    if (!parsers[type]) parsers[type] = {};

    mixin(parsers[type], options);
  }

  /**
   * Base functions and default attributes
   */
  mixin(Ebook.prototype, {
    mixin: function(options) {
      mixin(this, options);
    },
    initialize: function() {},
    _parsers: {},
    _attrs: {},
    get: function(attrName) {
      return this._attrs[attrName];
    },
    set: function(attrName, value) {
      this._attrs[attrName] = value;
      this.trigger('change:' + attrName, value);
    },
    encodeXml:encodeXml
  })

  /**
   * Simple Event System
   */
  mixin(Ebook.prototype, {
    trigger: function(events, value) {

      if (!(this._events && this._events.length)) {
        return this;
      }
      events = events.split(this.splitter);
      var args = Array.prototype.slice.call(arguments, 1),
        list,
        self = this;

      while (event = events.shift()) {
        list = this._events[event];

        if (!list) {
          continue;
        }


        list.forEach(function(item) {
          //console.log(event,self,item.context);
          item.callback.apply(item.context || self, args);
        });
      }
    },
    splitter: /\s+/,
    on: function(events, func, context) {
      if (!func) return this;
      events = events.split(this.splitter);
      if (!events.length) return this;
      if (!this._events) {
        this._events = {};
        this._events.length = 0;
      };
      var list = this._events;
      while (event = events.shift()) {
        if (!list[event]) {
          list[event] = [];
          this._events.length++;
        }
        var node = {};
        node.context = context;
        node.callback = func;
        list[event].push(node);
      }


    },
    off: function(event, func, context) {
      var list, tmp;
      if (!(events || func || context)) {
        this._events = {};
        this._events.length = 0;
        return this;
      }
      events = events.split(this.splitter);
      while (event = events.shift()) {
        list = this._events[event];
        tmp = [];
        if (!list.length) {
          continue;
        };
        list.forEach(function(item) {
          if ((func && item.callback !== func) ||
            (context && item.context !== context)) {
            temp.push(item);
          }
        });
        if (temp.length) {
          this._events[event] = temp;
        } else {
          delete this._events[event];
          this._events.length--;
        }

      }
    }
  });

  mixin(Ebook.prototype, {
    /**
     * Set FullPath like "http://localhost/bookpath/"
     * @param {String} path user custom path
     */
    setFullPath: function(path) {
      // set as user wish
      if (path) {
        this.fullPath = path;
        return;
      }
      var bookPath = this.get("bookPath");
      var isUrl = fileProtocols.indexOf(bookPath.split(":")[0]) > -1;

      if (isUrl) {
        this.set("fullPath", bookPath);
        return;
      }

      // if user dosen't give path url, get from location
      var paths = (window.location.origin + window.location.pathname).split('/'),
        last = paths.pop()
        // last is "" or last is `html` file
        ,
        keepLast = !last || /\.html/.test(last);

      if (!keepLast) paths.push(last);

      paths.push(this.get('bookPath'));
      this.set('fullPath', paths.join('/'));
    }
  });

  /**
   * Read content from file
   * @param  {String} filePath    file path
   * @param  {Function} success success callback
   * @param  {Function} error  error callback
   */
  Ebook.prototype._read = function(filePath, success, error) {

    var xhr = new XMLHttpRequest(),
      self = this,
      url = this.get('bookPath') + '/' + filePath,
      localData, type = this.getTypeWithPath(filePath);

    this.getCache(url, function(localData) {
      // if local has cache, get data from local 
      if (localData[url]) {
        success && success(localData[url]);
        return;
      }

      // if no local cache , get from remote 
      xhr.open('GET', url, true);
      xhr.send(null);

      xhr.onload = function() {
        self.setCache(url, xhr.responseText);
        // some browsers didn't has responseXML,
        // so this function didn't return responseXML.    
        success && success(xhr.responseText);
      };
      xhr.onerror = function(err) {
        error && error(err);
      }
    })

  }
  Ebook.prototype.getTypeWithPath = function(filePath) {
    var file = filePath.split('/').pop(),
      exts = file.split('.');
    if (exts.length == '1') {
      return 'txt';
    }
    return exts.pop().toLowerCase();
  }
  /**
   * get File Content
   * @param {String} path filePath Which file it wants to parse.
   * @param {Object} option
   *                  * {Function} success
   *                  * {Function} error
   *                  * {String} loadMessage
   */
  Ebook.prototype.read = function(path, option) {
    var self = this,
      callback = function(data, type) {
        var cb;
        // if didn't set error function , default set console the error
        if (!option[type] && type == 'error') {
          console.log(data);
          return;
        }
        // if option is object , find the option[type]
        if (option[type]) cb = option[type];

        // if option is callback function , set it as callback
        if (typeof option === 'function') cb = option;

        cb && cb.call(self, data);
      }, success = function(data) {
        callback(data, 'success');
      }, error = function(err) {
        callback(err, 'error');
      };

    this._read(path, success, error);
  }



  /**
   * Extend and parser function
   */
  mixin(Ebook.prototype, {
    extendWithType: function() {
      var self = this,
        success = function(type) {
          self.set('mimetype', type);
          var obj = self._parsers[type];

          if (!obj) {
            throw (new Error("Doesn't support this type: " + type));
            return;
          }
          this.bindParser(obj);
          this.initialize();
        }
      this.read('mimetype', success);
    },
    bindParser: function(obj) {
      var self = this;
      if (obj._processList && obj._processList.length) {
        self._completed = {};
        obj._processList.forEach(function(item) {
          self.on('complete:' + item, self.onProcess, self);
          self._completed[item] = 0;
        });
        delete obj._processList;
      }

      if (obj.events) {
        for (var i in obj.events) {

          if (obj.events.hasOwnProperty(i)) {
            var func = obj.events[i];
            self.on(i, obj[func], self);
          }
        }
        delete obj.events;
      }

      this.mixin(obj);
    },
    onProcess: function(name) {

      var callback = this.options.process;
      if (!callback || typeof callback !== 'function') {
        callback = false;
      }

      if (this._completed.hasOwnProperty(name)) {
        this._completed[name] = 1;
        callback && callback(name);
        this.checkComplete();
      }
    },
    complete: function(name) {
      this.trigger('complete:' + name, name);
    },
    checkComplete: function() {
      var list = this._completed;
      var done = 1;
      var callback = this.options.complete;

      if (!callback || typeof callback !== 'function') {
        callback = false;
      }

      for (var i in list) {
        if (list.hasOwnProperty(i) && list[i] !== 1) {
          done = 0;
        }
      }

      if (done && callback) callback(this);
    }
  });



  /**
   * Mixin Cache functions to Ebook
   */
  mixin(Ebook.prototype, {
    setCache: function(key, value, callback) {
      var obj = {};
      obj[key] = value;
      Storage.local.set(obj, callback);
    },
    getCache: function(key, callback) {
      return Storage.local.get(key, callback);
    },
    clearCache: function() {

      Storage.local.clear();
    }
  });


  GLOBAL.Ebook = Ebook;
}(window));


;
(function(GLOBAL) {

  if (!GLOBAL.Ebook) return;

  Ebook.register('application/etb+zip', {
    initialize: function() {
      this.read('META-INF/container.xml', this.parseContainer.bind(this));
    },
    events: {
      'change:opf': 'parseOpf'
    },
    _processList: ['ncx', 'manifest', 'spine'],
    parseContainer: function(data) {
      data = this.parseXML(data);
      var root = data.querySelectorAll('rootfile'),
        opf = root[0].attributes['full-path'].value

        this.set('opfRoot', opf.substring(0, opf.lastIndexOf('/')));
      this.set('opf', opf);
    },
    parseXML: function(data) {
      var parser = new DOMParser();
      return parser.parseFromString(data, 'text/xml');
    },
    parseOpf: function(opf) {
      var success = function(data) {

        data = this.parseXML(data);
        this.parseManifest(data);
        this.parseSpine(data);
        this.parseNCX();
      }
      this.read(opf, success.bind(this));
    },
    resolvePath: function(id, abs) {
      var item = this.get('manifest')[id];

      return !item ? false :
        (abs ? this.get('fullPath') + '/' : '') + this.get('opfRoot') + '/' + item.href;
    },
    parseManifest: function(opfXML) {

      var items = opfXML.querySelectorAll('manifest > item'),
        manifest = {}, url2id = {}, parseItem = function(item) {
          manifest[item.getAttribute('id')] = {
            'href': item.getAttribute('href'),
            'type': item.getAttribute('media-type')
          };

          url2id[item.getAttribute('href')] = item.getAttribute('id');
        }

      Array.prototype.forEach
        .call(items, parseItem);

      this.set("manifest", manifest);
      this.set("url2id", url2id);

      this.complete('manifest');
    },
    parseSpine: function(opfXML) {

      var spineEl = opfXML.querySelector('spine'),
        itemsEl = spineEl.querySelectorAll('itemref'),
        spine = [],
        id2page = {}, parseItem = function(item) {
          var id = item.getAttribute('idref');
          id2page[id] = spine.length + 1;
          spine.push(id);
        }, toc = spineEl.getAttribute('toc');


      Array.prototype.forEach
        .call(itemsEl, parseItem);
      this.set('id2page', id2page);
      this.set('pageCount', spine.length);
      this.set('spine', spine);
      this.set('toc', toc);
      this.complete('spine');
    },
    parseNCX: function() {
      var id = this.get('toc'),
        tocPath = this.resolvePath(id),
        points = {}, orders = [],
        modules = {}, previews = {}, assistants = {}, ncx = {
          points: points,
          orders: orders,
          previews: previews,
          modules: modules,
          assistants: assistants
        }, self = this;

      if (!tocPath) return;

      var success = function(content) {
        var parser = new DOMParser();
        content = parser.parseFromString(content, 'text/xml');
        var navMap = content.querySelector('navMap'),
          titleNode = content.querySelector('docTitle');

        ncx.title = titleNode ?
          titleNode.querySelector('text').textContent : '';

        navPointParser(navMap, points);
        var temp = [];
        orders.forEach(function(item, i) {
          temp.push(item);
        });
        ncx.orders = temp;
        self.set('ncx', ncx);
        this.complete('ncx');
      }
      // navPoin
      var navPointParser = function(node, points) {
        var navPointNodes = node.childNodes;

        for (var i = 0; i < navPointNodes.length; i++) {
          var n = navPointNodes[i];
          if (n.nodeType == 3) continue;

          if (n.nodeName == 'navPoint') {
            var childNodes = n.childNodes,
              p = {
                id: n.getAttribute('id'),
                order: parseInt(n.getAttribute('playOrder')),
                module: parseInt(n.getAttribute('module')),
                unit: parseInt(n.getAttribute('unit')),
                label: null,
                content: null,
                page: 0,
                children: {}
              };
            for (var j = 0; j < childNodes.length; j++) {
              var cn = childNodes[j];
              if (cn.nodeType == 3) continue;

              switch (cn.nodeName.toLowerCase()) {
                case 'navlabel':
                  p.label = self.encodeXml(cn.getElementsByTagName('text')[0].textContent);
                  break;
                case 'content':
                  p.content = cn.getAttribute('src');
                  break;
                case 'preview':
                  p.preview = cn.getAttribute('src');
                  previews[p.id] = p.preview;
                  break;
                case 'signals':
                  p.signals = cn.getAttribute('src');
                  break;
                case 'assistant':
                  p.assistant = cn.getAttribute('src');
                  assistants[p.id] = p.assistant;
                  break;
                case 'controls':
                  p.controls = cn.getAttribute('src');
                  break;
              }
            }
            navPointParser(n, p.children);
            points[p.id] = p;
            if (!modules[p.module]) {
              modules[p.module] = {};
            }
            if (!modules[p.module][p.unit]) {
              modules[p.module][p.unit] = {
                pages: [],
                maxPage: 0
              };
            };
            modules[p.module][p.unit].pages.push(p);
            modules[p.module][p.unit].maxPage++;
            p.page = modules[p.module][p.unit].maxPage;
            orders[p.order] = p.id;
          }
        }
      }
      console.log(tocPath);
      this.read(tocPath, success);

    },
    loadByURL: function(url, cb) {
      var self = this,
        id = this.get('url2id')[url];

      if (!id) {
        cb(new Error('URL ' + url + ' does not exist!'));
        return;
      }

      this._loadById(id, function(err, r) {
        if (err) {
          cb && cb(err);
          return;
        }
        r.page = self.get('id2page')[id];
        r.url = url;
        cb(false, r);
      });
    },
    pageCount: function() {
      return this.get('spine').length;
    },
    loadByPage: function(p, cb) {
      if (p > this.get('spine').length || p <= 0) {
        cb(new Error('Page ' + p + ' is out of range!'));
        return;
      }

      var self = this,
        id = self.get('spine')[p - 1];

      this._loadById(id, function(err, r) {
        if (err) {
          cb(err);
          return;
        }

        r.page = p;
        r.url = self.get('manifest')[id].href;

        cb(false, r);
      });
    },
    url2page: function(url) {
      var id = this.get('url2id')[url];
      return id ? this.get('id2page')[id] : 0;
    },
    _loadById: function(id, cb) {

      this._read(this.resolvePath(id, false), function(result) {
        cb(false, {
          content: result,
          id: id
        });
      }, function(err) {
        cb(err);
      });
    }

  });

}(window));