/**
 * template loader for requirejs
 * Help people to load template with `tpl!`  
 * @example
 * var template = require("tpl!./test");
 * it will load ./test.tpl file and 
 */
define(function(require,exports,module){
    var pack,
        config = module.config();

    pack = {
        load: function (name, req, load, config) {
            name.replace("-","_");
            name = name +'.tpl.js';
            name = req.toUrl(name);
            req([name], function (value) {
                load(value);
            });
        }
    }
    return pack;
});
