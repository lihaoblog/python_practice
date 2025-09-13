def test(num:int)->int:
    """
    求该数的递归值
    :param num:输入一个数值
    :return: 返回一个数值
    """
    if num==1:
        return 1
    else:
        return num * test(num - 1)

print(test(5))