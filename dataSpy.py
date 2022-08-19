# -*- coding: UTF-8 -*-

#引入模块
from bilibili_api import sync, search, settings, video 
from collections import OrderedDict
import json
import random
import time

#settings.proxy = "http://ProxyAddress.cat"  # 填写代理地址
#settings.proxy = "http://account:password@ProxyAddress.cat"  # 如果需要账号以及密码


def wait(sec=1):  #“等等陈睿”函数 这里填等待秒或在调用函数时填写 太快会被 -412 拦截
    """
    等等陈睿
        太快会被陈睿 Gank，特此写函数。
    """

    time.sleep(sec)

def videoSearch(kw, pg, printOrNot=True): #视频搜索函数
    """
    搜索函数 kw=关键词（str） pg=页面（int）
    """
    if printOrNot:
        print("搜索视频，关键词“", kw, "”，第", pg, "页。")
    #↓ 调用 API 搜索（由 bilibili-api-python 库提供）赋给结果变量 并返回
    try:
        result = sync(search.web_search(keyword=kw, page=pg))
    except:
        print("连接错误")
    return result

def dataSpy(kw, pg, moreInfomation=False): #数据捉虫函数
    """
    数据捉虫
        此函数用来调取哔哩哔哩搜索 API 的返回 Json。

        此函数具有时效性，至2022年7月30日仍然可用。
    """

    info = videoSearch(kw, pg)  # 获取搜索原始信息
    for a in info['result']:    # 过滤视频搜索结果
        if a["result_type"] == "video":
            videoResult = a["data"]
    ################ 获取一创作者列表
    authorBlackList = []  # 初始化一创作者列表
    with open('authorBlackList.txt', 'r', encoding='UTF-8') as f:
        elements = f.read().split('\n')[:-1]
        for element in elements:
            authorBlackList.append(element)
    f.close()
    ################ 获取一创作者列表
    #print(authorBlackList)
    #authorBlackList = ["EOE组合", "露早GOGO", "米诺高分少女", "莞儿睡不醒", "柚恩不加糖", "虞莫MOMO", "哎呀米诺录播组", "E坨史", "EOE五人团应援会", "壹ちゃン", "墨烧_莞熊电台记者", "露早老公", "烂活机器人", "长崎濑野kira", "我不该拥有炽热的梦", "北安不是北门安保"]
    for i in videoResult:     #处理搜索结果 计算权重
        __weight_random = random.randint(-10, 200)  # 初始化 随机权重
        __weight_like = 0        #初始化 点顶
        __weight_coin = 0        #初始化 投币
        __weight_collect = 0     #初始化 收藏
        __weight_danmaku = 0     #初始化 弹幕
        __weight_author = 0      #初始化 作者
        __weight_sendTime = 0    #初始化 时效
        __weight_click = 0       #初始化 点阅
        __weight_cooperation = 0 #初始化 联合
        __weight_vertical = 0    #初始化 竖屏
        __filter = False         #初始化 过滤
        __weight = 0             #初始化 权重值
        __authorExclude = False  #初始化 排除
        __debug = ""             #初始化 测试变量
        for b in i:           # 遍历  字典
            if b == "title":  # 消除  <em> 关键词标记
                i[b] = i[b].replace('<em class="keyword">', "").replace('</em>', "")
                #print("标题：", i[b])
                __debug = __debug+"标题:"+str(i[b])+"。"
            if b == "pic":  # 加載縮略圖照片
                i[b] = i[b]+"@544w_340h_1c"
            if b == "author": #判定 作者
                for BlackAuthor in authorBlackList:
                    if i[b].find(BlackAuthor) != -1:
                        #print("排除", i[b])
                        #print("已排除并 __authorExclude 设置为真：", i[b])
                        __weight_author = -9765
                        __authorExclude = True
                        __debug = __debug+"作者已排除。"
                    else:
                        pass
            if b == "like":   #权重 计算点顶
                __like = i[b]
                if i[b] <= 900:
                    __weight_like = i[b] * 1.21
                    __debug = __debug+"低顶率。"
                else:
                    __weight_like = i[b] * 0.18
                    __debug = __debug+"高顶率。"
            if b == "favorites":    #权重 计算收藏
                __weight_collect = i[b] * 0.3
                __debug = __debug+"收藏:"+str(i[b])+"。"
            if b == "pubdate":     #权重 计算时效
                __sendTimeCalc = int(int(time.time()) - int(i[b]))/(60*60*24)
                __debug = __debug+"时效:"+str(i[b])+"。"
                if __sendTimeCalc >= 5:  #老的视频 5*24*60*60秒后（五天后）
                    __weight_sendTime = -9345080
                    __debug = __debug+"老视频。"
                    #print("too old")
                if __sendTimeCalc <= 2:  #新的视频
                    #print("New video")
                    __weight_sendTime = 48706
                    __debug = __debug+"更新的视频。"
            if b == "play":         #权重 计算点阅
                if i[b] <= 5000:
                    __weight_click = ( 12 + i[b] ) * 1.2
                    __debug = __debug+"观看很少。"
                elif i[b] <= 30000:
                    __weight_click = ( 9 + i[b] ) * 0.7
                    __debug = __debug+"观看三万内。"
                else:
                    __weight_click = ( 1 + i[b] ) * 0
                    __debug = __debug+"观看过多。"
            if b == "video_review": #权重 计算弹幕
                if i[b] <= 100:
                    __weight_danmaku = i[b] * 0.2
                __debug = __debug+"弹幕:"+str(i[b])+"。"
            if b == "hit_columns":
                if i[b] == ["author"]:
                    __filter = True
            if moreInfomation:
                if b == "aid":
                    videoInfo = sync(video.Video(aid=i[b]).get_info())
                    if videoInfo["copyright"] == 2:
                        __authorExclude = True
                    原 = videoInfo['stat']
                    for 批 in 原:
                        if 批 == 'like':
                            __like = 原[批]
                    for 批 in 原:
                        if 批 == 'coin':
                            if __like <= 原[批]:
                                __weight_coin = 原[批] * 1.4
                            elif i[b] >= 86:
                                __weight_coin = 原[批] * 0.3
                            else:
                                __weight_coin = 原[批]
                    农 = videoInfo['rights']
                    for 批 in 农:
                        if 批 == 'is_cooperation':
                            __weight_cooperation = 200 + (__weight_coin / 2)
                    Ａ = videoInfo['dimension']
                    for 除 in Ａ:
                        if 除 == 'width':
                            __videoWidth = Ａ[除]
                        if 除 == 'height':
                            __videoHeight = Ａ[除]
                    if __videoWidth < __videoHeight:
                        __weight_vertical = -1000

        #↓↓↓↓ 计算权重
        __weight = int(__weight_random + __weight_click + __weight_sendTime + __weight_author + __weight_danmaku + __weight_collect + __weight_coin + __weight_like + __weight_vertical)
        #print("权重值：", __weight)
        # 在视频结果列表中插入权重
        __debug = ""
        i.update({"__weight": __weight, "__filter": __filter, "__authorExclude": __authorExclude, "debug": __debug})
        i = videoResult                  #将缓存中的列表赋给结果 并返回
    return videoResult


