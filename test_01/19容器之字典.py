#容器是包含其他对象的对象叫容器，之前的序列sequence都是一种容器
#容器三种：映射mapping，集合set和序列
#字典即键值对，由大括号包起来，键：值的形式,键是唯一的

dict1={'lihao':19,'liulu':20}

dict2=dict([('li',25),('liu',26)]) # 特殊写法把元祖转成键值对字典，必须二元
dict3=dict(name='li',age=26)  #这会把name和li做一个键值对
print(dict3)
dict3['l张']=26              #这是新增的写法
print(dict3)
dict3['name']='lih'              #这是修改覆盖的写法
print(dict3)

# dict3.clear()  #清空
# print(dict3)

# dict3.pop('age')  #键是唯一的，所以指定删除该键值对字典
# print(dict3)

del dict3['age']  #内置删除法，需要中括号
print(dict3)
print(dict3['name'])

dict4=dict.fromkeys(['adress','tel'])  #这种写法是只有键，空值，需要上面的写法加上值
print(dict4)
print(dict4.get('tel'))     #取得键的值和上面一样

for k,v in dict4.items():               #遍历输出键值对
    print(f'key={k},value={v}')



for k in dict4.keys():               #遍历输出键
    print(f'key={k}')


for v in dict4.values():               #遍历输出值
    print(f'values={v}')


