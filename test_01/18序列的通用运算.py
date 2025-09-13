# 序列可以+-*/
s1='1235'+'56789'  #字符串只能字符串类型,类型不同会报错，数据正常运算
s1=1122+355
print(s1)

lis=[1,2,89,'aaa',['s','sss']]
lis=lis+[4,5]  #也可以用+=
print(lis)

lis2=[lis*10]  #乘法是打印多少遍
print(lis2)

s2='hello word'
print(max(s2))  #max和min是把这些都拆开比较大小的

