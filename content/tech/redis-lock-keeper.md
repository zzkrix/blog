---
title: "分布式锁提前过期"
date: 2023-06-13 17:01:37
description: ""
draft: false
tags: ["redis"]
categories: ["redis"]
series: []
---

如果请求 A 抢到了锁，但是业务处理时间过长，导致分布式锁被 Redis 释放，此时请求 B 过来的时候，会造成并发问题，导致业务出错，怎么解决。

只需要在请求 A 获得锁的同时，创建一个监控程序，当任务未处理完，而锁快过期的时候，延长锁的过期时间即可。

```go
package main

import (
    "fmt"
    "sync"
    "time"

    "github.com/gomodule/redigo/redis"
)

type DistributedLock struct {
    key        string
    value      string
    expiration time.Duration
    conn       redis.Conn
    mu         sync.Mutex
    stopChan   chan struct{}
}

func NewDistributedLock(conn redis.Conn, key string, expiration time.Duration) *DistributedLock {
    return &DistributedLock{
        key:        key,
        value:      fmt.Sprintf("%d", time.Now().UnixNano()),
        expiration: expiration,
        conn:       conn,
        stopChan:   make(chan struct{}),
    }
}

func (l *DistributedLock) Acquire() bool {
    l.mu.Lock()
    defer l.mu.Unlock()

    reply, err := redis.String(l.conn.Do("SET", l.key, l.value, "NX", "PX", int(l.expiration.Milliseconds())))
    if err != nil || reply != "OK" {
        return false
    }
    go l.renewalLoop()
    return true
}

func (l *DistributedLock) renewalLoop() {
    ticker := time.NewTicker(l.expiration / 2)
    defer ticker.Stop()

    for {
        select {
        case <-ticker.C:
            l.mu.Lock()
            storedValue, err := redis.String(l.conn.Do("GET", l.key))
            if err == nil && storedValue == l.value {
                _, _ = l.conn.Do("PEXPIRE", l.key, int(l.expiration.Milliseconds()))
            }
            l.mu.Unlock()
        case <-l.stopChan:
            return
        }
    }
}

func (l *DistributedLock) Release() {
    l.mu.Lock()
    defer l.mu.Unlock()

    close(l.stopChan)

    script := redis.NewScript(1, `
        if redis.call("GET", KEYS[1]) == ARGV[1] then
            return redis.call("DEL", KEYS[1]) 
        else 
            return 0
        end`)
    _, _ = script.Do(l.conn, l.key, l.value)
}

func main() {
    conn, err := redis.Dial("tcp", "localhost:6379")
    if err != nil {
        panic(err)
    }
    defer conn.Close()

    lock := NewDistributedLock(conn, "my_lock", 10*time.Second)
    if lock.Acquire() {
        defer lock.Release()

        fmt.Println("Lock acquired!")
        time.Sleep(15 * time.Second) // 模拟长时间操作
        fmt.Println("Lock released!")
    } else {
        fmt.Println("Failed to acquire lock!")
    }
}
```

参考资料：
[https://www.51cto.com/article/742568.html](https://www.51cto.com/article/742568.html)
