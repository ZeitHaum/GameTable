import re
from xml.etree.ElementTree import tostring
import requests
import datetime


def LuoGuContestFinder():
    try:
        url = "https://www.luogu.com.cn/"
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
        }
        res = requests.get(url = url,headers = headers)
        string = res.text
        # print(string)
        # pattern = r"<a href=\"/contest/.*?\">(?P<Name>.*?)</a>.*?<strong class=\".*?\">(?P<Status>.*?)</strong>.*?<a class=\'.*?\' href=\".*?\" target=\"_blank\">(?P<MoreInf>.*?)</a>.*?<span class=\"lg-samll .*?\">(?P<Time>.*?)<br>(?P<EndTime>.*?)</span>.*?</div>"
        pattern = r"<a href=\"/contest/.*?\">(?P<Name>.*?)</a>.*?<strong class=\".*?\">(?P<Status>.*?)</strong>.*?<a class=\'.*?\' href=\".*?\" target=\"_blank\">(?P<MoreInf>.*?)</a>.*?<span class=\"lg-small lg-inline-up lg-right lg-md-hide\">(?P<Time>.*?)<br>(?P<EndTime>.*?)</span>.*?</div>"
        pattern = re.compile(pattern,re.S)
        res = pattern.finditer(string)
        # res2 = pattern.findall(string)
        # print(res2)
        retu = []
        # print(res)
        # print(1)
        for it in res:
            # print(it.group())
            # # print(1)
            if(it.group("Status")=="已结束"):
                continue
            reti = [it.group("Name"),it.group("Time"),"",it.group("MoreInf")]
            reti[0] = reti[0][1:-1]
            ds = datetime.datetime.strptime(reti[1],"\n%m-%d %H:%M")
            now = datetime.datetime.now()
            ds = ds.replace(year = int(now.year))
            reti[1] = ds.isoformat()
            EndTime = it.group("EndTime")       
            de = datetime.datetime.strptime(EndTime,"\n%m-%d %H:%M ")
            de = de.replace(year=ds.year)
            dt = de - ds
            reti[2] = dt.__str__()
            reti[2] = reti[2][:-3]
            reti[3] = "出题:"+reti[3]
            retu.append(reti)
        return retu
    except:
        print("更新洛谷数据出现异常!")
if __name__ == "__main__":
    print(LuoGuContestFinder())

