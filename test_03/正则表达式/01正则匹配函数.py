#re模块里面有个match函数可以匹配正则只能从头就匹配上，且只看第一个，开始数据对不上则不会返回结果
#group函数是的打印刚刚查的东西
#search是和match相比只多一个不规定开头
#findall查询多个字串，并写入一个列表
#fullmatch和字符串比较一样，必须全部相同
#finditer和fullmatch一样，区别是返回一个迭代器，这样不用一下子都存着
import re

str='python2.7sacsafqaszvveve veadpython  sadsa'

res1=re.match('python',str)
res2=re.search('ve',str)
res3=re.findall('ve',str)
res4=re.fullmatch('ve',str)
res5=re.finditer('ve',str)

print(res1)
print(res1.group())

print(res2)
print(res2.span())


print(res3)
print(res4)
print(res5)
