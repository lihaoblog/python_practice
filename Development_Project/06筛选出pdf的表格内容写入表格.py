# pdfplumber   专门处理pdf的包，plumber是管道的意思
import pdfplumber
import pandas as pd

pdf=pdfplumber.open(r'C:\Users\lihao\Desktop\dify\sample_table.pdf')
page=pdf.pages[0]   #取pdf的页数，不带下标表示分成所有的页，记得从0开始的
tables=page.extract_tables()  #抽出页中的表格
df=pd.DataFrame(tables)         #格式化表格
print(len(pdf.pages))    #页数

for i in range(len(pdf.pages)):
    tables=pdf.pages[i].extract_tables()
    for j in range(len(tables)):
        table = tables[j]  #取出第一行，不会有自动生成的0123
        #下面这个格式表化必须要有行列，【1：】表示1之后的所有行
        df = pd.DataFrame(table[1:], columns=table[0])
        df.to_excel(fr'C:\Users\lihao\Desktop\dify\第{i+1}页_第{j+1}张表.xlsx',index=False)
    print('success')