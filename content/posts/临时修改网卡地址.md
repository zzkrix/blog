---
title: "临时修改网卡地址"
date: 2023-11-01 13:03:49
description: ""
draft: false
tags: ["linux", "网络"]
categories: ["linux"]
series: []
---

```bash
# enp22s0f3 是网卡名

# 添加
ip addr add 192.168.0.1/16 dev enp22s0f3

#删除
ip addr del 192.168.0.1/16 dev enp22s0f3
```
