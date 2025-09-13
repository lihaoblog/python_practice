#map函数，，有两个参数，一个是函数一个是列表，我们可以用map对列表进行指定函数的处理

lst=[1,2,3,4,5]
print(map(lambda n: n ** 2, lst))  #这个返回的就是一个函数类型
print(list(map(lambda n: n ** 2, lst)))  #加个list表示对map函数的列表输出处理，属于迭代展示



# reduce函数是需要从functools导入的
# 该函数参数是一个必须带俩参数的函数，和一个list列表，主要是做叠加或者叠乘，把前两个值运算的结果再加第三个，如1，2，3是1+2的结果再和3运算
from functools import *
print(reduce(lambda a, b: a + b, lst))   #这个是非迭代展示的，而是算出函数计算结果，所以无需指定展示方式
print(reduce(lambda a, b: a + b, lst,100))  #最后一个参数是初始值，可写可不写，不写默认是0


#写一个查询字符串中相同单词出现次数
str = 'he li hao ni hao a word word ai ni a li hao'
#第一步把该串切开
s1=str.split(' ')
#第二部把切开的字符迭代处理加上我们要运算的数字,只有字典才能item展示
s2=list(map(lambda item:{item:1},s1))
print(s2)
def cunt(dict1,dict2)  :
    key=list(dict2.items())[0][0]
    value=list(dict2.items())[0][1]
    dict1[key]=dict1.get(key,0) + value #get根据键来取值,dict1[key]，得到的也是值
    return dict1

print(reduce(cunt, s2))  #记得调用count不可带（），会按照函数依次运算
print(reduce(cunt, list(map(lambda item:{item:1},str.split(' '))))) #或者高阶函数写法，拿函数当参数


#filter函数，对给定函数判断，留下True的，干掉false的，是个迭代器对象，需要指定展示方法

str=[1,2,3,4,5,6,7,8,9,10,888]
print(filter(lambda n: n % 2 == 0, str))            #不指定返回方式就返回一个函数名
print(list(filter(lambda n: n % 2 == 0, str)))  #需要指定显示方式


# sorted()函数，第一个参数给迭代器，可迭代的字典或者列表，后面跟key指明比较对象 ，要写key=。。
dt=dict([('li',25),('liu',26),('zhang',10),('wu',122)])
print(sorted(dt, key=lambda item: item[0],reverse=True))




