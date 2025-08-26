name = 'li'
age = 29
salary = 100000

# 输出格式必须要用下面这种，%（）括号里面给多个值
print('my name is %s,my age is %d'% (name,age))


brithday = 06.03
money = 5202012.555563
# 给的整数位数就算不够，也会整数输出，以免值改变
# 给的小数截断很有可能会不四舍五入，这是因为二进制误差导致。
# 必须要有小数点，不用逗号隔开，%和变量之间有没有空格都无所谓
print('my money is %3d,my brithday is %.1f'% (money,brithday))

fnum=22.3456
print('my fnum is %.2f'%fnum,end='aa')

# 精确使用四舍五入要用到类decimal
from decimal import Decimal
Decimal(fnum)
print(Decimal(fnum))
print(Decimal(str(fnum)).quantize(Decimal('0.00'),rounding='ROUND_HALF_UP'))


#第二种格式化输出f+字符串形式，对于没有对变量再次处理的好用，上面的截断就不能

print (f'my name is {name},my age is {age+1}+20')
