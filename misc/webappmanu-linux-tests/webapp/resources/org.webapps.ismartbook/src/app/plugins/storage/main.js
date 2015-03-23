/**
 * Storage plugin
 * Change the usage of localStorage from w3c to chrome.storage.local
 * 
 * @reference http://developer.chrome.com/apps/storage.html
 * @author iwege<weix.ge@intel.com>
 * @version 0.1.0
 * 
 */
define(function (require, exports, module) {
  var fs = require("./filesystem");
  var observer=  require("pkg!observer");
  var Storage = {},
  isObject = function (obj) {
    return obj === Object(obj);
  },
  isString = function (obj) {
    return Object.prototype.toString.call(obj) == '[object String]';
  },
  isArray = function (obj) {
    return Array.isArray(obj);
  },

  // check env 
  isApp = window.chrome && chrome.storage && chrome.storage.local ? 1 : 0,

    // default local is a javascript Object.
    local = {
      _data: {},
      getItem: function (item) {
        return this._data[item] || null;
      },
      setItem: function (item, value) {
        this._data[item] = value;
        return value;
      },
      removeItem: function (item) {
        delete this._data[item];
        return null;
      },
      clear: function () {
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

      get: function (arr, callback) {
        var ret = {};

        if (isString(arr)) {
          arr = [arr];
        }

        if (!isArray(arr) && isObject(arr)) {
          arr = Object.keys(arr);
        }

        arr.forEach(function (item) {

          ret[item] = local.getItem(item);
        });

        if (callback) return callback(ret);
      },

      set: function (obj, callback) {
        var keys = Object.keys(obj);

        keys.forEach(function (item) {
          local.setItem(item, JSON.stringify(obj[item]));
        });
        if (callback) return callback();
      },

      clear: function (callback) {
        local.clear();
        if (callback) return callback();
      },

      remove: function (arr, callback) {

        if (isString(arr)) {
          arr = [arr];
        }

        arr.forEach(function (item) {
          local.removeItem(item);
        });

        if (callback) return callback();
      }
    };

  Storage.local = isApp ? chrome.storage.local : w3cLocal;
  Storage.fs = fs;
  Storage.fs.init(null,function(){
    observer.trigger("storage:init.end");
  });
  return Storage;
});
