#! /usr/bin/env/ python
# coding=utf-8
import requests


def test_upload_image():
    type = "image"
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload"
    payload = {'access_token': access_token, 'type': type}
    upload_files = {'media': ('th3.png', open('python.jpg', 'rb'), 'image/jpg')}
    res = requests.post(url, files=upload_files, params=payload)
    print("res.json=", res.json())
    assert res.json().get('errcode') == 0









