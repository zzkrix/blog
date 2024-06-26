---
title: "curl"
date: 2023-03-02 11:25:27
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

## 自动重定向

```bash
curl qq.com -L 
```

## 只显示请求头

```bash
curl qq.com -I 
```

## 添加请求头

```bash
# 请求头的名字最好都按规范首字母大写
curl 192.168.190.1 -H "Host: a.b.c" -H "User-Agent: Chrome"
```
