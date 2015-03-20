# Core 

是READER的核心，负责初始化Plguin、Reader数据层以及书本的解析。

该插件目录文件详解：

*   action.fix.js

    用来屏蔽某些JS行为。

*   bookModel.js 
    
    书本的数据层，初始化的时候会调用etb相关函数解析书本数据。

*   readerModel。js

    Reader的数据层，用来统一整个书本的状态


*   main.js 
    
    入口文件，负责整本书的样式以及手势控制。



 