---
title: "Mac 下为 Python 安装 mysqlclinet"
date: "2024-05-06T14:24:49+08:00"
draft: false
tags: ["mac", "python"]
categories: ["mac", "python"]
---

如果直接执行`pip install mysqlclient`，会报错，需要先安装依赖：

```bash
brew install mysql-client

# 必须加这个环境变量，否则后面 pip 安装还是会报错，可以将这个加到 ~/.bash_profile 或者 ～/.zshrc 中
export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"
```

然后再执行：

```bash
pip install mysqlclient
```
