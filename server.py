# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import json, text, html, raw
from bilibili_api import sync, search
import json as theJson
from jinja2 import Template, FileSystemLoader, Environment

app = Sanic("EOELOL")
app.static("/src", "./src")
app.static("/assets", "./assets")

templateFolder = FileSystemLoader('./template') #设置 jinja 的模板文件路径
templateEnvironment = Environment(loader=templateFolder) #设置环境
templateApi = templateEnvironment.get_template('api.json')  # 设置 API 模板

@app.route("/api/<page:int>")
@app.get("/api")
async def api(request, page=-1):
    ################ 获取文件
    videoResult = []
    with open('result.json', 'r') as f:
        StoreList = f.read().replace("\\", "\\\\").split('\n')[:-1]
        for x in StoreList:
            result = theJson.loads(x)
            videoResult.append(result)
    f.close()
    ################ 获取文件
    setOnePageHowManyCardYouNeedLoad = 20  # 设置一页加载多少个卡片来展示？
    pages = page
    pageEnd = pages*setOnePageHowManyCardYouNeedLoad
    pageStart = pageEnd-(setOnePageHowManyCardYouNeedLoad-1)
    maxPage = int((len(videoResult)-1) / setOnePageHowManyCardYouNeedLoad + 1)

    videoResult = videoResult[pageStart-1:pageEnd]

    videoList = videoResult
    data = []
    
    for videoCard in videoList:
        for i in videoCard:
            if i == "title":
                videoTitle = videoCard[i]
            if i == "aid":
                videoAv = videoCard[i]
            if i == "pic":
                videoCover = videoCard[i]
            if i == "author":
                videoAuthor = videoCard[i]
            if i == "__authorExclude":
                __authorExclude = videoCard[i]
            if i == "play":
                videoPlay = videoCard[i]
            # if i == "coin":
            #     videoCoin = videoCard[i]
            #videoInfo = """<img src="./assets/播放.svg" alt="播放量图标">""" + videoPlay
        data.append({"videoTitle": videoTitle, "av": str(videoAv),
                    "videoCover": videoCover, "videoAuthor": videoAuthor, "HideOrNot": __authorExclude})
    if pages == 0:
        data = []
        data.append({"videoTitle": "【MV】保加利亚妖王AZIS视频合辑",
                    "av": 170001,
                    "videoCover": "https://i2.hdslb.com/bfs/archive/1ada8c32a9d168e4b2ee3e010f24789ba3353785.jpg",
                    "videoAuthor": "Azis"})
        data.append({"videoTitle": "【YYB/MMD】兔女郎米库你喜欢吗？-RBB",
                    "av": 428402381,
                    "videoCover": "https://i0.hdslb.com/bfs/archive/895f1559442de37f78a0d62e755a458955a0a0ba.jpg",
                    "videoAuthor": "修凡ヽBOO"})
    if pages == -1:
        data = []
        data.append({"videoTitle": "Hey! Look at here! You don't set any parameter at this url. You need set a page number at URL bottom. Like this /api/<page:int>",
                    "av": 170001,
                    "videoCover": "",
                    "videoAuthor": ""})
    if pages > maxPage:
        data = []
        data.append({"videoTitle": "No More 没有更多了",
                    "av": 170001,
                    "videoCover": "",
                    "videoAuthor": "no_more"})
    pageNumberIndicator = {"index": page, "previous": page-1, "next": page+1}
    pageResult = theJson.loads(templateApi.render(videoResult=data, pageNumber=pageNumberIndicator))
    return json(pageResult)

@app.route("/apiDynamic/<page:int>")
@app.get("/apiDynamic")
async def api(request, page=-1):
    ################ 获取文件
    dynamicResult = []
    with open('resultDynamic.json', 'r') as f:
        StoreList = f.read().replace("\\", "\\\\").split('\n')[:-1]
        for x in StoreList:
            result = theJson.loads(x)
            dynamicResult.append(result)
    f.close()
    ################ 获取文件
    setOnePageHowManyCardYouNeedLoad = 20  # 设置一页加载多少个卡片来展示？
    pages = page
    pageEnd = pages*setOnePageHowManyCardYouNeedLoad
    pageStart = pageEnd-(setOnePageHowManyCardYouNeedLoad-1)
    maxPage = int((len(dynamicResult)-1) / setOnePageHowManyCardYouNeedLoad + 1)

    dynamicList = dynamicResult[pageStart-1:pageEnd]

    pageResult = {"problem": "no_problem", "page": page, "data": dynamicList}
    if pages == -1:
        pageResult = {"problem": "wrong_page", "page": page, "data": [
            {"username": "Hey! Look at here! You don't set any parameter at this url. You need set a page number at URL bottom. Like this /apiDynamic/<page:int>", "userid": 0, "firstPicture": "", "dynamicID": 0}]}
    if pages > maxPage:
        pageResult = {"problem": "no_more", "page": page, "data": [
            {"tips": "No more"}]}
    return json(pageResult)

@app.route("/search/<page:str>")
@app.get("/search")
async def apiSearch(request, page=-1):
    ################ 获取文件
    dynamicResult = []
    with open('resultDynamic.json', 'r') as f:
        StoreList = f.read().replace("\\", "\\\\").split('\n')[:-1]
        for x in StoreList:
            result = theJson.loads(x)
            dynamicResult.append(result)
    f.close()
    ################ 获取文件
    setOnePageHowManyCardYouNeedLoad = 20  # 设置一页加载多少个卡片来展示？
    pages = page
    pageEnd = pages*setOnePageHowManyCardYouNeedLoad
    pageStart = pageEnd-(setOnePageHowManyCardYouNeedLoad-1)
    maxPage = int((len(dynamicResult)-1) / setOnePageHowManyCardYouNeedLoad + 1)

    dynamicList = dynamicResult[pageStart-1:pageEnd]

    pageResult = {"problem": "no_problem", "page": page, "data": dynamicList}
    if pages == -1:
        pageResult = {"problem": "wrong_page", "page": page, "data": [
            {"username": "Hey! Look at here! You don't set any parameter at this url. You need set a page number at URL bottom. Like this /apiDynamic/<page:int>", "userid": 0, "firstPicture": "", "dynamicID": 0}]}
    if pages > maxPage:
        pageResult = {"problem": "no_more", "page": page, "data": [
            {"tips": "No more"}]}
    return json(pageResult)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, fast=True, auto_reload=True)