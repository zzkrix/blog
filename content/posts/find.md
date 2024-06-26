---
title: "find"
date: 2023-12-12 20:04:05
description: ""
draft: false
tags: ["linux", "命令"]
categories: ["linux"]
series: []
---

`find . -type f -name "*.png" -exec ls -l {} \;`

> `{}` 是一个替换符，表示前面找到的内容
> `\;` 是`exec`的默认结尾标识符

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231213090218543.png)

`find /sys/devices/virtual/net -name iflink -exec grep -H -w 11 {} \;`

> grep 增加`-H`选项后，可以显示文件名

![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231214091431297.png)

如果目录下有软连接的外部文件夹，默认 find 不会显示软连接里的内容，如果需要可以加上`-L`，但是注意，如果软连接有循环，则会不停的输出，慎用，比如：
![](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/image-20231214092531133.png)