def MutiPageResult(keyword, moreInfomation=False):  # 多页结果整合函数
    """
    多页结果整合函数 需要输入关键词（str）
    """

    result = []     #初始化搜索结果列表
    page = videoSearch(keyword, 1, False)["numPages"] #获取页数
    maxPage = 50    #设置最大获取页数，设置更小的值可更快的爬完搜索结果，但是会导致结果不全。
                    #哔哩哔哩最多的结果页数是 50 页，所以请不要大于这个值。不要设置为 1 页，不然什么都不会被获取到。
    page = maxPage if page >= maxPage else page  # 若页数大于 maxPage 页，最大获取 maxPage 页。可在上面设置。
    for i in range(1, page): #遍历搜索的所有页数
        result = result + dataSpy(keyword, i, moreInfomation)
        wait()
    #print(result)
    return result


def makeJson(nameList=["EOE", "露早", "米诺", "莞儿", "柚恩", "虞莫"], moreInfomation=False):  # 制作词典列表函数
    """
    制作词典列表函数
    """
    
    result = []                  #初始化 结果列表
    #nameList = ["EOE", "露早", "米诺", "莞儿", "柚恩", "虞莫"] #初始化 搜索关键词列表
    for i in nameList:           #遍历 搜索关键词列表
        result = result + MutiPageResult(i, moreInfomation)
    Order = OrderedDict()        #初始化 -> 词典排序函数
    for item in result:          #去重 搜索关键词列表
        Order.setdefault(item['bvid'], {**item, }) #设定 为 bvid 去重
    Order = list(Order.values()) #赋值 去重后列表
    result = Order               #赋值 给结果变量
    result.sort(key=lambda x: x["__weight"]) #按权重值排序 从小到大
    result.reverse()             #反向排序
    #del result[-20: -1]          #删除权重值倒数的几个视频
    ################ 获取无关结果关键词列表
    BlockWord = []  # 初始化无关结果关键词列表
    with open('BlockWord.txt', 'r', encoding='UTF-8') as f:
        elements = f.read().split('\n')[:-1]
        for element in elements:
            BlockWord.append(element)
    f.close()
    ################ 获取无关结果关键词列表
    #BlockWord = ["多米诺", "凇子M", "黑猫与白喵", "米诺地尔", "明日方舟早露", "明日方舟", "舒舒酷北北", "贤宝宝Baby", "多米诺骨牌", "微物米诺", "天天打龟", "六弦阁徒_HTT", "街头社区", "艾森巴赫", "撒旦女巫的诱惑", "锤子game", "三千亿光年", "不知所措的周余", "十一点睡粥老师", "少喝运动多奶茶", "tsuiruaku", "战舰世界", "元首的渣渣", "菲尔米诺Bobby", "青衣之冇", "账号注销9999000", "非那米诺", "梦中の游乐园", "坦克世界", "林以恒的小星星", "ZeeNuNew", "无期迷途", "早露", "Alex43801"]
    #↑↑↑↑无关结果关键词 用于排除
    #print("列表长度：",len(result))
    for times in range(0,10): #反复循环过滤 50 遍无关视频 不知道为什么但是确实很有效果
        #print("\n列表长度：", len(result))
        for bL in BlockWord:  #遍历无关视频关键词列表
            #print("排除",bL)
            for i in result:  #对 标题、作者、简介、标签 检查关键词
                if i['title'].find(bL) != -1:
                    try:
                        result.remove(i)
                    except ValueError:
                        pass
                if i['author'].find(bL) != -1:
                    try:
                        result.remove(i)
                    except ValueError:
                        pass
                if i['description'].find(bL) != -1:
                    try:
                        result.remove(i)
                    except ValueError:
                        pass
                if i['tag'].find(bL) != -1:
                    try:
                        result.remove(i)
                    except ValueError:
                        pass
                if i['__filter']:
                    try:
                        result.remove(i)
                    except ValueError:
                        pass
    print("\n\n列表长度：", len(result))
    return result


#此处参考 @Risk2 感谢：https://www.zhihu.com/question/67111152/answer/249259611
#数据写入
result = makeJson(["EOE", "露早", "米诺", "莞儿","柚恩", "虞莫"], True)
#这里第一个参数填写关键词（字符串列表），第二个参数填写是否需要更精确的数据（布尔值），当然也会更慢。
resultJson = open('result.json', 'w', encoding="utf-8")
for i in result:
    json_i = json.dumps(i)
    resultJson.write(json_i+'\n')
resultJson.close()
