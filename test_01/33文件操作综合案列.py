# 写个函数拷贝大文件下的所有py结尾的文件，里面有多重目录，有多种文件，就算没有py文件也要保留目录

import os
from unittest.mock import file_spec


def copy_dir(src, dst):
    """
    拷贝文件到指定目录
    :param src: 原有路径
    :param dst: 拷贝到的路径
    :return: 拷贝文件的数量
    """
    cnt=0
    for f in os.listdir(src):  #列出指定目录path的所有文件和目录名
        s_path=os.path.join(src,f)       #把文件名和目录拼起来
        if os.path.isfile(s_path) and f.endswith('.py'): #取到保证这个是文件且是py结尾
            if not os.path.exists(dst):   #如果最终路径不存在，那么就创建一个，用makedirs表示多级目录创建
                os.makedirs(dst)
            d_path=os.path.join(dst,f)    #这个要获取所有的最终生成的路径和文件名组合。
            #拷贝内容到文件中
            num = copy_file(s_path,d_path)
            cnt+=num
        elif os.path.isdir(s_path) :  #如果是个目录那就递归查下去
            new_path=os.path.join(dst,f)
            copy_dir(s_path, new_path)
    return cnt

#一次性写入方法
# def copy_file(f_src, f_dst):
#     with open(f_src, 'r+', encoding='utf-8') as f_s:
#         content=f_s.read()
#         with open(f_dst, 'w', encoding='utf-8') as f_d:
#              f_d.write(content)
#     return  1

#文件较大，一次写入10kb
def copy_file(f_src, f_dst):
    f_s=open(f_src, 'r+', encoding='utf-8')
    f_d=open(f_dst, 'w', encoding='utf-8')
    while True:
        content=f_s.read(1024*1024)
        if content is None or len(content)==0:
            break
        f_d.write(content)
    f_s.close()
    f_d.close()
    return 1



copy_dir(r'C:\Users\lihao\Desktop\python',r'C:\Users\lihao\Desktop\python111')


