---
title: "解决 vscode 终端乱码"
date: "2024-01-26T09:53:02+08:00"
draft: false
tags: ["vscode"]
categories: ["vscode"]
---

我的终端使用的是 zsh，在 vscode 里打开时显示有乱码。

解决办法是在 `settings.json` 中加入：

```json
"terminal.integrated.fontFamily": "MesloLGS NF",
```
