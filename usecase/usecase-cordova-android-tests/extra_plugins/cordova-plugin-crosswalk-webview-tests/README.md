## Introduction

This plugin is used for testing the Embedding API in cordova-plugin-crosswalk-webview.


## Authors:

* Zhu, Yongyong <yongyongx.zhu@intel.com>

## how to install

Enter you project directory then run:
cordova plugin add <plugin_path>/cordova-plugin-crosswalk-webview-tests

##usage

```js
navigator.webview.canGoBack(function(error, res){
  if(error){
    console.error(error);
  }else{
    console.log('ok',res.getCanGoBack);
  }
});
```

