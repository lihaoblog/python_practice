# __all__函数，限定只能用模块里面的哪些函数，用了这个之后，导入模块用精确导入情况下 from XX import XX，就只能用这里面的。
# 要是别人直接用impor XXX，上述限制就失效了
__all__=['test2']  #只能公开test2
def My_Sum(n:int)->int:
    """
    求1到n的累加和
    :param n: 数字
    :return: 数字
    """
    s=0
    for i in range(n):
        s=s+i
    return s



def test2(n):
    """
    阶乘
    :return:正整数
    """
    s=1
    for i in range(n):
        if n==1:
            return 1
        else:
            s=test2(n-1)*n
    return s

if __name__=='__main__':  #这个语句表示是不是自己当前执行入口，是的话才执行，这是对测试的一个过滤，以免调用模块时候也会跑下面的调用
    print(test2(5))
    print(My_Sum(5))


