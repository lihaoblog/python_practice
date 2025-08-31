# 在属性名和函数名前面加__，即为该函数或属性添加了私有属性，私有属性不可在外部调用，自己在外部调都不行
class annimal:
    __name='animal'
    def __init__(self,color):
        self.__color=color
        print(f'颜色是{self.__color}')
        print(annimal.__name)           #只能这样调类函数的属性

    def __run(self,catelog):
        print('this is color')
    def cloud(self):
        print('this is cloud')


#也不是一定不能用私有函数，有set函数修改属性，用法如下,set和get一起用的，set修改，get获得，不然的话修改了也没办法输出
    def set_color(self,new_color):
        self.__color=new_color
    def get_color(self):
        return self.__color


class dog(annimal):
    pass


an=annimal('red')
# print(an.__color)  不可以用私有的属性，变量
# an.__run('cat')不可以用私有的函数，自己的也不行，外部都不行
d=dog('blue')  #不给参数不报错，但是调不起来init函数
d.cloud()
d.set_color('black')
print(d.get_color())




