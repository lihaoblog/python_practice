# 类函数。两个特点，参数是cls且以@classmethod开头
# 成员函数的参数是第一个self
# 静态函数是#staticmethod修饰，不需要传递类对象和实例对象，即不需要self和cls参数
# self是正在被调用的对象，如p1,p2等，cls是类函数，如这里的persion


class person():
    def __init__(self,name):    #成员函数
        self.name = name

    def eat(self):
        print(f'{self.name}要吃饭')

    @classmethod                #类函数
    def work(cls,cname):
        print(f'{cname}要上班')

    @staticmethod
    def run():
        print(f'run go')

p1=person('li')
p1.eat()  #这里只调用eat不会走类函数
# person.eat() 不可以直接用类名调用成员函数，因为有参数self调用

p1.work('hao')      #调用类函数和成员函数差不多
person.work('lih')

p1.run()
person.run()
