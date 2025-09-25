import glob
import os
import shutil

#
mkdir_path=r'C:\Users\lihao\Desktop\test'
global_path=r'C:\Users\lihao\Desktop\dify'

if  not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

# 取出所有的目标文件，glob关键字是用于提取的所有文件的，rescursive是定义是否递归的
#路径带**\*表示目录下所有的文件
files=glob.glob(r'C:\Users\lihao\Desktop\dify\**\*',recursive=True)
# print(files)

#遍历处理
for file in files:
    #文件夹不要，只筛选取文件
    if os.path.isfile(file):
        # print(file)
        #切割生成的是一个字符串，取出第一个是后缀，第0个是名。二次切分是把.去掉，只要后面的文件类型
        #这个[]在外面，写里面就切分错东西了
        file_cate=os.path.splitext(file)[1][1:]
        # print(file_cate)
        if not os.path.exists(fr'{mkdir_path}\{file_cate}'):
            os.mkdir(fr'{mkdir_path}\{file_cate}')
        # 拷贝文件到该目录下，不要放在里面，放这个if里面只会有一个
        shutil.copy(file,fr'{mkdir_path}\{file_cate}')
    else:
        pass

print('success')