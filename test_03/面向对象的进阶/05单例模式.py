# 单例模式，不管你创多少实例，都只有一个地址
# 1.通过私有属性设计单例
# 2.通过元类动态设计单例
# 私有设计，原理就是创建实例的时候，有就返回这个实例，没有就按照父类创建一个，当然一样了
class SingleClass(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance


# if __name__=='__main__':
#
#     p1=SingleClass()
#     p2=SingleClass()
#     print(p1 is p2)   #判断两个是不是一个对象

# 元类设计方法，即修改元类，用类的时候将元类修改成我们修改过的，类创建实例就是修改call函数，所以改动call函数就行
class TypeClass(type):
    def __init__(cls,*args,**kwargs):    #初始化新增一个——instance属性
        cls._instance=None
        super().__init__(*args,**kwargs)

    def __call__(cls,*args,**kwargs):   #创建实例就是这个函数起作用
        if not cls._instance:
            cls._instance=super().__call__(*args,**kwargs)
        return cls._instance

class my_single(object,metaclass=TypeClass):
    pass

if __name__=='__main__':

    p1=my_single()
    p2=my_single()
    print(p1 is p2)   #判断两个是不是一个对象

