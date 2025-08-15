---
title: "CPU 模式下 comfyUI 运行 flux"
date: "2024-08-05T22:07:13+08:00"
draft: false
tags: ["ai", "comfyUI", "flux"]
categories: ["ai", "comfyUI", "flux"]
---

## 下载 comfyUI

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git

# 启动 python 虚拟环境
cd ComfyUI/

python3 -m vevn venv & source ./venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 安装 comfyUI-Manager

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
cd ComfyUI/custom_nodes/ComfyUI-Manager
pip install -r requirements.txt
```

## 下载模型

```bash
cd ComfyUI/models/checkpoints
wget https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors

cd ComfyUI/models/vae
wget https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.sft
```

## 启动

```bash
python main.py --cpu --listen 0.0.0.0
```

浏览器访问 <http://localhost:8188>

输入配置，点击 `Queue Prompt` 开始执行，等待 30 分钟后终于得到一张图（谁能送我一个 H100，我想试试 😊 ······

![2024-08-05-22-20-eVSxvM](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-05-22-20-eVSxvM.png)

![2024-08-05-22-20-SxCWvA](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-05-22-20-SxCWvA.png)

![2024-08-05-22-19-IvXVtG](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-05-22-19-IvXVtG.png)

同样的提示词，steps 设置成 20，跑了第二遍：

![2024-08-06-08-46-0pRGZr](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-06-08-46-0pRGZr.png)

![2024-08-06-08-48-8mEXJI](https://raw.githubusercontent.com/zzkrix/blog-images/main/assets/2024-08-06-08-48-8mEXJI.png)

so，自由就是张开翅膀，拥抱阳光？
