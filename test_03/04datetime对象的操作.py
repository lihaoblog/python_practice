from datetime import datetime

#年月日时分秒
dt=datetime(2025,10,9,15,50,55,2)
print(dt)
dt2=datetime.now()
print(dt2)
print(dt2.timetuple())
print(dt2.timetuple().tm_mon)
dt3=dt2.strftime('%Y年%m月%d日 %H:%M:%S')  #指定格式转化字符串
print(dt3)

#返回的日期类型，time库里面是元祖类型
dt3=datetime.strptime(dt3,'%Y年%m月%d日 %H:%M:%S')  #字符串转成datetime类型，可运算
print(dt3,'aa')


dt4=dt2.utcnow()  #弃用，通用时区
# dt4=datetime.now(datetime.UTC)
print(dt4,'北京时间')

#时间戳
print(dt2.timestamp(),'时间戳')
