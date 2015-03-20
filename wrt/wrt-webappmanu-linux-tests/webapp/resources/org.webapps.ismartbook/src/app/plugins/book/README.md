# Book

与书本直接关联的插件，该插件包含以下的功能：

* 书本内容的缓存
    * 缓存控件类
    * 缓存书本页面渲染关联的数据
       * controls-data.json
       * signal-map.json
* 书本内容在Reader当中的加载：
    * HTML的渲染
    * 控件类的缓存和控件实例化
    * Signal/Slot通讯机制的处理
* 其他与书本内容相关的操作：
    * 翻页
    * 书本整体的缩放


## 核心文件`main.js`的解读：

book插件的`main.js`只负责

 * 预先加载BookView，让其依赖的`unit.js` 能注册自己的初始化函数到`book:start.preload`事件上
 * 预先让BookView的实例化，好让BookView能注册全局
 * 将全局事件和BookView的相关API进行绑定。
 * 在书本缓存完成之后，执行BookView.endInit方法来让书本进行渲染。

在开发阶段只要保证 BookView 的API一致性（包括函数名称、事件以及事件传参），即可更换不同的BookView实现。

当前插件下面就有三个不同的BookView的实现:

   * turn.js
   * bookblock.js
   * custom.flip.js

用户只需切换相关的module即可实现更换BookView。


## 书本内容的缓存


### 控制层 unit.js

控制层 unit.js 包含其他两个执行缓存行为的对象：

* connect.js
* control.js

unit.js监听`book:stat.preload`事件，并执行两个对象的`cache`方法。通知两个对象对book的数据进行缓存。

* `connect:end.cache`
* `controls:end.cache`


### signal/slot数据缓存层 connect.js

connect.js 是具体实现singal/slot机制的文件。

在缓存阶段，他通过`toc.ncx`文件解析的结果，找到所有的`signals`节点，将对应的文件内容按照页码全部先缓存下来。

缓存完毕之后会向系统广播`connect:end.cache`事件。

### 控件类以及控件实例化数据的缓存层 controls.js

controls.js 是实例化控件的文件，因此它缓存了两样东西：

*   控件类
    
    通过`controls/controls.json`知道控件目录下所有的控件目录，然后使用`requirejs`加载控件的`main.js`文件，将文件返回的内容缓存下来。

*   控件实例化所需要的数据
    
    在缓存阶段，他通过`toc.ncx`解析的结果，找到所有`controls`节点，将文件内容按照页码缓存下来。

缓存完毕之后会向系统广播`controls:end.cache`事件。



以上是书本缓存阶段三个文件所做的事情，当缓存阶段结束之后，会向系统广播`book:end.preload`事件，通知各个插件书本内容已经缓存完成，可以渲染系统的UI部分了。



## 书本内容在Reader当中的渲染

这块是由该插件下的`singlePage/main.js`/`signlePageWithBlock/main.js`来实现的。

当前的使用到的是BookView 是`signlePageWithBlock/main.js`（以下均描述为BookView），这里就详细讲解下它对书本内容的渲染过程。

1. BookView 根据具体的页数添加和页数一致的空白div。

2.  根据加载的页数选择该页前后一共五页的内容，通过Ajax请求回HTML的内容，将其放置到到对应的空白div里面，并将这部分内容jQuery化，连同页码一起转交给`unit.js`，进行控件的实例化以及Signal/Slot的绑定。相关代码如下：

    `new Unit($pageContent,p)`

3.  在`unit.js`里面，它首先为当前页面创建一个空白的Object用来缓存当前页面所需要用到的东西，并创建一个`pageOb` 作为当前页面的广播者。

4. 接着`unit.js`调用`control.js`提供的`PageRender`的方法将控件实例化。控件实例化所需要的数据来自之前缓存的内容。`pageRender`依照 DOM 提供的`data-id`的值，找到当前`controls-data.json`里面对应的key，获取相关的value，传递给控件，完成实例化。在控件实例化完成之后，unit.js 将实例化之后的控件缓存为一个数组，保存在当前页面缓存的那个Object上面。

5.  最后`unit.js`将这个缓存数据交给`connect.js`的`registerSignal`，让其依照之前缓存的Signal/Slot数据将当前页面控件的signal和slot绑定起来。


## 其他和Book相关的操作

### 接收翻页通知

Book插件绑定了全局的`book:turn.page`事件，这个事件通知Book去调用BookView的翻页函数进行翻页

### Book整体的缩放

Book插件绑定了全局的`book:zoom.in`和`book:zoom.out`事件，用来放大缩小Book的所有内容。该功能主要是和`Toc`插件配合使用。











