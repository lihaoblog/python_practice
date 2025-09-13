# time库是处理时间的库，获取系统时间
# 时间戳是从格林威治时间1970年01时01分00秒到现在时间的总秒数，（那个时候北京时间08时，所以叫东八区）

import time


print(time.time())  # 1757052240.1628737

# ctime可以把秒转化成日期，打印具体时间，西方的写法
print(time.ctime())  # Fri Sep  5 14:05:37 2025
print(time.ctime(1757052240.1628737))  # Fri Sep  5 14:04:00 2025

# gmtime()时间元祖输出，可以给后面的这个参数来打印对应的时间，小时对不上，要加八个小时，因为时区不同
print(
    time.gmtime())  # time.struct_time(tm_year=2025, tm_mon=9, tm_mday=5, tm_hour=6, tm_min=7, tm_sec=35, tm_wday=4, tm_yday=248, tm_isdst=0)
print(time.gmtime().tm_year)

# strftime（）格式化转换，转化成你想要的格式，后面跟格式 %Y-%m-%d %H:%M:%S
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(1757052240)))  # 必须是元祖形式，时间戳不行

# strptime()字符串转化时间戳，和上面的strftime相反，转换的时候给的格式必须一致，解析时间
print(time.strptime('2025-09-05','%Y-%m-%d'),'aa')

