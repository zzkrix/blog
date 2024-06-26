---
title: "redis re-hash 过程"
date: 2023-03-10 20:11:06
description: ""
draft: false
tags: ["redis"]
categories: ["redis"]
series: []
---

数据结构里存放了两个 hash 结构，一个是当前的，一个是 rehash 时候使用的。

数据从旧结构往新结构迁移，为了不影响查询和插入，是渐进式的，新数据写新结构。
