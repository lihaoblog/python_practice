#for  else 这表示for循环正常结束而非被跳出才执行else
#random需要import才能用，用法random.randint(1,10)头尾都包括
import  random
print("-" * 50)  #表示打印50次
print("欢迎来到 李 的《猜数游戏》")
print("规则一：系统每次会自动生成一个1~10之间的随机数")
print("规则二：每次游戏最多只能猜三次")
print("规则三：进入游戏或者继续玩，输入：yes或者y")
print("规则三：离开游戏，输入：no或者n")
print("-" * 50)

i=0
while True : #True这样写才对
    order= input('请问是否开始游戏:')
    if order=='yes' or order=='y':
        i+=1
        print(f'这是您的第{i}次游戏')
        number = random.randint(1,10)
        for n in range(1,4,1):
            my_num = int(input('请输入您猜的数字:'))
            if my_num == number :
                print(f'猜对了，答案就是{number},您用了{n}次机会')
                break
            elif my_num > number :
                print(f'猜错了，答案比这个小，您还有{3-n}次机会')
            else:
                print(f'猜错了，答案比这个大，您还有{3-n}次机会')
        else:
            print(f'次数用尽,正确答案是{number}，游戏结束')
    elif order=='no' or order=='n' :
        print('好的，over')
        break
    else:
        print('输入有误，请重新输入')






