from datetime import date

# datetime五大类。.date/.time/.datetime/.timedelta/.tzinfo
d=date(2025,9, 5 )
d=date.today()   #得到今天的年月日
print(d)    #2025-09-05 格式化输出
print(d.timetuple())   #时间元组输出
print(d.weekday())   #时间元组输出
print(d.isocalendar())  #datetime.IsoCalendarDate(year=2025, week=36, weekday=5)

new_time=d.replace(month=10)   #替换月份呢
print(new_time)
