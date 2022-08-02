# OpenFansite
开源二创推送站点

## 关于 OpenFansite
OpenFansite 是一个高定制性的哔哩哔哩视频推送网站服务。通过设置关键词给用户推送合适喜好的视频内容。本服务是高度可控的，通过高性能服务器 Sanic 提供网页服务。

### 优点
- **迅速**，通过使用高性能服务器软件 Sanic 给用户提供服务。
- **界面优美**，由 KurisuCat 手搓的 CSS，以及他的 *独特的审美（相较他自己而言）* 对 UI 的把控。
- **简单操作**，对*任何人*都易用的软件，通过对无障碍优化以及直观的交互让每个人都能轻松使用。

### 缺点
- **很慢**，尚未使用异步操作对速度进行优化。
- **界面简陋**，通过对 YouTube 的界面抄袭以及不知道从哪儿抄过来的代码进行缝合。
- **引用私人服务器**，通过对 KurisuCat 的服务器连接可能会获取到用户的部分数据。

## 使用
1. Fork 一份代码
2. 在终端执行 `pip install -r requirements.txt` 安装必要的库。
3. 修改 `dataSpy.py` 里的代码，对搜索关键词、搜索页数、无关搜索结果、一创作者名单等进行调整。
4. 使用 `crontab` 命令定时对 `dataSpy.py` 执行。或立即执行，执行后会生成 `result.json` 文件。请不要动它。
5. 执行 `server.py` 文件或在终端执行 `sanic server.app` 来启动站点。
6. 访问 `http://127.0.0.1:8080` 打开站点。**完成！**

## 协议
采用 [CC-BY-SA-4.0](https://github.com/OpenEOELOL/OpenFansite/blob/main/LICENSE)，使用时请遵守。
