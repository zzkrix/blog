---
title: "lsof"
date: 2023-04-18 17:54:01
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

> lsof = list open file

```bash
-i  # 查看网络
-c  # 某进程打开的文件
-p  # 某进程号打开的文件
-r  # 重复执行时间间隔，单位秒
-n  # 将出现的主机名转换成IP显示
```

`lsof -i tcp`

`lsof -i udp`

`lsof -n -i tcp`

`lsof -c 进程名`

`lsof -p pid`

`lsof -r 1` 每秒执行一次
