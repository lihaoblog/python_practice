#找模块的时候，首先当前目录，如果没有就找shell变量中pythonpath上面找变量配置信息，在import后面按crtl可以点进去查看，这里面有所有的模块



import  sys
from test_01.pkg1.my_moudle2 import * #这两个里面都有test，用这个方法调用模块时会有替换，导入每个都执行代码，最后执行的会覆盖原有的，所以要取别名

# print(My_Sum(10))
print(test2(10))
print(sys.path)
