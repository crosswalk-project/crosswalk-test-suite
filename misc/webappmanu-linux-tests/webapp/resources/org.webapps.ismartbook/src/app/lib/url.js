define(function(require){
 var arrTrim = function(arr){
  // get start
  var start = 0;
  arr.some(function(item,index){
    if (item !== "") return true;
    start ++;
  });

  //get end ;
  var end = arr.length;
  arr.some(function(item){
    if (item !== "") return true;
    end --;
  });

  if (start > end) {
    return [];
  }
  return arr.slice(start, end+1);
  

 };

 var relative = function(from, to) {
    console.log(from,to);
    var fromPath = arrTrim(from.replace("//","/").split("/"));
    var toPath = arrTrim(to.replace("//","/").split("/"));
  

    var minPath = fromPath.length >= toPath.length? toPath:fromPath;

    var samePartsLength = minPath.length;
    var outputParts = [];

    minPath.some(function(item,index){
      if (fromPath[index] !== toPath[index]) {
         samePartsLength = index;
         return true;
      }
    });

    // get up level 
    fromPath.slice(samePartsLength).forEach(function(item){
      outputParts.push("..");
    });

    outputParts = outputParts.concat(toPath.slice(samePartsLength));

    return outputParts.join("/");
  }



  function realpath (path) {
  
    var isUrl = 0, paths = []; 
    var isFile = window.location.protocol === "file:";
    var href = window.location.origin + window.location.pathname;
    console.log(href,path);
    var result = [];

    path = (path + "").replace("\\", "/"); 
    
    if (path.indexOf("://") !== -1) {
      isUrl = 1;
    } 
    // if path is a relative path ,
    // change it to absoute path;
    if (!isUrl) {
      path = href.substring(0, href.lastIndexOf("/") + 1) + path;
    } 
  
    paths = path.split("/");

    paths.forEach(function(item){
      if (item == ".") return ;
      if (item == ".." && result.length > 3) {
        result.pop();
        return ;
      }
      if (item !== "" || result.length < 2) {
        result.push(item);
      }
    });

    if (isFile) {
      result.splice(2,0,"");
    }

    return result.join("/");
  }

return {
    realpath:realpath,
    relative:relative
    };
});