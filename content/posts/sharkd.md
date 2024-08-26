+++
title = 'sharkd 使用'
date = 2024-08-26T17:04:45+08:00
draft = false
tags = ["sharkd"]
categories = ["sharkd"]
+++


## 介绍

官方文档： <https://wiki.wireshark.org/Development/sharkd>

sharkd 用来解析数据包，并提供接口用于数据查询（tcp 或本地 socket）。

可能是文档太久未更新，官方文档中的使用方法有错误，通过查看 [sharkd 源码](https://github.com/wireshark/wireshark/blob/master/sharkd.c)，

发现所有发送给 sharkd 的请求格式都应该是类似 `{"jsonrpc":"2.0","id":1, "method": "xxx"}`，而不是官方文档中的 `{"req": "xxx"}`。

> 官方示例中的 req 应该替换成 method。
>
> json 数据里都需加上  "jsonrpc":"2.0","id":1
>
> 其中的 id 目前还不清楚什么含义，可能是每个抓包文件对应不同的 id。

其他参数参考官方文档即可。

## 示例

示例一：让 sharkd 加载抓包文件

```json
{"jsonrpc":"2.0","id":1, "method": "load", "file": "/tmp/test.pcap"}
```

> 对 sharkd 来说，文件是一次性加载的，如果加载后文件发生变化，sharkd 并不会动态更新，所以需要开发人员给 sharkd 发送上述指令重新加载。

示例二：使用代码和 sharkd 交互

```python
import socket

def get_json_bytes(json_string):
    return bytes((json_string + '\n'), 'utf-8')

def json_send_recv(s, json) -> str:
    s.sendall(get_json_bytes(json))
    data = s.recv(1024)
    return data[:].decode('utf-8')

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect("/home/node/sharkd.sock")

json_string = '{"jsonrpc":"2.0","id":1, "method": "status"}'
print('send: ' + json_string)
rx_json = json_send_recv(s, json_string)
print('recv: ' + rx_json)

s.close()
```

## 编译

```bash
git clone --depth=1 https://github.com/wireshark/wireshark

cd wireshark

# debian 系使用这个，其他平台在tools目录下找对应的文件即可
tools/debian-setup.sh

mkdir build

cd build

cmake -DBUILD_wireshark=OFF ..

make -j
```
