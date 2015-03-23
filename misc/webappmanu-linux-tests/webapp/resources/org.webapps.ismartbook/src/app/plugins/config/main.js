/**
 * 配置文件模块
 * 这个模块是将各种配置文件的内容进行汇合
 * @author William<weix.ge@intel.com>
 * @return {Object} 配置类的一个实例
 */
define(function(require, exports, module) {
  /**
   * 系统配置参数.
   * @type {String}
   */
  var Config = require("text!../../config.json");
  var fileProtocols = ["file","filesystem","http","https","chrome-extension"];
  /**
   * 预设的一些配置参数
   * @type {String}
   */
  var ModeConfig = require("text!../../config/mode.json");
  /**
   * Backbone 需要使用到里面的Model
   * @type {Object}
   */
  var Backbone = require("backbone");

  /**
   * 存储插件
   * @type {[type]}
   */
  var Storage = require("pkg!storage");

  var _ = require("underscore");

  var url = require("../../lib/url");

  /**
   * 配置文件类
   * @class
   */
  var Configure = Backbone.Model.extend({
    /**
     * 初始化函数
     * @constructor
     * @param {Object} config 包含Config 以及 ModeConfig,结构如下：
     *    {
     *      "config":Config,
     *      "modes":ModeConfig
     *    }
     */
    initialize: function(config) {
      var modes = config.modes;
      config = config.config;

      if (!config || !modes) {
        console.error("no config / modes file");
        return;
      }
      // 将文本格式的 JSON 解析成为Javascript使用的 Object
      config = JSON.parse(config);
      modes = JSON.parse(modes);

      // 设置该配置信息的名称，名称和书本路径有关联。
      // 这样允许多本书有不同的配置信息
      this.set("name", "config." + config.path);

      // 清理原来缓存的配置信息
      if (config.dev) {
        this.clearLocal();
      };

      //将不同地方的 config 数据进行汇总。
      // config 内容来源于: 
      //  * reader/config.json
      //  * reader/config/modes.json
      //  * 原来保存在localStorage里面，通过上面的名称获取的Item

      // 获取本地已经有的相关配置文件
      // 合并的过程当中的覆盖顺序为
      // modes会覆盖config里面同名的配置信息
      // localConfig会覆盖modes和config里面的同名配置信息
      this.getFromLocal(function(localConfig) {
        config = this.mergeConfig(config, modes, localConfig);

        // 将新的配置信息缓存在本地
        this.set(config);
        this.save();
      }.bind(this));

    },
    parseHrefConfig: function() {
      var href = location;
      var hrefConfig, tmp = {};
      if (!href.search) return {};

      hrefConfig = href.search.split("?")[1];
      hrefConfig = hrefConfig.split("&");
      hrefConfig.forEach(function(item) {
        item = item.split("=");
        tmp[item.shift()] = decodeURIComponent(item.join("="));
      });
      return tmp;

    },
    mergeConfig: function(config, modes, localConfig) {
      var hrefConfig = this.parseHrefConfig();
      // 如果config.mode 有配置，并且modes里面有相关的内容 
      // 则将modes里面的相关内容和config 合并
      if (config.mode && modes[config.mode]) {
        config = _.extend(config, modes[config.mode]);
      }

      // 如果有 localConfig保存的内容
      // 则将localConfig的内容和config的合并
      if (localConfig) {
        config = _.extend(config, localConfig);
      }

      if (hrefConfig) {
        config = _.extend(config, hrefConfig);
      }
      
      this.parsePath(config);

      // 返回合并后的配置信息
      return config;
    },
    parsePath:function(config){
      var baseUrl = require.toUrl("");
      var bookPath = config.path;
      var protocol = bookPath.split(":");
      var isUrl = fileProtocols.indexOf(protocol[0]) > -1;

      if (!isUrl) {
        config.path = url.realpath(config.path);
      }
    },
    /**
     * 目前为saveToLocal的alias
     */

    save: function() {
      this.saveToLocal();
    },
    /**
     * 从本地获取原先保存的配置。
     * @return {Object} 如果有的话，则返回配置文件的Object
     */

    getFromLocal: function(cb) {
      if (!_.isFunction(cb)) return;

      var name = this.get("name");

      Storage.local.get([name], function(obj) {
        if (obj[name]) {

          data = JSON.parse(obj[name]);
        } else {
          data = obj;
        }
        return cb(data);
      });
      return cb(false);
    },
    /**
     * 保存当前的配置信息到本地
     */

    saveToLocal: function() {

      // 调用backbone.model.toJSON的方法获取到当前配置文件的JSON格式的内容
      var data = this.toJSON();
      var name = this.get("name");
      var obj = {};
      obj[name] = data;
      // 将内容保存到localStorage
      Storage.local.set(obj);
    },
    /**
     * 清理本地同名的配置信息
     */

    clearLocal: function() {
      // 获取到配置的名称，并将同名的配置信息删除掉
      Storage.local.remove(this.get("name"));
    },
    /**
     * 清理本地缓存的所有配置信息
     */

    clearAll: function() {
      Storage.local.clear();
    }
  });

  return new Configure({
    config: Config,
    modes: ModeConfig
  });
});