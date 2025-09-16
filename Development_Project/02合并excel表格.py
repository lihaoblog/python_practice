"""
该工具时合并多个列相同的xlsx表格，不相同的会错位
"""
import pandas as pd
import os

df_001 = pd.read_excel(r'C:\Users\lihao\Desktop\dify\产品月度销量数据_产品A.xlsx')
df_002 = pd.read_excel(r'C:\Users\lihao\Desktop\dify\产品月度销量数据_产品B.xlsx')
df = pd.concat([df_001, df_002], ignore_index=True)  # 这个时concat的忽略索引列
# print (df)
# # os.listdir()   #所有的文件名列出来


# 读取所有的excel文件
df_list = []  # 建一个list放入元素
path = r'C:\Users\lihao\Desktop\dify'

for i in os.listdir(path):
    if i.split('.')[1] == 'xlsx':
        full_path = os.path.join(path, i)
        # 读文件必须完整路径，所以要把文件路径和读到的文件拼接起来
        df = pd.read_excel(full_path)
        df_list.append(df)
# 数据写入
df_all = pd.concat(df_list, ignore_index=True)
print(df_all)

# 拼接起来路径，用join指定好路径，别的方法不行
out_path = os.path.join(path, '表格大汇总.xlsx')
df_all.to_excel(out_path, index=False)
print('success')
