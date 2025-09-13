#闭包
# 1.内部函数用到了外部函数的变量
# 2.函数有嵌套
# 3.外部函数返回内部函数


def say_hello(name):
    def say(msg):
        nonlocal name   #表示全局变量  这就是闭包修改变量的方法
        name='zhang'  #只有这一句是局部变量，不影响外面的全局，上面有个nonlocal才给权限修改全局
        print(f'{name}{msg}')
# 这里返回say是返回的函数，用say（）是返回调用函数，那不一样
    return say

if __name__=='__main__':
    sa=say_hello('lihao')
    sa('hello')
    # say_hello('lihao').say('hello')#不可以直接用函数对象调用函数，需要给个对象来调用
    #say_hello('lihao')('hello')  #要么这样直接给函数
