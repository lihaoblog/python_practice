# .匹配任意单个字符
# []匹配字符集，区间的集合，匹配其中任意一个字符
# \d匹配数字0-9，等同[0-9]
# \D非数字，上一个的取反
# \s匹配空白字符，tab和换行等
# \S上面的取反，非空白字符
# \w匹配单词字符，只能有a-z，A-Z，——，0-9
# \W上面的取反

# * 前一个字符出现0次或者无限次
# + 前一个字符1次或者无限次，至少一次
# ? 前一个字符出现0次或者一次，0或1
# {m} 前一个字符出现m次
# {m,} 前一个字符出现至少m次
# {m,n} 前一个字符出现m到n次之间

# 边界正则
# ^ 以某某开头，用法 ^a  以a开头，也可以取反
# $ 以某某结束，用法 a$ 以a结束
# \b  以字母为边界 用法\b[a-z]左边界字母，放右边是右边界
# \B  上面的那个反向，非字母边界

# # 分组正则
# | 匹配左右随便一个
# (ab) 括号里作为一个分组
# \number 匹配和前面索引为number的分组得到的内容一样的字符串
# (?p<name>) 分组起别名
# (?P<name>) 应用别名为name的分组匹配到的字符串


import re

str = 'python2.7_asasmfkbpdmkepqm  mqp\nsssqdwq,\t521pythonILENG asaPM__--hhh li906@qq.com'

s1 = re.findall('\\d', str)
print(s1)

s2 = re.findall('s{2}', str)
print(s2)

s3 = re.findall('s{2}', str)
print(s3)

s4 = re.findall('s+', str)
print(s4)

s5 = re.findall('[^0-9]', str)  # 表示不包括0-9的数据
print(s5)

s6 = re.findall('^[0-9]', str)  # 表示以0-9开头
print(s6)


s7 = re.match(r"<([a-zA-Z]+)>\w*</\1>", "<html>hhh</html>")  #这里的\1代表第一个正则
print(s7)

s7 = re.match(r"<(?P<my_name>[a-zA-Z]+)>\w*</(?P=my_name)>", "<html>hhh</html>")  #命名用法
print(s7)