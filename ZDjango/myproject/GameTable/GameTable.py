from concurrent.futures import ThreadPoolExecutor,as_completed
import datetime

import ContestFinder.AtCoder as AtCoder
import ContestFinder.CodeForces as CodeForces
import ContestFinder.LeetCode as LeetCode
import ContestFinder.PTA as PTA

class Contest:
    Name = ""
    Time = datetime.datetime.today()
    Length = ""
    OtherInf = ""

    def __init__(self,Name,Time,Length,OtherInf = "")->None:#初始化函数
        self.Name = Name 
        self.Length = Length 
        self.OtherInf = OtherInf
        self.Time = Time

    def __lt__(self,other)->int:
        return self.Time<other.Time

def update():
    print("开始更新比赛日程表")
    #多线程更新
    tp  = ThreadPoolExecutor(max_workers=4)
    #存储所有的运算的线程,守护模式中直接得到返回值
    threads = []
    thri = tp.submit(AtCoder.AtCodeContestFinder)
    threads.append(thri)
    thri = tp.submit(CodeForces.CodeForcesContestFinder)
    threads.append(thri)
    thri = tp.submit(LeetCode.LeetCodeFinder)
    threads.append(thri)
    thri = tp.submit(PTA.PTAFinder)
    threads.append(thri)
    #守护模式结束
    Rets = []
    #判断线程是否结束
    for thri in as_completed(threads):
        Rets.append(thri.result())
    Cts = []
    for Ri in Rets:
        for ri in Ri: 
            Cts.append(Contest(Name= ri[0],Time = datetime.datetime.strptime(ri[1],"%Y-%m-%dT%H:%M:%S"),Length= ri[2],OtherInf=ri[3]))
    Cts.sort()
    toaddlist = []
    for ci in Cts:
        newline = "<tr><td>" + ci.Name +"</td><td>"+ ci.Time.isoformat() +"</td><td>"+ ci.Length +"</td><td>"+ ci.OtherInf+"</td></tr>\n"
        toaddlist.append(newline)
    start_essay = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\"><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>比赛日程表</title>\n</head>")
    #更换为html5的格式
    #add_path = "./templates/GameTable.html"
    '''
    服务器地址
    '''
    add_path = "./GameTable/templates/GameTable.html"
    #添加文件检查逻辑
    with open(add_path,"w",encoding="utf-8") as pt:
        head = start_essay + "\n<body>\n<h1>比赛日程表</h1>\n" + "<p>\n<img src = \"../static/img/fig_cf.png\" width=\"200\"\>\n<img src = \"../static/img/fig_atc.png\" width=\"100\"\>\n<img src = \"../static/img/fig_lc.png\" width=\"150\"\>\n<img src = \"../static/img/fig_pta.png\" width=\"130\"\>\n</p>"
        pt.write(head)
        update = "<p>"+datetime.datetime.now().isoformat()+"更新</p>"
        pt.write(update)
        then = "<table border=\"1\" cellspacing=\"0\"> \n<head>\n<th>比赛名称</th>\n<th>比赛开始时间</th>\n<th>比赛时长(时:分)</th>\n<th>备注信息</th>\n</head>\n"
        pt.write(then)
        for i in toaddlist:
            pt.write(i)
        last = "</table>\n</body>\n</html>\n"
        pt.write(last)
    #print(toaddlist)
    print("更新顺利结束!")


if __name__ == "__main__":
    update()