---
title: "grep"
date: 2023-12-13 16:04:04
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

## 或运算

`-E` 参数加上`|`

`lsof -i | grep -E 'epc-ims:|IPv6'`

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231213161825123.png)

## 与运算

实际上就是正则`.+`表示任意 N 个字符

`lsof -i | grep -E "8323.+38911"`

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231213161727296.png)
