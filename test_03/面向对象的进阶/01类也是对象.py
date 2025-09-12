# 类型对象（类对象）：可创实例和继承如 class persion():
# 非实例对象：不可以被继承和创实例  如 p= persion()
# 类本身也是对象，int也是对象，常量也是对象，万物皆对象，python看到的都是对象，这叫面向对象编程
# 两种关系1.父子  2.实例对象  p=person()
# 两个属性1.__class__查是谁创建的的对象实例   2.__bases__查父对象
# type是一切对象的顶点，所有对象都是它创建的，始祖   是创建类对象的类，如同int是创建整数的类
# object是一切对象的继承顶点，所有的类都是继承它，老祖

class person(object):
    print('我是类对象person')

class man(person):
    print('我是man')


p=person()
m=man()
print(p.__class__)
print(man.__bases__)
print(person.__class__)
print(person.__bases__)
print(int.__class__)