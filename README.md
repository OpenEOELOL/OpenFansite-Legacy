# OpenFansite 高级版 API 分支

开源二创推送 API。

## 关于 OpenFansite

OpenFansitePro-Api 是一个高定制性的哔哩哔哩视频推荐解决方案，使用高性能服务器 Sanic 提供 API 服务。

### 特点

- **开发者友好的 API**，特意设计的 API 随处可用，可开发配套 App。

## 使用

1. 克隆代码
2. 执行 ` pip install -r requirements.txt ` 安装必要的库
3. 修改 `authorBlackList.txt` 来增删改一创、录播man以及切片man。投转载的视频将会自动标记为录播或切片。
4. 修改 `BlockWord.txt` 来增删改无关关键词，这些关键词将直接在结果里删除，无论开关隐藏录播或切片
5. 修改 `keyWords.txt` 来增删改搜索关键词
6. *必要时*修改 `dataSpy.py`，尤其是 `makeJson(nameList, moreInfomation)` 函数，第二个参数 `moreInfomation` 如果设置为**真**的话可能会增加大约 15 分钟的扫描时间，请酌情开启，默认为开启
7. 使用 ` crontab ` 命令定时对 ` dataSpy.py ` 执行，或立即执行，执行后会生成 ` result.json ` 文件，请不要动它。执行时间大约为 30 分钟。
8. 执行 ` server.py ` 文件或在终端执行 ` sanic server.app ` 来启动 API

## 协议

采用 [CC-BY-SA-4.0](https://github.com/OpenEOELOL/OpenFansite/blob/main/LICENSE)，使用时请遵守。

## 致谢

- E 个魂儿们
- EOE 工具人们
- 虞莫、柚恩、露早、莞儿、米诺，五人。
- 贡献者们
- 我的家人
- Google、Stack Overflow、 菜鸟教程等网站
- AsAsFans
- 我喜欢的人
- 我的朋友
- 还有你们 🥰
