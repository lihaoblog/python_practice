#return函数返回并退出，不写默认返回None
#return返回多个值是用容器装起来的，默认是元祖，因为元祖是这样形式，可以加list的【】来换成list


def retn1(x,y):
    return x**2,y**2

print (type(retn1(1,2)))
print (retn1(1,2))

#换成列表输出
def retn1(x,y):
    return [x**2,y**2]

print (type(retn1(1,2)))
print (retn1(1,2))