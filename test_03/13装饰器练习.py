# 求一个时间差
import time

def out(func):
    def inner():
        print('start')
        start=time.time()
        result = func()
        end=time.time()
        print(f'时间差是{end-start}')
        print('end')
        return result
    return inner
@out
def test1():
    print('t1')
    time.sleep(1)


@out
def test2():
    print('t2')
    time.sleep(3)

test1()
test2()