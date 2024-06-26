---
title: "xargs"
date: 2023-12-22 16:03:59
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

```
# xargs -t # 在执行前先打印处要执行的命令
# xargs -I {} # 设置一个符号{}表示管道前面的某一行输出内容，以便后续复杂命令进行替换
# xargs -P `nproc` # 并发数，默认为1，如果置0表示让xargs使用尽可能多的并发数，这里`nproc`是cpu核数

docker ps -q | xargs -t -I {} docker exec {} sh -c "find /sys -name iflink | xargs grep -w 14"

等价于

# 最后的 grep -H 表示查找到内容后显示对应的文件名
docker ps -q | xargs -t -I {} docker exec {} sh -c "find /sys -name iflink | xargs -I {} grep -w 14 {} -H"
```
