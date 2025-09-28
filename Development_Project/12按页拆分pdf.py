from PyPDF2 import PdfReader, PdfWriter
import os

input_file=PdfReader(r'C:\Users\lihao\Desktop\dify\家庭教育促进法.pdf')

start_page=1
end_page=3
every_div=2
#创建空的pdf
pdf_write=PdfWriter()

# # 循环取出写入
# for page in range(start_page,end_page+1):
#     pdf_write.add_page(input_file.pages[page-1])
#     if page+1>end_page:
#         with open(r'C:\Users\lihao\Desktop\dify\家庭教育促进法_拆分版.pdf','wb') as out:
#             pdf_write.write(out)
# print('success')
print(len(input_file.pages))
for page in range(len(input_file.pages)):
    #当没写的还够既定分组就成组往下写
    if len(input_file.pages)-page > len(input_file.pages) % every_div:
        #把每页写进pdf_write去
        pdf_write.add_page(input_file.pages[page])
        if (page+1)%every_div==0:
            #页码从0开始的
            output_filename=fr'C:\Users\lihao\Desktop\dify\拆分版{page-every_div+2}至{page+1}页.pdf'
            with open(output_filename, 'wb') as out:
                pdf_write.write(out)
                print(f'created {output_filename}')
                # 每次写完重新创建一个
                pdf_write = PdfWriter()
        else:
            continue

    else:
        pdf_write.add_page(input_file.pages[page])
        if (page + 1)==len(input_file.pages):
            output_filename = fr'C:\Users\lihao\Desktop\dify\拆分版{len(input_file.pages)-len(input_file.pages) % every_div+1}至{len(input_file.pages)}页.pdf'
            with open(output_filename, 'wb') as out:
                pdf_write.write(out)
            print(f'created {output_filename}')