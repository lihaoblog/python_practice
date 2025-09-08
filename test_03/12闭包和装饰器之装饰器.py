# 装饰器在不修改源代码和调用方式的前提下，新增额外的功能

#先写一个闭包,参数必须是一个函数，一会回传
def login(fun):
    def pre(inp):
        print(f'{inp}login')
        fun()
    return pre

@login   #表示login是run的装饰函数，这样就不用再调用了
def run():
    print('running')


if __name__=='__main__':
    # r=login(run)  #这里返回一个pre,再下面正常执行pre
    # r('please')

    run('please')  #申明装饰器就可以直接用。，但是有参数还是必须给。就等于上面被注释的那几个