/**
 * pkg loader for requirejs
 * Help people to load package with `pkg!`  
 * @example
 * First, add module config like this:
 * ```
 *     requirejs.config({
 *         config:{
 *             pkg:{
 *                 path:'plugins'
 *             }
 *         }
 *     })
 * ```
 * then if you use the file `pkg!core` will load the script as `plugins/core/main.js`
 */
define(function(require,exports,module){
    var pack,
        config = module.config();

    var parse = function(name){
        
        return config.path + '/' + name +'/main';

    };

    pack = {
        load: function (name, req, load, config) {
            name = parse(name);
            req([name], function (value) {
                load(value);
            });
        }
    }
    return pack;
});
