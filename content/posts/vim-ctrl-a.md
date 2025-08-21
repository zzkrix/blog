---
title: "vim 中数字增加或减少"
date: 2024-01-09 16:55:39
description: ""
draft: false
tags: ["vim"]
categories: ["vim"]
series: []
---

光标放在数字上：

- `ctrl + a` 数字加 1
- `ctrl + x` 数字减 1

将某一列数字递增的加 1：
选中该列，按`g`，再按`ctrl + a`

```vim
1
1
1
1
1
```

将变成

```vim
2
3
4
5
6
```
