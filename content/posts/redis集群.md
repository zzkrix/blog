---
title: "redis 集群"
date: 2023-03-10 09:55:54
description: ""
draft: false
tags: ["redis"]
categories: ["redis"]
series: []
---

## 哨兵

> 参考：[https://www.cnblogs.com/kevingrace/p/9004460.html](https://www.cnblogs.com/kevingrace/p/9004460.html)

sentinel 系统可以监视一个或者多个 redis master 服务，以及这些 master 服务的所有从服务；当某个 master 服务下线时，自动将该 master 下的某个从服务升级为 master 服务替代已下线的 master 服务继续处理请求。
![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20230310095645257.png)

## 集群模式下的请求

> 参考： [https://zhuanlan.zhihu.com/p/511199672](https://zhuanlan.zhihu.com/p/511199672)

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20230310102213209.png)

集群模式是去中心化的，随便请求到哪个 master 后，判断 key 属于哪个 hash 槽以及在哪个机器上，进行请求路由。

## 问题

Q：怎么保证高性能、高可用和数据不丢失

使用集群分片保证请求的离散来突破单机 QOS 瓶颈。

使用主从模式保证数据的不丢失。

使用哨兵模式监控 master 可用性，及时提升从服务为主服务，来保证高可用。
