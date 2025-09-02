# 5种
import random   #直接import，第一种
import math

print(math.log2(8))  #用法就是math.函数
print(math.log(8,2)) #等于这种写法

from math import *   #第二种，导入部分，不知道直接用*表示所有
print(log10(100))     #特点是不用写math直接用函数

from math import log2,log10  #第三种精确导入，使用方法和上面相同，这三种用的最多
print(log10(100))

import multiprocessing as mp   #取别名的方法，第四种
from math import log10  as lg10 #第五种一样，对精确的函数取别名
print(lg10(100))
