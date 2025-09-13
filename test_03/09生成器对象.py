# 生成器本质也是一种迭代器，包含yield关键字的函数，被调用时函数体的代码不会被执行，而是返回一个迭代器，
# 每次请求一个值就会执行生成器的代码，直到遇到yield才会输出，或者遇到return返回结束

def genera():
    yield 1
    s2=yield 2
    print(s2)
    yield 3
    print('3333')
    yield 4

# 直接执行并不会有任何值生成，而是返回生成器对象，既然是迭代器所以用next使用，每次会走一个yield，然后暂停
g=genera()
# hasattr()函数查看里面有没有该函数
print(hasattr(g,'__iter__'))
print(hasattr(g,'__next__'))
print(g)
print(next(g))
# 可以用send函数传值,yield可以输出也可以传入，send是传给刚刚调用的yield的值，所以必须要调一个yield函数才行
print(next(g))
print(g.send('666'))
print(next(g))





