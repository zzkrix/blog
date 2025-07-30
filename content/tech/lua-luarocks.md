---
title: 'lua 包管理工具 luarocks'
date: '2025-07-30T12:04:39+08:00'
draft: false
tags: ['lua']
categories: ['lua']
---

## 介绍

luarocks 是 lua 的包管理工具。

可以搜索和安装第三方依赖包。

但是不支持导出当前项目依赖的包版本到项目依赖文件 - 垃圾😒~

## 安装

MacOS： `brew install luarocks`

其他平台： <https://github.com/luarocks/luarocks/wiki/Download>

## 常用命令

搜索依赖：`luarocks search <package-name>`

安装依赖：`luarocks install <package-name> <package-version> --tree <save-path>`

```bash
# 默认是全局安装，可以使用--tree 指定安装目录

luarocks install lua-cjson --tree ./thirdlibs


# 不加版本号默认安装最新版本
# 如果指定版本号，会将其他版本删除
# 即luarocks只能保存某个包的某一个版本

luarocks install lua-cjson 2.1.0.9-1 --tree ./thirdlibs
```

查看安装的依赖： `luarocks list --tree <save-path>`

## 其他

lua 依赖导出脚本：

<https://github.com/zzkrix/scripts/blob/main/lua/lua-dependencies-checkout.lua>
