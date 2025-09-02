# 异常处理，捕获异常，强制抛出异常，自定义异常
# try:
#     '可能发生的异常代码'
# except 异常1:
#     执行1
# except 异常2：
#     执行2
# 。。。。。。。。。。
from logging import exception
import traceback #处理异常的模块
try:
    f=open('test.txt','w')
    str=f.readline()
    num=int(str.strip())  #这个函数时去两边空值的
    print(num)
except FileNotFoundError:
    print('没发现文件')
except ValueError:
    print('值不对')
except Exception as e:  #最好还是要取别名，这是所有异常的汇总exception，所有异常都在内1
    print(traceback.format_exc())  #打印详细报错信息，和不给捕获异常一样，但是是蓝色的不是红的
else:                   #前面都没匹配到，执行else
    print('没异常')
finally:                #不管有没有异常都会执行
    if f:
        f.close()
print('over')

