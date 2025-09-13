#自定义异常
class PasswordTooShortError(Exception):
    def __init__(self, length,min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):              #直接打印异常会返回一个对象或地址，影刺要转成str字符类型输出
       return  f'您输入的密码长度为{self.length},最小长度不得小于{self.min_length}'   #函数必须要用return语句


def input_passwd():
    inp=input('请输入密码:')
    if len(inp) < 6:
        raise PasswordTooShortError(len(inp),min_length=6)  #抛出异常



if __name__ == '__main__':
    try:
        input_passwd()   #用try捕获上面的抛出异常
    except Exception as err:
        print(err)



