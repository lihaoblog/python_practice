# 对象三大特征：封装、继承、多态
# 封装：将属性和方法书写到类里面的操作叫封装，可以添加权限
# 继承：子类继承父类一切属性和方法（私有除外），可以重写
# 多态：不同对象传入类，产生不同结果，如下：

class animal:
    pass

class dog(animal):
    def say(self):print('wangwang')

class cat(animal):
    def say(self):print('miaomiao')


def test(obj):
    obj.say()
c=cat()
d=dog()

test(c)
test(d)


