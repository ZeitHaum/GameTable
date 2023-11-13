import re
import requests
import datetime

def findFutureContest(string):
    pattren = r"<h2>等你来战</h2>.*?<h2>已结束</h2>"
    pattren = re.compile(pattern=pattren,flags=re.S)
    res = pattren.findall(string=string)
    return res[0]

def NewCoderContestFinder():
    try:
        url = "https://ac.nowcoder.com/acm/contest/vip-index"

        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "referer":"https://ac.nowcoder.com/acm/home/627359730",
        }

        res = requests.get(url=url,headers=headers)
        string = res.text
        string = findFutureContest(string)
        pattren = r"<h4>.*?<a href=\"/acm/contest/(?P<ContestId>.*?)\" target=\"_blank\".*?>(?P<Name>.*?)</a>.*?</h4>.*?<li class=\"match-time-icon\">比赛时间：\s*(?P<Time>.*?)\s*至.*?\(时长:(?P<Length>.*?)\)</li>"
        pattren = re.compile(pattern=pattren,flags = re.S)
        ret = pattren.finditer(string=string)
        retu = []
        for it in ret:
            reti = [it.group("Name"),it.group("Time"),it.group("Length"),it.group("ContestId")]
            ds = datetime.datetime.strptime(reti[1],"%Y-%m-%d %H:%M")
            today = datetime.datetime.today()
            reti[1] = ds.isoformat()
            reti[3] = "Id:"+reti[3]
            if(ds>today):
                retu.append(reti)
        return retu
    except:
        print("更新牛客数据时出现异常!")

if __name__ == "__main__":
    print(NewCoderContestFinder())