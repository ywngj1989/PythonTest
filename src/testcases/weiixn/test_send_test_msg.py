#! /usr/bin/env python
# coding = utf-8

import requests

# 发送文本消息
def test_send_text_msg():
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+access_token
    send_json = {
   "touser" : "GaoJian|YuanWanNi",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "这是用自动化接口发送的,少打游戏早睡觉，啊哈哈，潇洒的村妞"
   },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    res = requests.post(url, json=send_json)
    assert res.json().get('errmsg') == 'ok'
    assert res.json().get('invaliduser') == ""
    print(res.json())


def test_send_text_msg_without_msgtype():
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+access_token
    send_json = {
   "touser" : "GaoJian|YuanWanNi",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "agentid" : 1000002,
   "text" : {
       "content" : "这是用自动化接口发送的,不带msgtype"
   },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    res = requests.post(url, json=send_json)
    print('erro=', res.json().get('errmsg'))
    assert 'invalid message type' in res.json().get('errmsg')


# 上传临时素材
def test_get_temporary_materials():
    type = "image"
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    # you.png是要下载的图片的名字，必须在项目目录中存在的
    upload_files = {'media': ('th2.png', open('you.png', 'rb'), 'image/png')}
    url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+access_token+"&type="+type
    res = requests.post(url, files=upload_files)
    print('media_id = ', res.json().get('media_id'))
    assert res.json().get('errcode') == 0


# 获取临时素材
def test_get_materials():
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    media_id = "3PqKTtelx6IVXjqM9hpbX4vvvLPfYbLFx8f9XAUBweKDJE0ATSTlGdILFEswSw4sg"
    url = "https://qyapi.weixin.qq.com/cgi-bin/media/get?access_token="+access_token+"&media_id="+media_id
    res = requests.get(url)
    print("code=", res.status_code)
    assert res.status_code == 200


# 发送图片消息
def test_send_image_msg():
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    media_id = "3PqKTtelx6IVXjqM9hpbX4vvvLPfYbLFx8f9XAUBweKDJE0ATSTlGdILFEswSw4sg"
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + access_token
    send_json = {
                 "touser" : "GaoJian|YuanWanNi",
                 "toparty" : "PartyID1|PartyID2",
                  "totag" : "TagID1 | TagID2",
                  "msgtype" : "image",
                  "agentid" : 1000002,
                  "image" : {
                              "media_id" : media_id
                            },
                  "safe":0,
                  "enable_duplicate_check": 0,
                  "duplicate_check_interval": 1800
                  }
    res = requests.post(url, json=send_json)
    assert res.json().get('errmsg') == 'ok'
    assert res.json().get('invaliduser') == ""
    print(res.json())



# 上传图片
def test_get_picture():
    access_token = "aUV-eEt97o4PllcE5hDruZOXB1ZLJZFAhySoaEnJ8hQmTF0e3VSShkCkGJlCwTYtP7KApFOWuri4fAdgiOpiMsoUpoFKNjMwJsWLUwZOVRLxeJtfDla8N0IXc-rwyATKugqBfUSabvfX3iQB-3mi1PVO28WkIQ22iFhAAONdVX2k6-B6cr1gEA6c1FFWY9M1Co213wbwlVsl_0Iuqo8TDg"
    '''you.png是要下载的图片的名字，必须在项目目录中存在的
       th2.png是上传到服务器之后图片的名字
       you.png是本地待上传的图片名字
       image/png是Content-Type
    '''
    upload_files = {'media': ('th2.png', open('you.png', 'rb'), 'image/png')}
    url = "https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + access_token
    res = requests.post(url, files=upload_files)
    print('url = ', res.json().get('url'))
    assert res.json().get('url') != ""


