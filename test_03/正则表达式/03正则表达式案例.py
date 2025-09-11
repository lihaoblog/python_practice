# 匹配用户名和密码,用户名有数字字母和_组成，不可以数字开头
import re
from functools import reduce

txt = 'a201314Lh'
tst = 'jj{d%dqs.?q}'

s1 = re.search(r"^[a-zA-Z_]\w{2,16}$", txt)  # 在中括号里面表示取反，外面表示开头
print(s1.group())

s2 = re.match(r"^[a-zA-Z][^!@#$%&]{1,13}$", tst)  # 必须要加$结尾，否则会匹配一小段
print(s2)

# 匹配qq号码
qq = '2278271333'
s3 = re.match(r"^[1-9][0-9]{6,10}$", qq)
print(s3)

file='aa.txt pcome.py buy.sql student.py'
s4=re.findall(r"\b\w+.py\b",file)    #用\b来确定边界，不要用结尾符号，用了只有一个，因为这里面把前一个认为是空格结尾
print(s4)


# 分组正则配合使用findall的，不然只能获取第一个，这里的？：是表示非捕获，这样就不会只返回匹配的哪一点了，就会
email='2278271333@qq.com lihao603@outlook.com lihao960603@foxmail'
s5=re.findall(r'\b\w+@(?:outlook|qq)\.(?:com|cn)\b',email)
print(s5)


s7 = re.match(r"<([a-zA-Z]+)>(?P<msg>\w*)</\1>", "<html>hhh</html>")  #这里的\1代表第一个正则
print(s7.group('msg'))
print(s7.group(2))   #没取别名用第几个编号也可以

s8 = re.findall(r"<(?P<my_name>\w+)>\w+</(?P=my_name)>", "<html>hhh</html> <html>ggg</html>")  #这里的\1代表第一个正则
print(s8)

s9 = re.findall(r"<\w+>(.*?)</\w+>", "<html>hhh</html> <html>ggg</html>")  #这里的\1代表第一个正则
print(s9)    #加括号分组


num='3.16aqfdc-56vd-seqp/12'
s10=re.findall(r"-?\d+\.?\d+",num)  #取正负数据
print(s10)
print(reduce(lambda x,y : x+float(y),s10,0))   #必须要给个初始值，且一定要把数据转成数字，之前是字符串类型


#匹配正负数
str1='-9.33'
s11=re.fullmatch(r"[+-]?(0|[1-9]\d*)(\.\d+)?",str1)
print(s11)

#找是否有中文 中文编码：\u4e00-\u9fa5
s12='李浩.java lihao hhh Aa 我的钱.txt'
chinese=re.findall(r'\b[\u4e00-\u9fa5]+\.[a-zA-Z]*\b',s12)  #用（）只能输出括号选中的匹配值，用\b会返回所有匹配到的
print(chinese)



