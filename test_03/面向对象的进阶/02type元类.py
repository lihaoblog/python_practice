class person(object,metaclass=type):  #这些都是隐藏的元类和元继承
    age=33


if __name__=='__main__':
    p1=person        #不加括号是一个类对象，加了是一个实例对象，类对象可以闯将实例对象
    p2=type('person',(object,),{'age':33})   #p1上一句创建类对象就是执行的这一句，解释器的执行，用顶点写的方法

    print(p1.age)
    print(p2.age)

p1=p1()
p2=p2()
# 这下面两个都是一样的
print(p1.__class__)
print(p2.__class__)