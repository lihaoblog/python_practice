#lambda 匿名函数，只有一行的时候可以使用，没有名字。传不传参数都可以
#格式：lambda 参数:返回值
fin1=lambda a,b:a if a>b else b  #简短的函数，取大一点的值
print(fin1(2,1))

lst = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]


lst.sort(key=lambda x:x['age']) #相当于遍历lst中的age值，此外排序会写回原来的lst
print(lst)
