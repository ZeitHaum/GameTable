'''
PTA一般只有520争霸赛和跨年挑战赛.
'''

import datetime

def PTAFinder()->list:
    try:
        today = datetime.date.today()
        if(today.month>5 or (today.month==5 and today.day>20)):
            next520 = datetime.date(year=today.year+1,month=5,day=20)
        else:
            next520 = datetime.date(year=today.year,month=5,day=20)
        if(today.month == 1 and today.day == 1):
            nextnewyear = datetime.date(year=today.year,month=1,day = 1)
        else:
            nextnewyear = datetime.date(year=today.year+1,month=1,day = 1)
        LENGTH = "N/A"
        name1 = "PTA520钻石争霸赛"
        name2 = "PTA跨年挑战赛"
        ret = []
        if today.month == 5:
            ret.append([name1,next520.isoformat() + "T00:00:00",LENGTH])
        if today.month == 12:
            ret.append([name2,nextnewyear.isoformat() + "T00:00:00",LENGTH,""])
        return ret
    except:
        print("更新PTA数据时出现异常!")

if __name__ == "__main__":
    print(PTAFinder())

