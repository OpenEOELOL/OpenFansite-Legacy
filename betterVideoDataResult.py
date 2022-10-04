def cleanShitKey(videoResult):
    result = []
    for i in videoResult:
        videoInfo = {}
        for b in i: 
            if b == "title":
                videoInfo.update({"title": i[b]})
            if b == "aid":
                videoInfo.update({"aid": i[b]})
            if b == "pic":
                videoInfo.update({"pic": i[b]})
            if b == "author":
                videoInfo.update({"author": i[b]})
            if b == "__authorExclude":
                videoInfo.update({"__authorExclude": i[b]})
        result.append(videoInfo)
    return result
