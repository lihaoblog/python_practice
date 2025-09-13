# 迭代器对象有三个条件
# 1.类中定义了__iter__和__next__函数
# 2.__iter__返回self自身
# 3.__next__函数返回下一个数据，如果没有下一个就返回StopIteration()异常

from collections.abc import Iterator


# 迭代器写一个range函数，是从0开始不包括最大的值，包头不包尾
# for循环本质就是不断调用next函数，直到捕获StopIteration退出
class my_range():
    def __init__(self, max):
        self.count = -1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.max:
            raise StopIteration()
        return self.count


if __name__ == '__main__':
    obj = my_range(6)
    print(isinstance(obj, Iterator))
    print(obj)
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))

#可迭代对象，有iter没有next，且返回一个迭代器对象，这个返回可用dir调iter来看有没有迭代器对象的两个函数
obj1=range(6)   #可迭代对象
obj2=my_range(6)  #迭代器对象
obj3=obj1.__iter__()

print(dir(obj1))
print(dir(obj3))