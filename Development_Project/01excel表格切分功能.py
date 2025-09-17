"""
该工具是切分多个表格，需要替换地址和列名，以那一列切分
使用时修改路径
"""
import pandas as pd

df=pd.read_excel(r'C:\Users\lihao\Desktop\dify\产品月度销量数据.xlsx')
df_dup=df['产品'].drop_duplicates()
for i in df_dup:
    df[df['产品'] == i].to_excel(fr'C:\Users\lihao\Desktop\dify\产品月度销量数据_{i}.xlsx',index=False)  #index忽略索引列

print('完成')