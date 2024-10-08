---
title: "docker 安装"
date: 2023-12-07 16:04:42
description: ""
draft: false
tags: ["docker"]
categories: ["docker"]
series: []
---

安装 docker

```bash
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun
```

建立 `docker` 组：

```bash
$ sudo groupadd docker
```

将当前用户加入 `docker` 组：

```bash
$ sudo usermod -aG docker $USER
```



