# id函数可以查物理地址
# 变量不可以以数字开头，不能关键字，区分大小写；


num = 5
print(id(num))
print(type(num))
num:float = 0.5  # 指定类型。
tuple(num) #转元组 list转列表
a1, a2 = 100, 200
a1 = a2 = 100

# python类型有三大类：数值，容器和其他，顾名思义，容器就是数组，字符串列表元组啥的装一堆东西。