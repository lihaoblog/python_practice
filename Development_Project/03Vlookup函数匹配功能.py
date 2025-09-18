import pandas  as pd

df_001=pd.read_excel(r'C:\Users\lihao\Desktop\dify\产品月度销量数据.xlsx')
df_002=pd.read_excel(r'C:\Users\lihao\Desktop\dify\城市月度降水量数据.xlsx')
# df_01=df_001.head(10)
# df_02=df_002.head(10)
# print(df_02)


#merge函数就是数据库的链接函数，里面是表名，how接连接方式，on接条件
# df_pinjie=pd.merge(df_001,df_002,how='outer',on='月份')
#下面这个写法针对两表列名不一样的情况。如果没有要链接的条件就用left_index：bool=True来表示用索引链接
df_pinjie=pd.merge(df_001,df_002,how='left',left_on='月份',right_on='月份')
print(df_pinjie)