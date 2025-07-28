+++
title = '命令行 vi 模式快捷键冲突解决'
date = 2025-07-28T13:43:39+08:00
draft = false
tags = ["vim", "iterm2"]
categories = ["vim"]
+++

默认配置了 vi 模式后，`ctrl + a / ctrl + e / ctrl + r` 这三个命令是不生效的。需在`~/.zshrc`中配置下面的内容：

```zsh
bindkey -v  # 启用 vi 模式

# 设置 vi 模式下插入态使用 emacs 的快捷键
# ctrl + a / ctrl + e / ctrl + r
bindkey -M viins '^A' beginning-of-line
bindkey -M viins '^E' end-of-line
bindkey -M viins '^R' history-incremental-search-backward
```
