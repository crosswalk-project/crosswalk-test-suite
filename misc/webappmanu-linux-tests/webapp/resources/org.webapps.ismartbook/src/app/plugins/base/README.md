# 控件的基础类 Base 

`Base`对`Backbone`的基础类进行了扩展，减少开发者的代码量。同时提供了Reader的一些参数。

当前控件最好的是基于 Reader 的基础类 `Base` 进行扩展。

## 1. 如何取得

在定义模块的时候使用`var Base = require('base');` 既可使用 `Base`。

## 2. 代码的位置

Reader 目录下面的`app/plugins/base`即为 `Base` 所使用到的所有代码。

## 3. Base 的 API

`Base`的API有：

* View
* Model
* Collection
* fullPath
* controller

下面介绍每个API：

### 3.1 View

调用方式为`Base.View`。

基于Backbone的原生方法进行了扩展，增加了以下内容：

* page
* itemId
* modelEvents
* mixins
* initialize
* emit
* addClass

下面详细解释新增加的内容：

*   `page` 属性
    
    当前控件的页码
    
*   `itemId` 属性
    
    当前控件的itemId
    
*   `modelEvets` 属性 

    用户可以定义`modelEvents`来简化对model事件的绑定。其使用方法类似Backbone的Events，将事件绑定到`this.model`上。(注：必须要在初始化的时候设定`this.model`,初始化之后再设定的`this.model`无法绑定相关事件)。
    
    例如：
    
    ```
      "modelEvents":{
        "change":"onModelChange"
      }
    ```

    其等价于：
    
    `this.model.on('change',this.onModelChange.bind(this))`

*  `mixins` 属性

    该属性用来将View的属性模块化，详细资料参考：

    系统本身希望除了控件本身能模块化之外，连控件的某些方法也能模块化，因此使用了[Cocktail](https://github.com/onsi/cocktail)的扩展，可配合`requirejs`做更灵活的模块化，其官方描述为：
   
    > Break out your shared Backbone.js model/collection/view behaviors into separate modules and mix them into your classes with Cocktail - an implementation of Backbone mixins.
      
*  `initilize`函数
   
    覆盖了原生函数，提供了该函数的三个参数描述：
   
       * `$el`
     
         第一个参数为该控件的DOM，在传递进来之间已经jQuery化，并且预先绑定在View上面了，用户可以无需再次绑定即可直接以`this.$el` 来获取该DOM
   
       * `config`
   
         第二个参数为用户写在`controls-data.json` 文件里面，与 `this.itemId`相关的参数，在传递进来之前，系统已经额外的增加了`fullPath`,`itemId`这两个参数，用户可以直接通过`config.fullPath`/`config.itemId`获取。
   
       * `page`
      
         第三个参数为当前控件所在的页数。
   
*   `emit`函数

    signal的触发函数，以Card为例，如果要发出`selected.card`的signal，则可以直接：
  
    `this.emit('selected.card',this.itemId);`
  
    其中`selected.card` 为signal名称，后面的为传递的参数。

*   `addClass` 函数
  
    该函数可协助用户简单的添加控件所需要的CSS文件。例如：
  
    `this.addClass('./card.css')`
  
    其就向HTML里面添加了控件目录下面的`card.css` 文件。


  
  
### 3.2 Model

调用方式为`Base.Model`。

为 Backbone的原生方法，未扩展。

### 3.3 Collection

调用方式为`Base.Collection`。

为 Backbone的原生方法，未扩展。

### 3.4 fullPath

调用方式为`Base.fullPath`。

书本的绝对路径，如`http://localhost/book/OEBPS/`，该路径可以和其他路径配合得到资源的绝对路径。

这个主要是为了非`View`扩展内容用的。

### 3.5 controller

调用方式为`Base.controller`。

书本是不是控制端，如果为0则为学生端的。方便控件层面针对两个不通的终端做交互限制