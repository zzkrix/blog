---
title: "redis 热点 key"
date: 2023-03-10 20:01:32
description: ""
draft: false
tags: ["redis"]
categories: ["redis"]
series: []
---

单机 QPS 瓶颈后，可以用集群分片，来分担请求压力，但是如果一个 key 就是在某一个分片上形成了热点 key 怎么办。

对 key 的值在业务上拆分，使其分散到更多的分片上。

或者如果 key 对应的数据允许有一定的误差，可以将该值存在进程内存里，做二级缓存，定时同步 redis 即可。
