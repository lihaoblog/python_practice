from employee import *
import os


class EmployeeMannerSystem:
    def __init__(self):
        self.employee_file = 'employee.data'  # 这里把员工信息文件定义为实例属性，其实类属性会更好，不用随便改名字
        self.employee_back_up = 'employee_bak.data'  #备份文件名
        self.employee_list = []  # 建一个空列表来存储读出来的数据
        self.save_flag = True    #该标记是用来标记数据是否已保存

    def main(self):
        """ 员工管理系统的额入口"""
        # 1.加载和读取员工的数据文件
        self.load_employee()
        # print(self.load_employee())
        # 2.显示系统的欢迎页面
        while True:
            self.show_hello()
            num = int(input('请选择功能：'))
            if num == 7:
                self.save_out()
                break
            elif num == 1:
                self.add_employee()  # 实例属性必须要加self来访问
            elif num == 2:
                self.delete_employee()
            elif num == 3:
                self.update_employee()
            elif num == 4:
                self.search_employee()
            elif num == 5:
                self.show_all_employee()
            elif num == 6:
                self.save_employee()
    def save_out(self):
        """
        系统在修改后未保存，退出时调用该函数自动保存
        :return:
        """
        if not self.save_flag:   #self.save_flag == False这种写法过时了换成not写法
            self.save_employee()
            print('save yet')


    def save_employee(self):
        """
        保存的需求和步骤：
        1.先备份之前的数据（只备份最近一次的，删掉之前）
        2.创建新文件
        3.写入数据
        4.关闭文件流
        :return:
        """
        if os.path.exists(self.employee_back_up):
            os.remove(self.employee_back_up)  # 删掉之前的备份文件
        os.rename(self.employee_file, self.employee_back_up)  # 备份数据，旧文件直接改名备份文件名字
        with open(self.employee_file, 'w', encoding='utf-8') as f:  # 打开文件往里面写数据
            new_list = []
            for emp in self.employee_list:
                new_list.append(emp.__dict__)
            f.write(str(new_list))  #写入必须要是字符串，这里要转成串
            print('success')
        self.save_flag = True  # 已保存的表示

    def show_all_employee(self):
        """
        直接展示所有的员工信息
        :return:
        """
        print('姓名\t性别\t年龄\t联系方式\t是否离职')
        for nm in self.employee_list:
            print(nm)

    def search_employee(self):
        """
        按名字查员工信息
        :return:
        """
        sear_name = input('请输入要查询的员工名字')
        for nm in self.employee_list:
            if nm.name == sear_name:
                print(nm)
                break
        else:
            print(f'查无{sear_name}此人')

    def update_employee(self):
        """
        按照员工姓名来修改员工信息
        :return:
        """
        up_name = input('请输入要修改的员工姓名')
        for nm in self.employee_list:
            if nm.name == up_name:
                self.save_flag = False

                new_name = input('请输入新的名字，不修改按回车').strip()
                nm.name = new_name if new_name else nm.name

                new_gender = input('请输入新的性别，不修改按回车').strip()
                nm.gender = new_gender if new_gender else nm.gender

                new_age = input('请输入新的年龄，不修改按回车').strip()
                nm.age = new_age if new_age else nm.age

                new_mobile_num = input('请输入新的联系方式，不修改按回车').strip()
                nm.mobile_num = new_mobile_num if new_mobile_num else nm.mobile_num

                new_leave = input('请输入员工是否离职，1离职，0在职，不修改按回车').strip()
                nm.is_leave = '离职' if new_leave == '1' else '在职'
            print('update over')
            print(nm)
            break
        else:
            print(f'查无{up_name}此人')

    def delete_employee(self):
        """
        以员工姓名来修改员工信息
        :return:
        """
        dele_name = input('请输入要删除的员工姓名')
        for nm in self.employee_list:
            if nm.name == dele_name:
                self.save_flag = False
                self.employee_list.remove(nm)  # 移除该对象
                print('remove ok')
                break
            else:
                print(f'查无{dele_name}此人')

    def add_employee(self):
        """
        依次输入员工信息
        :return:
        """
        name = input('请输入员工姓名')
        gender = input('请输入员工性别')
        age = input('请输入员工年龄')
        mobile_num = input('请输入员工联系方式')
        is_leave = input('请输入员工是否离职，1离职，0在职')
        emp = Employee(name, gender, age, mobile_num, is_leave)  # 创建一个对象
        self.save_flag = False
        self.employee_list.append(emp)  # 把对象加入到列表中
        print(emp)

    @staticmethod  # 静态方法，里面用不到self和cls的参数，不依赖实例或者类的状态
    def show_hello():
        print('欢迎进入员工管理系统')
        print('=' * 60)
        print('1.添加员工')
        print('2.删除员工')
        print('3.修改员工')
        print('4.查找员工')
        print('5.显示所有员工')
        print('6.保存员工数据')
        print('7.退出系统')
        print('=' * 60)

    def load_employee(self):
        """
        读取员工数据文件，把所有的员工信息都放到一个列表
        :return:
        """
        try:
            f = open(self.employee_file, 'r')
        except Exception as error:
            # 报错不是说明有问题，可能是没有该文件，建一个
            f = open(self.employee_file, 'w')
        else:  # 有这个文件就要开始处理读出来了
            data = f.read()  # 这取到的很有可能时列表中的一个个字典，所有进一步处理
            if data:
                lst = eval(data)  # 这个函数和vars类似，不过这个用来转列表,解析成列表方便后续遍历
                for dict1 in lst:
                    # 拿出来的还是字典类型，用字典取值的方式拿到我们要的值
                    # self.employee_list.append (Employee(dict1.name,dict1.gender,dict1.age,dict1.mobile_num,dict1.is_leave))
                    self.employee_list.append(
                        Employee(dict1['name'], dict1['gender'], dict1['age'], dict1['mobile_num'], dict1['is_leave']))
                    print(self.employee_list)
        finally:
            if f:
                f.close()


if __name__ == '__main__':
    obj = EmployeeMannerSystem()
    obj.main()




