class Employee:
    """
    定义员工类
    """
    def __init__(self,name,gender,age,mobile_num,is_leave='0'):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_num = mobile_num
        self.is_leave = False if is_leave == '0' else True

    def __str__(self):      #该魔法函数重新定义输出函数为字符串  要用return而不是print 否则会出现none空返回值
        msg='离职' if self.is_leave else '在职'
        return f'{self.name}\t{self.gender}\t{self.age}\t{self.mobile_num}\t{msg}'

if __name__ == '__main__':
    e=Employee('lihao','man','30','1582778','1')
    e.is_leave = False   #这里给false和True，01不行，因为进入str函数不处理01
    print(e.__str__())
    print(e.__dict__)               #转化字典输出
    print(vars(e))                  #vars也时转化字典的

    try:
        f = open('employee.data', 'r')
    except Exception as error:
        # 报错不是说明有问题，可能是没有该文件，建一个
        f = open('employee.data', 'w')
    else:  # 有这个文件就要开始处理读出来了
        data = f.read()  # 这取到的很有可能时列表中的一个个字典，所有进一步处理
        # lst = eval(data)
        # print(lst['gender'])
        if data:
            lst = eval(data)  # 这个函数和vars类似，不过这个用来转列表,解析成列表方便后续遍历
            for dict1 in lst:
                print(dict1)

                print(Employee(dict1['name'], dict1['gender'], dict1['sge'], dict1['mobile_num'], dict1['is_leave']))
