# property装饰器：前面加上@会把该函数变成一个参数即属性

class person():
    def __init__(self):
        self.__age=0

    @property               #该装饰器会把该函数变成一个属性，调用的时候不要加（）而是直接用.
    def age(self):
        print(f'age用来')
        return self.__age

    @age.setter             #和上面的配套使用，这样就可以修改上一个里面的参数，否则它是一个属性，属性没办法修改属性        #该
    def age(self,n_age):
        print('xiugai1age')
        self.__age=n_age



if __name__=='__main__':
    p=person()
    p.age=10
    print(p.age)