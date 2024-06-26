---
title: "MySQL 允许 root 远程访问"
date: 2023-03-22 16:09:45
description: ""
draft: false
tags: ["mysql"]
categories: ["mysql"]
series: []
---

```bash
$ mysql -u root -p

> use mysql;

> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

> FLUSH PRIVILEGES;
```
