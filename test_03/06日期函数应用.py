#1.计算日期是本年的第多少天
from datetime import datetime,date,timedelta

dt=input('请输入你要计算的时间，年月日格式不用隔开：')

stm=datetime.strptime(dt,'%Y%m%d')
print(stm)


# 方法1
#strftime的参数%j是计算今年第几天的参数
days=stm.strftime('%j')
print(f'你输入的{dt}是{stm.year}年的第{days}天')

# 方法2
# 时间戳格式也有一个tm_yday
days1=stm.timetuple().tm_yday
print(days1)




#2计算上个月的最后一天的日期
result = date(year=stm.year,month=stm.month,day=1)
last_monthday=result + timedelta(days=-1)
print(last_monthday)