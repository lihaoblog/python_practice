"""
    该工具是抓取网页的表格内容，写入excel
"""

import pandas as pd
import time

df_list=[]


#循环1到4个网页，抓取数据
for i in range(1,5):
    df = pd.read_html(fr'https://s.askci.com/stock/0-0-0/{i}/')
    df_list.append(df[i])
    time.sleep(3)  #读取每页等三秒，以防卡死

#这是pandas的拼接方式，list用append，这个用concat
all_df=pd.concat(df_list)
print(all_df)
all_df.to_excel(fr'C:\Users\lihao\Desktop\dify\网页抓取表格.xlsx',index=False)