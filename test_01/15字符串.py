#串可以用'',"",""" """,''' ''',都可以，I'm 要用转义  I\'m
#字符串是以0开始的，0下标开始，下标也叫索引，从尾到头的话，尾部负1
#切片，即一串中取一段，写法  s[开始：结尾：间隔] 包头不包尾
s1='hello word'
print(s1[7])
print(s1[1:9:2])
print(s1[-6:-2:1])
print(s1[::-1])  #反向打印

print(s1.find('woq')) #find函数用法，查找第一次的位置，没有给-1,同样功能还有index，这个查不到会报错

#切分函数split,分隔符不会在切分出现
print(s1.split('o'))

#切分函数partition,分隔符会在切分出现，只切一次，分三部分
print(s1.partition('o'))

# replace（旧，新值，最多换n次）
print(s1.replace('o','1',2))

#strip 去掉两端指定的数据，前面加l,r代表左右,默认空格，去空值一样trim的
print(s1.lstrip('h'))


