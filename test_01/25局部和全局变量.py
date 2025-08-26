# 函数内部是局部变量，加global应用全局变量
#变量被改变的时候，改变的是栈里面的地址，该地址从之前指向堆里的值的地址换成新值的地址，因此是不可变类型。


a=66
def test1(x,y):
    global a
    print(id(a))
    a=20
    print(id(a))
    return x+y+a

print(test1(1,1))



