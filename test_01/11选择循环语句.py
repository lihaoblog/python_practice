#因为python里面的if语句没有括号，所以都是以缩进来表示范围，属于该if的就缩进一次，多次if多次缩进，否则和该if平行的就是另一个elif
#
age = int(input('please input your age:'))  #python中input输入的都是字符串，所以别的类型要转义

if 0<age<=18:
    print('未成年')
elif 18<age<60:
    print('中年')
else:
    print('old')

#三目运算符：
num=int(input('what is num:'))
result = f'{num}是偶数' if num%2==0 else f'{num}是奇数'  #条件后写，if在判定后面
print(result)
