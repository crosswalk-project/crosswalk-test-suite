define(function(require,exports,module){
  var defaultSize = 1024*1024*1024;
  var Filer = require("filer");
  /**
   * file system global err function
   * @param err
   * @returns {*}
   */
  var onError = function(err){
    return console.error("Err",err);
  }

  var fs = {
     init:function (size,cb){
       size = size || defaultSize;

       this.filer = new Filer();

       this.filer.init({
         persistent:true,
         size:size
       },function(){
         
         cb && cb();
       },function(error){

        cb && cb(error);
       });
     },
     mkdirpWithFilePath:function(file,callback){
       var folders, length ;
       if(!file){
         callback("noFilePath",null);
         return false;
       }
       var folders = file.split('/');
       folders = folders.slice(0, folders.length - 1);

       return this.filer.mkdir(folders.join("/"),false,callback,onError);
     },
     clearRoot:function(callback){
       var self = this;
       return this.filer.ls("/",function(fileList){
         var length, success;
         length  = fileList.length;
         success  = function(){
           length --;
           if(length === 0 ){
             return callback && callback();
           }
          };
         // 一旦文件一多，这个操作将非常耗费cpu
         // TODO reduce cpu operation;
          return fileList.forEach(function(item){
            return self.filer.rm(item.fullPath,success,onError);
          });
       });
     },
    /**
     * Write File to filesystem;
     * @param fileName
     * @param fileData
     * @param callback
     * @returns {*}
     */
    write:function(fileName, fileData, callback){

      return this.filer.write(fileName,{
        data:fileData,
        type:fileData.type
      },function(fileEntry,fileWriter){
         callback && callback(fileEntry, fileWriter);
      },function(){
        console.error(arguments);
      });
    },
    /**
     * Read file from filesystem
     * @param filePath
     * @param callback
     */
    read:function(filePath,callback){
      if(!filePath){
        callback && callback("error");
        return ;
      }
      this.filer.open(filePath,function(file){
          var reader;
        reader = new FileReader;
        reader.onload = function(e){
          callback && callback(null,e);
          return ;
        };
        reader.readAsText(file);
      },onError);
    },
    exists:function(filePath,callback){
      if(!filePath){
        callback && callback("error");
        return ;
      }
      var folder = filePath.split("/");
      var file = folder.pop();
      folder.join("/")
      this.filer.ls("/"+folder,function(entries){
       var target = _.toArray(entries).filter(function(entry){
          if(entry.name == file) return true;
          return false;
        });
        callback && callback(target[0]);
      })
    },
    /**
     * get file tree
     * @param path
     * @param callback
     */
    getFileTree:function(path,callback){
      var list;
      if(!path){
        path = "/";
      }
      list = [];
      var self  =this;
      var filer = this.filer.bind(this);

      filer.ls(path,function(entries){
         var count = entries.length;
         if(count === 0 ){
           callback && callback();
           return false;
         }
        // check directories
        entries.forEach(function(item){
           var cb, tmp;
          tmp = {};
          tmp.name = item.name;
          tmp.fullPath = item.fullPath;
          cb = function(child){
              count--;
             tmp.child = child;
            list.push(temp);
            if(count== 0){
              callback && callback(list);
              return ;
            }
          };

          if(item.isDirectory){
            self.getFileTree(item.fullPath,cb);
            return ;
          }
          if(item.isFile){
            count --;
            list.push(tmp);
            if(count === 0){
              callback && callback(list);
            }
          }
        });
      });
    }
  };

  return fs;
});