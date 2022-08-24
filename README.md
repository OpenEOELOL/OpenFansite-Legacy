# OpenFansite 高级版前端分支

![EOE.LOL 图标](./EOELOL.png)

开源二创推送站点。

## 关于 OpenFansite

OpenFansitePro-Api 是一个高定制性的哔哩哔哩视频推荐解决方案，使用高性能服务器 Sanic 提供 API 服务。

### 特点

- **开发者友好的 API**，特意设计的 API 随处可用，可开发配套 App。

## 使用

1. Fork 一份代码
2. 在终端执行 ` pip install -r requirements.txt ` 安装必要的库。
3. 修改 ` dataSpy.py ` 里的代码，对搜索关键词、搜索页数、无关搜索结果、一创作者名单等进行调整。
4. 使用 ` crontab ` 命令定时对 ` dataSpy.py ` 执行。或立即执行，执行后会生成 ` result.json ` 文件。请不要动它。
5. 执行 ` server.py ` 文件或在终端执行 ` sanic server.app ` 来启动 API。**

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
