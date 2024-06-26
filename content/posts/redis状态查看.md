---
title: "redis 状态查看"
date: 2023-03-10 21:11:22
description: ""
draft: false
tags: ["redis"]
categories: ["redis"]
series: []
---

## 查看大 key

`redis-cli -h 127.0.0.1 -p 6379 --bigkeys`

> 使用 scan 扫描，对性能影响较小

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20230310212039340.png)

## 查看状态

`redis-cli -h 127.0.0.1 -p 6379 --stat -i 3`

> -i 3 每隔 3 秒输出一次

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20230310213230350.png)
