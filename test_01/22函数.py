#新版的pycharm中，是支持函数的类型申明的
#文件是从上往下执行，所以不能先调用再写函数
#注释可以在调用函数时候放在上面会显示注释

def my_abs(num:int)->int :
    """
    该函数是对数值的取绝对值
    :param num: 输入的int类型
    :return: 输出也是int类型
    """
    if num<0:
        return -num
    else:
        return num

print(my_abs(-444))
print(my_abs(4))
print(my_abs(ss))