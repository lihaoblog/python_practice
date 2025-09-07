#my_range是一个迭代器对象，所以必然是可迭代对象，满足条件，反之不一定
#myiter是可迭代对象，因为有iter，同时包含了my_range()是一个迭代器对象，可迭代代表了可以被for循环
#迭代器条件：有next和iter，且iter返回self，next超出限制抛出StopIteration异常
#可迭代条件：有iter对象，且返回一个迭代器对象即返回的是有iter和next，可以用dir查——-iter__
#迭代器好处是节省空间，只占一个空间反复利用，缺点是next只能往后不能回头，不可以指定和长度预测，这点不如索引，类比链表和线性表。

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


class my_iter():
    def __iter__(self):
        return my_range(6)

print(my_iter().__iter__())

#这里123被认为是一个列表，所以列表是可迭代对象
print(dir([1,2,3]))