#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Rain'
__time__ = ''17-4-14'
__Descriptions__ = '引导界面广告设置'

        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +
"""
import json

import requests
from _dbus_bindings import String

from config import Constant
from url import Url


def showInfo():
    content = ""
    resultJson = requests.get(Url.splash_advert_url, data=None, json=None, headers=Constant.headers)
    data = json.loads(resultJson.text)
    for advertInfo in data["results"]:
        content += advertInfo["objectId"] + "\t"
    return content


print("======== 引导界面广告设置 ========\n")
print("使用说明：(输入数字1-3) \n指令1：引导界面广告添加\t 指令2：引导界面广告修改\t 指令3：引导界面广告删除\n")
print("=================================")
print("当前广告信息ID：%s" % showInfo())
print("=================================\n")

code = input("请输入执行指令：")


def show(code):
    if code == '1':
        content = "引导界面广告添加"
        return content

    elif code == '2':
        content = "引导界面广告修改"
        return content

    elif code == '3':
        content = "引导界面广告删除"
        return content

    else:
        return (input("请输入正确执行指令："))


print('您此次操作为：%s' % show((code)))


def addAdvert():
    url = input("请设置广告Url链接：")
    picture = input("请设置广告展示图片链接：")

    body = {'url': (String)(url), 'picture': (String)(picture)}
    result = requests.post(Url.splash_advert_url, data=None, json=body, headers=Constant.headers)
    print("返回数据：", result.text)

def modifyAdvert():
    advertId = input("请输入需要修改的广告ID：")
    url = input("请设置新的广告Url链接：")
    picture = input("请设置新的广告展示图片链接：")

    body = {'url': (String)(url), 'picture': (String)(picture)}
    result = requests.put(Url.splash_advert_url + advertId, data=None, json=body, headers=Constant.headers)
    print("返回数据：", result.text)

def removeAdvert():
    advertId = input("请输入需要删除的广告ID：")

    result = requests.delete(Url.splash_advert_url + advertId, headers=Constant.headers)
    print("返回数据：", result.text)

if code == '1':  # 添加
    addAdvert()
elif code == '2':  # 修改
    modifyAdvert()
elif code == '3':  # 删除
    removeAdvert()