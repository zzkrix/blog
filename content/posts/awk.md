---
title: "awk"
date: 2023-12-22 16:17:59
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

awk 指定多个分隔符 `awk -F '[;:]'`（使用`;`或`:`进行分割）

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231212230106796.png)

```bash
获取最后一列
awk '{print $NF}'
```
