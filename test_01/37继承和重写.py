#继承是多个类的从属关系，默认继承父类所有属性和函数
#python中，所有类默认继承object类，这是顶级或者基础类
# 单继承，即只继承一个父类
class animal():
    name='dongwu'
    @staticmethod
    def act():
        print('breve')


class tiger(animal):        #这里就是只继承一个父类，所以叫单继承
    @staticmethod
    def food():
        print('meat')

class duck(animal):        #这里就是只继承一个父类，所以叫单继承
    @staticmethod
    def food():
        print('glass')

t=tiger()
print(t.name)
t.act()

print(type(t))
# isinstance是一个判断函数，返回布尔类型用法就是问前一个是不是后一个类型
print(isinstance(t, animal))
print(isinstance(t, tiger))
print(isinstance(t, int))
print(isinstance(tiger, animal))


#issubclass 也是一个判断函数，判断前面是不是后面一个子类
print(issubclass(duck, animal))
print(issubclass(tiger, duck))
print(issubclass(tiger, object))
