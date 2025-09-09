# 因为装饰器只能带一个参数且还必须是是函数，所以不可以直接给，方法是再套一个函数，把参数给他再返回装饰器
import time
import os
import sys
from functools import wraps


def psd(file_name):
    """
    最外层仅仅负责传个文件名参数进来而已
    文件存在读取不存在则创建
    :param file_name:保存密码的文件，文件格式。里面是password:mima  user：name
    :return:
    """

    def login_check(func):
        users = []  #存储所有的用户名和密码
        check_flag=False
        if os.path.exists(file_name):
            with open(file_name) as f:
                lines = f.readlines()
                for line in lines:
                    user = eval(line)
                    users.append(user)

        else:  # 文件不存在要创建再写入
            choice = input('if create')
            if choice == 'Y' or choice == 'y':
                with open(file_name,'w') as f:
                    p_name = input('please name:')
                    p_pad = input('please password')
                    txt = {'name':p_name,'password':p_pad}
                    users.append(txt)
                    f.write(str(txt) +'\n')
            else:
                print('exit')
                sys.exit(1)

        @wraps(func)   #伪装调用调用的函数本身，把装饰函数隐藏
        def inner(*args,**kwargs):
            # 用户认证，要求认证成功后续不用再输入
            nonlocal check_flag
            if not check_flag:
                nm=input('please input name')
                psd=input('please input you psn')
                for k in users:
                    if nm==k['name'] and psd==k['password'] :
                        print(f'success login{k}')
                        check_flag = True
                        break
                    else:    #登录不成功
                        print('input error')
            if check_flag:
                return func(*args,**kwargs)


        return inner
    return login_check


@psd('user.txt')
def test1():
    print('6666')
    time.sleep(1)


if __name__=='__main__':
    test1()
    test1()
    print(test1.__name__)
    test1()
