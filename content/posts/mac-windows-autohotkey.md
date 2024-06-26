+++
title = '虚拟机中使用 Mac 快捷键'
date = 2024-06-24T09:47:05+08:00
draft = false
tags = ["mac", "tools"]
categories = ["mac", "tools"]
+++


Mac 上使用虚拟机安装了 Windows，若想正常使用`cmd + c`、`cmd + v`等快捷键，按以下步骤操作。

安装 [AutoHotkey](https://www.autohotkey.com/)，这里选择下载 v1 版本，因为下面的脚本只支持 v1。

![2024-06-24-09-56-zgZaVp](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-06-24-09-56-zgZaVp.png)

从 GitHub 上下载一个脚本[https://github.com/stroebjo/autohotkey-windows-mac-keyboard](https://github.com/stroebjo/autohotkey-windows-mac-keyboard)。

把里面的`MacKeyboard.ahk`这个文件下载下来。

windows 里快捷键 `win + r`，输入 `shell:startup`，回车后会打开开机启动文件夹。

将上面的`MacKeyboard.ahk`文件拖到打开的文件夹里，重启电脑即可。

![2024-06-24-10-03-G9bHyM](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-06-24-10-03-G9bHyM.png)
