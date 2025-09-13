#面向函数编程，是指一个个函数的编程，一切皆函数，比如高阶函数
#面向对象编程，所有皆是对象，一个个类中描述特征，有类特征的是实际的对象。
# 类的命名规范 类中包括属性和函数，属性是对象特征，函数是行为
from enum import nonmember


class MyCar():
    #三个形参，第一个self系统给的，不算参数。这个名字可以改，但是规范给这个
    def __init__(self,brand,type_name,category):  #这个__init__函数是魔法函数，初始化函数，默认自动调用
        self.brand=brand
        self.type_name=type_name
        self.category=category

    def run(self):
        print(f'{self.brand}-{self.type_name}')  #在这类里面都是用函数名来写
        print("go")
#new函数 #这个在创建类是也是自动创建的，而且优先于init
    def __new__(cls,*args,**kwargs):
        print(f'new函数')
        return super().__new__(cls)

#str魔法函数，是在print的输出时候自动调用，输出str函数的返回值
    # 这里改写str函数
    def __str__(self):
        return f'{self.brand}and{self.type_name}'
#del函数，在删除数据的时候默认调用
    def __del__(self):
        print(f'wo yao delete')


C1=MyCar('BYD',"han",'suv')
print(C1.brand)
print(C1)
C1.run()

