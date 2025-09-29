from PyPDF2 import PdfReader, PdfWriter
import os

all_pdfs=os.listdir(r'C:\Users\lihao\Desktop\dify')
# print(all_pdfs)

# lambda自己不带循环，这样写是判断是否的，不带循环。
# fileter是两个参数，第一个写返还的布尔类型，后面是迭代对象
# 取出需要的文件
pdf_files=list(filter(lambda f:f.lower().endswith('页.pdf') ,all_pdfs))
pdf_files.sort()
# print(pdf_files[0])

# for i in pdf_files:
#     print(os.path.splitext(i)[1]=='.pdf')
#     print(i)

# # 创建一个pdf文件对象准备写入
out_files=PdfWriter()
input_file=PdfReader(r'C:\Users\lihao\Desktop\dify\拆分版1至2页.pdf')
# 获取总页数
# page_count=len(input_file.pages)
# print(page_count)

# 读取每一页并且写入
# for i in range(page_count):
#     out_files.add_page(input_file.pages[i])
#     with open(r'C:\Users\lihao\Desktop\dify\并pdf.pdf','wb') as out_f:
#         out_files.write(out_f)

for j in all_pdfs:
    if j in pdf_files:
        input_file=PdfReader(fr'C:\Users\lihao\Desktop\dify\{j}')
        page_count=len(input_file.pages)
        for i in range(page_count):
            out_files.add_page(input_file.pages[i])
    with open(r'C:\Users\lihao\Desktop\dify\并pdf.pdf', 'wb') as out_f:
       out_files.write(out_f)

