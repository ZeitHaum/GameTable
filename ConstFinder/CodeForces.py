import re
import requests
import datetime

def clears(string)->str:
    clpattern = r"[a-z,0-9].*?[\r,\n]"
    clpattern = re.compile(clpattern,flags=re.I)
    toadd = clpattern.findall(string = string)
    toadd = toadd[0]
    toadd = str(toadd)[:-1]
    return toadd


def CodeForcesContestFinder()->list:
    try:
        params = {
            "complete":"true",#补全参数
        }
        url = "https://codeforces.com/contests"

        headers = {
            "referer":"https://codeforces.com/",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
        }

        res = requests.get(url = url,params=params,headers= headers)

        string = res.text#网页源代码

        #正则表达式，根据网页源代码得出
        # pattern = r"<tr\s*data-contestId=\"(?P<ContestId>.*?)\"\s*>\s*<td>(?P<Name>.*?)</td>.*?\
        # <td .*?>.*?</td>.*?<td>.*?<span .*?>(?P<Time>.*?)</span>.*?</td>.*?<td>(?P<Length>.*?)</td>.*?</tr>"

        pattern = r"Current or upcoming contests.*?<script type=\"text/javascript\">"#第一遍过滤

        pattern = re.compile(pattern = pattern,flags= re.S)
        ret = pattern.finditer(string= string)
        substring = ""
        for it in ret:
            substring = it.group()
        #print(substring)
        res.close()

        #正则表达式，根据网页源代码得出
        pattern = r"<tr\s*data-contestId=\"(?P<ContestId>\d+)\"\s*>\s*<td>(?P<Name>.*?)</td>.*?<td>.*?<span class=.*?>(?P<Time>.*?)</span>.*?</td>.*?<td>(?P<Length>.*?)</td>.*?</tr>"
        pattern = re.compile(pattern=pattern,flags = re.S)
        ret = pattern.finditer(string = substring)

        retu = []
        for it in ret:
            #前后清理多余空格和换行
            reti = []
            keys = ["Name","Time","Length","ContestId"]
            for ki in keys:
                string = it.group(ki)
                reti.append(clears(string = string+"\r"))
            #压入返回列表中
            retu.append(reti)
        #标准化数据
        for ri in retu:
            ds = datetime.datetime.strptime(ri[1],"%b/%d/%Y %H:%M")
            ds = ds + datetime.timedelta(hours=5)#不要使用replace
            ri[1] = ds.isoformat()
            ri[3] = "ContestId:" + ri[3]
        return retu
    except:
        print("更新CodeForces数据时出现异常!")


if __name__ == "__main__":
    print(CodeForcesContestFinder())


