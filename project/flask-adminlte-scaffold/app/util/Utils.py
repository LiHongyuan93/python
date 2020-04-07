# -*- coding: utf-8 -*-

import html
import json
import logging
from urllib.parse import unquote
from flask import Response

## alert加跳转
from app.models import BaseModel
logging.basicConfig(level=logging.INFO)

def show_alert(str,url):
    return "<script>alert('"+str+"');window.location.href='"+url+"';</script>"

## URL解码
def urldecode(raw_str):
    return unquote(raw_str)


# HTML解码
def html_unescape(raw_str):
    return html.unescape(raw_str)

## 字符串转字典
def str_to_dict(dict_str):
    if isinstance(dict_str, str) and dict_str != '':
        new_dict = json.loads(dict_str)
    else:
        new_dict = ""
    return new_dict

# 字典转对象
def dict_to_obj(dict, obj, exclude=None):
    for key in dict:
        if exclude:
            if key in exclude:
                continue
        setattr(obj, key, dict[key])
    return obj


# peewee转dict
def obj_to_dict(obj, exclude=None):
    dict = obj.__data__
    if exclude:
        for key in exclude:
            if key in dict: dict.pop(key)
    return dict

# 成功返回
def resp_success(obj=None,msg='成功'):
    #状态码
    result= {'data': obj, 'code': 1,'msg':msg}
    json_resp =  json.dumps(result,cls=DateEncoding)
    response=Response(json_resp, mimetype='application/json', status=200)
    return response

# 失败返回
def resp_failure(msg='失败',obj=None,status=500):
    #状态码
    result= {'data': obj, 'code': 0 ,'msg':msg}
    json_resp =  json.dumps(result,cls=DateEncoding)
    return Response(json_resp, mimetype='application/json', status=status)

#将model对象转换为dict再进行序列化
class DateEncoding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseModel):
            return obj_to_dict(o)
