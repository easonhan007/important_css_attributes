根据css属性在流行框架中出现的次数排序，从而找到最需要学习的css属性。

### 如何实现

首先下载好一些流行的css框架，目前有

* twitter-bootstrap
* bulma
* foundation
* materialize
* pure
* semantic-ui

再使用bash来统计各个属性出现的次数

```
cat *.css | grep  ';' | tr -d ' ' | cut -d ':' -f 1 | sort | grep -v "^-" | grep -v "^/"| grep -v "^\."| grep -v "^\*"|grep -v "^@"| grep -v "^\s"|uniq -c | sort -r > all.txt
```

输出大概是这样的

```
head all.txt

248 color
248 background-color
237 display
134 margin-left
114 border-color
89 padding
85 max-width
85 margin-bottom
81 width
80 flex
```
数字代表css属性出现的次数。

最后将具体属性在[mdn](https://developer.mozilla.org/en-US/)中查找，方便学习，顺便输出reference.md文件，可以在github中查看。

```
python make_doc.py > reference.md
```

### reference 文件

[reference.md](/reference.md)

### 总流程

```
./download.sh # 下载css文件
./attr.sh *.css > all.txt # 输出临时文件
python make_doc.py > reference.md # 创建md文件
```

### TODO

* 为每一个css框架增加版本配置，每次下载最新版本
