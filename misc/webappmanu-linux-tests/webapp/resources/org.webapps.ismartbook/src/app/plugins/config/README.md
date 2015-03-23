# 配置插件

将全局的配置文件合并成为一个。

## 使用方法

`var config = require('pkg!config')`;

即可以`config` 来获取相关的配置。

## 配置的来源


* app/config.json，系统的配置文件
* config/modes.json，系统默认的一些配置合集
* localStorage，本地缓存的文件配置。
* ....


## 配置权重以及覆盖机制

如果两个配置当中有相同的配置，权重大的将会覆盖权重小的。当前的权重如下：

localStorage > config/modes.json > app/config.json


