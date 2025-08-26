#形参
from keyword import kwlist


def test1(x,y):
    return x*y


def test2(a,b,c=110): #可以指定参数值，后续不传给这个值也行，传了按新传的值算，叫默认传参
    c+=a+b
    return c


#不定长传参
def test3(*nums,t=1):       #不定长度，可以随意给多少个值都行
    if nums :
        return t+sum(nums)
    return t

# 键值对不定长参数
def test4(t=1,**kwargs):  #赋值参数必须要放在键值参数前面，必须
    print(kwargs)
    for k,v in kwargs.items():
        print(f'参数名字{k}: 参数值{v}')
    return sum(kwargs.values()) + t

#各类参数都有的情况下，有严格的顺序
#位置参数》默认参数》不定长普通参数》不定长键值参数。即为：
def test5(a,b,c=100,*args,**kwargs):
    return  0



print(test1(y=12,x=1))  #指定传参数
print(test1(5,10))

print(test2(11,1))
print(test2(0,0,0))

print(test3(1,2,1,t=100 ))

print(test4(a=1,b=100,c=12))