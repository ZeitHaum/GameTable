import re
from time import time 
import requests
import datetime

def AtCodeContestFinder()->list:
    try:
        url = "https://atcoder.jp/contests/"                                                              

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
            "cookie":"_ga=GA1.2.1189320787.1651659192; REVEL_FLASH=; _gid=GA1.2.23145984.1656170181; timeDelta=-945; REVEL_SESSION=1d5b60e333d98c9e0b10b0aa0bbd66ee825040ad-",
        }

        resp = requests.get(url = url,headers = headers)
        string = resp.text
        resp.close()
        pattern = r"<div id=\"contest-table-upcoming\">.*?</table>"
        pattern = re.compile(pattern= pattern,flags = re.S)
        ret = re.finditer(pattern= pattern,string = string)
        for it in ret:
            substring = it.group()#第一次筛取

        pattern = r"<tr>.*?<time class='fixtime fixtime-full'>(?P<Time>.*?)</time>.*?<a href=\".*?\">(?P<Name>.*?)</a>.*?<td class=\"text-center\">(?P<Length>.*?)</td>.*?</tr>"

        pattern = re.compile(pattern= pattern,flags = re.S)
        ret = pattern.finditer(string = substring)
        retu = []
        for it in ret:
            retu.append([it.group("Name"),it.group("Time"),it.group("Length"),""])
        #标准化数据
        for ri in retu:
            ds = datetime.datetime.strptime(ri[1],"%Y-%m-%d %H:%M:%S+0900")
            ds = ds + datetime.timedelta(hours=-1)#不要使用replace
            ri[1] = ds.isoformat()
        return retu
    except:
        print("更新AtCoder数据时出现异常!")

if __name__ == "__main__":
    print(AtCodeContestFinder())