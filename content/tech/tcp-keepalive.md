---
title: "tcp 保活"
date: 2023-12-04 20:11:39
description: ""
draft: false
tags: ["linux", "网络"]
categories: ["linux"]
series: []
---

```bash
没有数据发送后，多长时间发送保活探测包
/proc/sys/net/ipv4/tcp_keepalive_time

保活探测包多久发一次
/proc/sys/net/ipv4/tcp_keepalive_intvl

最多发几次保活探测包
/proc/sys/net/ipv4/tcp_keepalive_probes
```

<https://juejin.cn/post/7142654287493988359>
