# timedelta 是一个日期运算函数，最高的值是天，也就是说只能运算天的加减

from datetime import timedelta ,datetime

td= timedelta(days=10,hours=5)  #10 days, 5:00:00
print(td)


# 里面的参数放最大为天的，正负表前后
td_dt=datetime.now()+timedelta(hours=10)
print(td_dt)

start='2025-09-06 09:48:55'
end='2025-10-01 01:01:01'
t1=datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
t2=datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
print((t2-t1).days,(t2-t1).seconds)