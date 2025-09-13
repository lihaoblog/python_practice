#列表是可以放很多类型的数据，写法lis=[12,'aa',66],可以直接修改
lis =[]
lis =[1,5,'lih','lihao',5,[1,5]]
lis[3]=666

#查找列表数据
print(lis.index('lih'))
print(lis.count(5))
print(len(lis))


#添加列表数据
lis.append('lih8')  #直接添加到尾部
lis.extend('lih8')  #每个字符拆开添加到结尾
lis.insert(5,'1000') #指定位置添加值
print(lis)


#删除
print(lis.pop(3))    #返回删的值并删除，以下标来定位
del lis[1]          #内置的删除语句
lis.remove('lih')   #remove以数值来定位删除
print(lis)

# 排序
lis.reverse()   #逆序
print(lis[::-1])
print(lis)

lis2 =[1,5,12,82,66,-1,55,7,496]
lis2.sort()   #默认从小到大排序
print(lis2)
lis2.sort(reverse=True)   #默认从小到大排序
print(lis2)
for i in lis2:
    print (i,end='-')





