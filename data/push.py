#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from socket import *

HOST = '39.170.4.213' # 主机ip
PORT = 18307 # 软件端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) # 创建socket对象
tcpCliSock.connect(ADDR) # 连接服务器


def sendToTraveler():       #推送给乘客端
    msg = {
        "jsonrpc":"2.0",
        "method":"1.0::App\\Rpc\\Lib\\JpushInterface::sendToTraveler",
        "params":["UserTestdemo001",{},'171976fa8a16923d74a',{}],
        "id":1,
        "ext":[]
         }
    json_encode = json.dumps(msg)
    print(json_encode)
    # print(type(json_encode))
    tcpCliSock.send((json_encode + "\r\n\r\n").encode())   #发送消息
    data = tcpCliSock.recv(BUFSIZ) #读取消息
    print(data.decode('utf-8'))
    tcpCliSock.close() #关闭客户端


def sendToDriver():       #推送给司机端
    msg = {
        "jsonrpc":"2.0",
        "method":"1.0::App\\Rpc\\Lib\\JpushInterface::sendToDriver",
        "params":["Drivertestdemo001",{},'101d855909d231d86fc',{}],
        "id":1,
        "ext":[]
         }
    json_encode = json.dumps(msg)
    print(json_encode)
    # print(type(json_encode))
    tcpCliSock.send((json_encode + "\r\n\r\n").encode())  # 发送消息
    data = tcpCliSock.recv(BUFSIZ)  # 读取消息
    print(data.decode('utf-8'))
    tcpCliSock.close()  # 关闭客户端

def sendToDevice():     #推送验票端
    pass


def sendToMonitor():        #推送给Android大屏
    pass
