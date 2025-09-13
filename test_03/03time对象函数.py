#该函数操作时分秒
from datetime import time

t=time(hour=16,minute=6,second=55)
print(t)
t1=t.replace(hour=10)
print(t1)

