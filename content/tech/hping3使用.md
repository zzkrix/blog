---
title: "hping3 使用"
date: 2023-11-04 11:39:44
description: ""
draft: false
tags: ["其他"]
categories: ["其他"]
series: []
---

发送伪造 syn 握手包：

```bash
-c 次数
-p 目标端口
-a 源IP
-s 源端口
-S 攻击类型是Syn flood

hping3 192.168.190.1 -c 1 -p 6106 -S -a 172.22.0.27 -s 31399
```

hping3 192.168.190.1 -c 1 -p 6109 -S -a 172.22.0.29 -s 31683
