#用生成器写一个取质数的函数，用yield
import math
from math import sqrt


def my_prime():
    i=2
    yield i
    while True:
        i+=1
        for j in range(2,math.ceil(sqrt(i))+1):
            if i%j==0:
                break
        else:
            yield i

if __name__=='__main__':
    g=my_prime()
#要用next来调用,num代表每次调用获取的值
    count=0
    num=next(g)
    while num<100:
        print(num)
        num = next(g)
        count+=1
    print(f'一共有{count}个质数')


