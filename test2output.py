# -*- coding: UTF-8 -*-
import json
#此处参考 @Risk2 感谢：https://www.zhihu.com/question/67111152/answer/249259611
def main():
    ################ 获取文件
    videoResult = []
    with open('result.json', 'r') as f:
        StoreList = f.read().split('\n')[:-1]
        for x in StoreList:
            result = json.loads(x)
            videoResult.append(result)
    f.close()
    ################ 获取文件
    for i in videoResult:
        for b in i:
            print(b,i[b])


main()