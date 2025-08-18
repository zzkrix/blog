---
title: "docker 仓库"
date: 2023-07-29 22:01:35
description: ""
draft: false
tags: ["docker"]
categories: ["docker"]
series: []
---

## 配置自定义仓库地址

Linux 下创建并修改 `/etc/docker/daemon.json`

```bash
{
  "registry-mirrors": [
    "https://a.b.c",
  ],
  "insecure-registries": [
    "192.168.199.100:5000"
  ]
}
```
