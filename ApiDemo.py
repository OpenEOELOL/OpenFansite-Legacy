#ApiDemo

import requests

headers = {'Referer': 'https://www.bilibili.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
#设置 Header
for i in range(0, 1000):
    getInfo = requests.get("http://127.0.0.1:8080/apiDynamic/1", headers=headers)
    result = getInfo.json()
    print(result["data"][i]["username"])
