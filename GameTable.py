from concurrent.futures import ThreadPoolExecutor,as_completed
import ConstFinder.AtCoder as AtCoder
import ConstFinder.CodeForces as CodeForces
import ConstFinder.LeetCode as LeetCode
import ConstFinder.PTA as PTA
import ConstFinder.NewCoder as NewCoder
import ConstFinder.LuoGu as LuoGu
import datetime
import operator
import csv

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

if __name__ == "__main__":
    print("开始更新比赛日程表")
    #多线程更新
    tp  = ThreadPoolExecutor(max_workers=4)
    #存储所有的运算的线程,守护模式中直接得到返回值
    threads = []
    thri1 = tp.submit(AtCoder.AtCodeContestFinder)
    threads.append(thri1)
    thri2 = tp.submit(CodeForces.CodeForcesContestFinder)
    threads.append(thri2)
    thri3 = tp.submit(LeetCode.LeetCodeFinder)
    threads.append(thri3)
    thri4 = tp.submit(PTA.PTAFinder)
    threads.append(thri4)
    thri5 = tp.submit(NewCoder.NewCoderContestFinder)
    threads.append(thri5)
    thri6 = tp.submit(LuoGu.LuoGuContestFinder)
    threads.append(thri6)
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
    with open("ContestTable.csv","w",encoding="utf-8",newline="") as f:#导出csv
        csvwriter = csv.writer(f)
        thisrow = ["比赛名称","比赛开始时间","比赛时长","备注信息"]
        csvwriter.writerow(thisrow)
        for i in range(len(Cts)):
            csvwriter.writerow([Cts[i].Name,Cts[i].Time.isoformat(),Cts[i].Length,Cts[i].OtherInf])
    for ci in Cts:
        newline = "<tr><td>" + ci.Name +"</td><td>"+ ci.Time.isoformat() +"</td><td>"+ ci.Length +"</td><td>"+ ci.OtherInf+"</td></tr>\n"
        toaddlist.append(newline)
    with open("GameTable.html","w",encoding="utf-8") as pt:
        head = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>比赛日程表</title>\n</head>\n<body>\n<h1>比赛日程表</h1>\n"
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



