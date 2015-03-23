# 教学助手
## 需求
1. book.end.preload 之后cache所有的助手需要使用的信息到model里面。
2. 如果这一层数据过长，应该先将数据缓存到本地store里面，如indexeddb or localStorage
3. 系统在翻页之后找到新的内容并替换掉原来的内容。
4. 支持html，当然如果能支持前端markdown最好。
5. 在不同模式下面有不同的转化过程。


