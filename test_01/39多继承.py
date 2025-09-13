# 子类继承多个父类（object除外）
# 就近原则：MRO原则:多个父类被继承的时候，会把这些父类放在线性结构上，依次执行，所以最近那个的值覆盖前面的，就近是离得最近的，线性结构可以用类.MRO查看

class parent():
    def __init__(self,name,*args,**kwargs):
        self.name = name
        print('parent的init')

    def test(self):
        print('p的test')


class son1(parent):
    def __init__(self,name,age,*args,**kwargs):
        self.age = age
        super().__init__(name,*args,**kwargs)
        print('son1的init')
    def test(self):
            print('s1的test')

class son2(parent):
    def __init__(self,name,sex,*args,**kwargs):
        self.sex=sex
        super().__init__(name,*args,**kwargs)
        print('son2的init')
    def test(self):
        print('s2的test')


class grandson(son2,son1):
    def __init__(self,name,age,sex,*args,**kwargs):
        super().__init__(name,age,sex)
        print('gs的init')

gs=grandson('li',30,'man')
gs.test()   # 这个就近原则走到son2就取到了需要的值，不会在往下走了，要是取不到就继续走，如上面的gs函数
print(grandson.mro())  # 按照这个顺序线性装入栈，依次弹出，也像递归
