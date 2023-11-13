'''
力扣比赛较为固定，一般分为单周赛和双周赛。
单周赛固定在每周日的上午10:30 - 12:00.双周赛时间为双周六的晚上22:30 - 0:00.
'''

import datetime

def DatetimeChangeToIso(timeArg,dateArg)->str:
    dt = datetime.datetime(
        year= dateArg.year,
        month= dateArg.month,
        day= dateArg.day,
        hour = timeArg.hour,
        minute= timeArg.minute
    )
    return dt.isoformat()

def FindRelativeCnt()->list:
    weekcnt = 299
    doubleweekcnt = 81
    standarddate1 = datetime.datetime(year = 2022,month = 6,day = 26) 
    standarddate2 = datetime.datetime(year = 2022,month = 6,day = 25)
    today = datetime.datetime.today()
    delta1 = int(((today-standarddate1).days-1)/7)
    delta2 = int(((today-standarddate2).days-1)/14)
    return [weekcnt+delta1,doubleweekcnt+delta2]#理解-1的作用

def LeetCodeFinder()->list:
    try:
        today = datetime.date.today()
        weekgame1 = datetime.timedelta(days= 7 - today.isoweekday())+today#最近的一场周赛
        weekgame2 = datetime.timedelta(days= 14 - today.isoweekday())+today#次近的一场周赛
        doubleweekgame = datetime.timedelta(days= (13 - today.isoweekday())%7 + 7) + today #最近的一场双周赛
        time1 = datetime.time(hour=10,minute=30)
        time2 = datetime.time(hour=22,minute=30)
        LENGTH = "01:30"
        Sequence = FindRelativeCnt()
        #注意余项含义
        Name1 = f"LeetCode第{Sequence[0]+1}场周赛"
        Name2 = f"LeetCode第{Sequence[0]+2}场周赛"
        Name3 = f"LeetCode第{Sequence[1]+1}场双周赛"
        Name = [Name1,Name2,Name3]
        Time = [DatetimeChangeToIso(timeArg=time1,dateArg=weekgame1),
            DatetimeChangeToIso(timeArg=time1,dateArg=weekgame2),
            DatetimeChangeToIso(timeArg=time2,dateArg=doubleweekgame),
        ]
        ret = []
        for i in range(3):
            ret.append([Name[i],Time[i],LENGTH,""]) 
        return ret
    except:
        print("更新LeetCode数据时出现异常!")

if __name__ == "__main__":
    print(LeetCodeFinder())
    