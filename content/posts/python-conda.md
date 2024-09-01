+++
title = 'Conda 安装和使用'
date = 2024-08-30T14:23:24+08:00
draft = false
tags = ["python", "conda"]
categories = ["python", "conda"]
+++


## 介绍

[Conda](https://docs.anaconda.com/) 可以用来在一台机器上管理不同的 Python 版本。

比如项目 A 使用 python3.10，项目 B 使用 python3.12。

Conda 有两个版本：Anaconda 和 Miniconda。

一般选择 Miniconda 就可以了，Anaconda 只是多了一些科学计算相关的包。

![2024-08-30-15-01-64AKdK](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-30-15-01-64AKdK.png)

## 安装

这里只讲 [Miniconda](https://docs.anaconda.com/miniconda/#quick-command-line-install) 安装。

```bash
# 创建一个文件夹，用来存放 miniconda 和它将要管理的 Python 相关文件。
# 文件夹名字可以随便写，只要后面命令保持一致即可
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

# 执行安装
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

惊！这个安装用的 shell 脚本竟然有 142M（里面包含一些可执行文件内容）。
![2024-08-30-15-11-n20qj4](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-30-15-11-n20qj4.png)

![2024-08-30-15-17-xRb7gt](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-30-15-17-xRb7gt.png)

根据你使用的 shell 类型进行初始化。init 之后，重启下终端，就自动激活 conda 环境了。

```bash
~/miniconda3/bin/conda init bash
或
~/miniconda3/bin/conda init zsh
或
~/miniconda3/bin/conda init fish
或
~/miniconda3/bin/conda init <其他>
```

默认情况下，每次进入终端，都会打开一个名为`base`的 conda 环境，一点用都没有。

所以重启终端后，执行下面的命令禁用它：

```bash
conda config --set auto_activate_base false
```

## 使用

帮助信息 `conda -h`：

```bash
$ conda -h
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...

conda is a tool for managing and deploying applications, environments and packages.

options:
  -h, --help          Show this help message and exit.
  -v, --verbose       Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.
  --no-plugins        Disable all plugins that are not built into conda.
  -V, --version       Show the conda version number and exit.

commands:
  The following built-in and plugins subcommands are available.

  COMMAND
    activate          Activate a conda environment.
    clean             Remove unused packages and caches.
    compare           Compare packages between conda environments.
    config            Modify configuration values in .condarc.
    content-trust     Signing and verification tools for Conda
    create            Create a new conda environment from a list of specified packages.
    deactivate        Deactivate the current active conda environment.
    doctor            Display a health report for your environment.
    export            Export a given environment
    info              Display information about current conda install.
    init              Initialize conda for shell interaction.
    install           Install a list of packages into a specified conda environment.
    list              List installed packages in a conda environment.
    notices           Retrieve latest channel notifications.
    package           Create low-level conda packages. (EXPERIMENTAL)
    remove (uninstall)
                      Remove a list of packages from a specified conda environment.
    rename            Rename an existing environment.
    repoquery         Advanced search for repodata.
    run               Run an executable in a conda environment.
    search            Search for packages and display associated information using the MatchSpec format.
    update (upgrade)  Update conda packages to the latest compatible version.
```

创建指定 python 版本的 conda 环境：

```bash
conda create --name <env_name> python=<version>

# 创建一个名称为 myenv 的 python3.10 版本的环境
conda create --name myenv python=3.10
```

查看已有 conda 环境：

```bash
conda env list
```

切换 conda 环境：

```bash
conda activate <env_name>
```

删除某个 conda 环境：

```bash
conda remove --name <env_name> --all
```

退出 conda 环境：

```bash
conda deactivate
```

## conda & venv

conda 管理的是 python 多版本，venv 管理的是多项目的依赖。

这俩并不冲突，可以理解成 conda 管理的比 venv 高一层。

你可以在某一个 conda 环境里在使用 venv 创建项目的虚拟环境。

并且在创建完虚拟环境后，也可以在 conda 环境之外进入该虚拟环境。

在该虚拟环境里安装的包，只在该虚拟环境内有效。

## 其他

实际上，conda 不仅可以用来管理 python，还可以管理其他语言。

比如创建一个 go1.21 的 conda 环境：

```bash
conda create --name go1.21 go=1.21
```

更多支持语言看[这里](https://github.com/conda/conda/blob/ef93541d0132837ede502a2b62e88d9169cdc872/conda/base/constants.py#L286-L303)。

[官方说明](https://docs.anaconda.com/miniconda/)里有这么一段话：
![2024-08-30-17-26-KL5Xuy](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-30-17-26-KL5Xuy.png)

翻译过来就是：

Miniconda 可供任何人免费使用！但是，只有个人和小型组织（少于 200 名员工）才能免费访问 Anaconda 的公共软件包存储库。大型组织和任何嵌入或镜像 Anaconda 存储库的人都需要付费许可证。有关详细信息，请参阅 [TOS](https://legal.anaconda.com/policies/en/)。

[卸载 conda](https://docs.anaconda.com/anaconda/install/uninstall/):

```bash
conda activate
conda init --reverse --all

# 注意这里是你 conda 的安装目录，默认是 miniconda3
rm -rf ~/miniconda3
```
