#!/usr/bin/env python
# coding=utf8
# Copyright (C)  www.361way.com site All rights reserved.

import requests, json

def loginRight():
    url = 'http://dev.api.education.webus.vip:12321/api/v1/admin/login'
    data = {'phone': '18358103147', 'password': '654321'}
    r = requests.post(url, data)
    print(r)
    #以文本格式返回响应内容
    print('text',r.text)
    #以字节格式返回响应内容
    print('content',r.content)
    #以json格式返回相应内容，因为就算请求出错也会返回一串json格式的字符串。所以可以使用r.status_code或者r.raise_for_status来判断响应是否成功
    print('json',r.json())
    code = r.status_code;
    print('code=',code)
    json = r.json()
    #获取到响应内容中的token，后面的接口调用
    token = json['access_token']
    print('token',token)
    assert code == 200
    assert r.json().get('access_token') != ""