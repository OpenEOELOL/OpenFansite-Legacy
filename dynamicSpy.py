# -*- coding: UTF-8 -*-

#引入模块
from bilibili_api import sync, search, settings, video
from collections import OrderedDict
import json
import random
import time
import requests

headers = {'Referer': 'https://www.bilibili.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

#settings.proxy = "http://ProxyAddress.cat"  # 填写代理地址
#settings.proxy = "http://account:password@ProxyAddress.cat"  # 如果需要账号以及密码


def wait(sec=1):  # “等等陈睿”函数 这里填等待秒或在调用函数时填写 太快会被 -412 拦截
    """
    等等陈睿
        太快会被陈睿 Gank，特此写函数。
    """

    time.sleep(sec)


def getDynamic(keyword, offset=None, printOrNot=False):
    """
    传入一个关键词来获取一个动态数据
    """
    global headers
    if offset == None:
        params = {"topic_name": keyword, "sortby": 2}
        if printOrNot:
            print("正在打印“", keyword, "”。无偏移值")
    else:
        params = {"topic_name": keyword, "sortby": 2, "offset": offset}
        if printOrNot:
            print("正在打印“", keyword, "”。偏移值", offset)
    getInfo = requests.get(
        "http://api.vc.bilibili.com/topic_svr/v1/topic_svr/fetch_dynamics", headers=headers, params=params)
    result = getInfo.json()
    return result

def getRawData(keyword="", pages=1, printOrNot=False):
    offset = None
    result = []
    for i in range(1,pages+1):
        if printOrNot:
            print("获取第{}页".format(i))
        pendingData = getDynamic(keyword, offset=offset, printOrNot=printOrNot)
        data = pendingData["data"]["cards"]
        theNextStart = pendingData["data"]["offset"]
        offset = theNextStart
        result = result + data
        if pendingData["data"]["has_more"] == 0:
            if printOrNot:
                print("nomore")
            break
        wait()
    return result

def makeResultJsonFriendly(keyword="", pages=1, printOrNot=False):
    pendingData = getRawData(keyword=keyword, pages=pages, printOrNot=printOrNot)
    data = []
    for i in pendingData:
        cardJson = json.loads(i["card"])
        if "item" in cardJson:
            data.append({"username": cardJson["user"]["name"],
                        "userid": cardJson["user"]["uid"],
                        #"content": cardJson["item"]["description"],
                        "firstPicture": cardJson["item"]["pictures"][0]["img_src"],
                        "dynamicID": i["desc"]["dynamic_id"]
            })
    return data


def MutiDataSpy():
    pendingData = {}
    ################ 获取关键词列表
    KeyWords = []  # 初始化关键词列表
    with open('keyWord.txt', 'r', encoding='UTF-8') as f:
        elements = f.read().split('\n')[:-1]
        for element in elements:
            KeyWords.append(element)
    f.close()
    ################ 获取关键词列表

print(makeResultJsonFriendly(keyword="eoe", pages=1, printOrNot=False))
