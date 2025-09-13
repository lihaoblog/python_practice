#对象属性即成员属性也叫实例属性如p1
class person():
    species='人类'

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('man',30)  #p1是实例对象，person是类对象
p2=person('woman',29)
person.species = '类人' #修改类的属性只有这一种方法，用新建的p1这种类只能修改自己的那部分

print(p1,p2)  #这种直接打印的是对象地址
print(p1.species,p1.age,p1.name)