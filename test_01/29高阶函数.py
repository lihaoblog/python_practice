#高阶函数是：函数作为值传入或者返回值是函数，是为多阶，称高阶

def test(a,b,f):  #这里的f是函数，我们可以传对于函数名来实现功能
    return f(a)+f(b)


print(test(1,-1,abs))  #这里必须是不带（）的因为在函数里面有括号了，写了报错
print(test(2,3,lambda n:n**2))


def test2(*args):
    def test3():
        sum=0
        for n in args:
            sum+=n
        return sum
    return test3     #不要加括号，返回一个函数而不是函数值

print(test2(1,2,3))  #这个只是返回一个函数，一个什么都没有的test3，要想有值还得用调函数的（）
print(test2(1,2,3)())
