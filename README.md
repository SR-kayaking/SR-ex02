# SR-ex02

## 爬虫部分说明

>依赖库：`PyGithub`

`spider.py`通过调用Github API爬取[vscode仓库](https://github.com/microsoft/vscode/)下所有tag为`feature-request`的issue，并存储在`data.json`中

数据格式为

```json
{
    "title": 标题,
    "reactions":[]
}
```



## 排序部分说明

`data.py`整理`data.json`中的reactions，统计其中positive reactions的数量，并据此划分排序等级，生成`data.txt`文件。

数据格式为

```
[positive reactions count] [level] [title]
```



