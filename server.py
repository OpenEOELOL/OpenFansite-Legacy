# -*- coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import json, text, html, raw
from bilibili_api import sync, search
import json
from jinja2 import Template, FileSystemLoader, Environment

app = Sanic("EOELOL")
app.static("/src", "./src")
app.static("/assets", "./assets")

templateFolder = FileSystemLoader('./template') #设置 jinja 的模板文件路径
templateEnvironment = Environment(loader=templateFolder) #设置环境
template = templateEnvironment.get_template('main.html')  # 设置模板
templateApi = templateEnvironment.get_template('api.json')  # 设置 API 模板


@app.route("/<page:int>")
@app.get("/")
async def main(request, page=1):
    ################ 获取文件
    videoResult = []
    with open('result.json', 'r') as f:
        StoreList = f.read().split('\n')[:-1]
        for x in StoreList:
            result = json.loads(x)
            videoResult.append(result)
    f.close()
    ################ 获取文件
    pages = page
    pageEnd = pages*50
    pageStart = pageEnd-49

    videoResult = videoResult[pageStart-1:pageEnd]
    HideOrNot = ""
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
                if videoCard[i]:
                    HideOrNot = "ItIsRecoder"
            if i == "play":
                videoPlay = videoCard[i]
            # if i == "coin":
            #     videoCoin = videoCard[i]
            #videoInfo = """<img src="./assets/播放.svg" alt="播放量图标">""" + videoPlay
        data.append({"videoTitle": videoTitle, "av": str(videoAv),
                    "videoCover": videoCover, "videoAuthor": videoAuthor, "HideOrNot": HideOrNot})
        HideOrNot = ""
    if pages == 0:
        data.append({"videoTitle": "【MV】保加利亚妖王AZIS视频合辑",
                    "av": 170001,
                    "videoCover": "https://i2.hdslb.com/bfs/archive/1ada8c32a9d168e4b2ee3e010f24789ba3353785.jpg",
                    "videoAuthor": "Azis"})
        data.append({"videoTitle": "【YYB/MMD】兔女郎米库你喜欢吗？-RBB",
                    "av": 428402381,
                    "videoCover": "https://i0.hdslb.com/bfs/archive/895f1559442de37f78a0d62e755a458955a0a0ba.jpg",
                    "videoAuthor": "修凡ヽBOO"})
    pageNumberIndicator = {"index": page, "previous": page-1, "next": page+1}
    pageResult = template.render(videoResult=data, pageNumber=pageNumberIndicator)
    return html(pageResult)


@app.route("/api/<page:int>")
@app.get("/api")
async def api(request, page=1):
    ################ 获取文件
    videoResult = []
    with open('result.json', 'r') as f:
        StoreList = f.read().split('\n')[:-1]
        for x in StoreList:
            result = json.loads(x)
            videoResult.append(result)
    f.close()
    ################ 获取文件
    pages = page
    pageEnd = pages*20
    pageStart = pageEnd-19

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
        data.append({"videoTitle": "【MV】保加利亚妖王AZIS视频合辑",
                    "av": 170001,
                    "videoCover": "https://i2.hdslb.com/bfs/archive/1ada8c32a9d168e4b2ee3e010f24789ba3353785.jpg",
                    "videoAuthor": "Azis"})
        data.append({"videoTitle": "【YYB/MMD】兔女郎米库你喜欢吗？-RBB",
                    "av": 428402381,
                    "videoCover": "https://i0.hdslb.com/bfs/archive/895f1559442de37f78a0d62e755a458955a0a0ba.jpg",
                    "videoAuthor": "修凡ヽBOO"})
    pageNumberIndicator = {"index": page, "previous": page-1, "next": page+1}
    pageResult = templateApi.render(videoResult=data, pageNumber=pageNumberIndicator)
    return text(pageResult)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, fast=True, auto_reload=True)