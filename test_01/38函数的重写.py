#重写是你继承父类，又不想完全用父类的，可以修改，但是变量名必须一模一样
#supper().name这个用法是直接拿父类的函数，再加上自己需要的来使用，扩展函数。1.重写函数。2。用supper来继承父亲那部分3.加上自己扩展的部分


class Parents():
    p_name='lih'
    print(p_name)
    def __init__(self,name):
        self.name=name
        print(f'{name}init被执行')

    def sys_hello(self):
        print(f'{self.name}:hello')
        print('hello执行')

class son(Parents):             #这里重写了之前的sys_hello函数，也继承了init，先继承，再修改
    p_name = 'hhhhhh'
    def sys_hello(self):            #前面这个圈圈就是重写的意思
        print(f'{self.name}:nihao')
        print('son执行')
    def __init__(self,name,age):       # init函数是类的初始化函数，也是对object类的重写（严格叫重载，看作新建函数，前面没有重写的圈圈），调用类的对象的时候传几个参数进来
        super().__init__(name)#这里继承了父类的name


s=son('zhang')
s.sys_hello()
print(s.p_name)
