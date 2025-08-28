#对文件夹的操作通常用到os模块，这是python标准库访问操作系统的模块
# import os                           # 使用之前先导入
# os.name                             # 查看当前操作系统的名字，"nt"表示Windows，"posix"表示Linux
# os.sep                              # 获取当前系统平台路径分隔符
# os.getcwd()                         # 获取当前工作目录
# os.environ[key]/os.getenv(key)      # 获取当前环境变量值
# os.listdir(path)                    # 列出指定目录path的所有文件和目录名
# os.chdir(path)                      # 切换目录
# os.mkdir(path)/os.makedirs(path)    # 创建单层目录/多层目录
# os.rmdir(path)/os.removedirs(path)  # 删除单层空目录/多层空目录
# os.remove(file_name)                # 删除文件
# os.rename(old_name,new_name)        # 修改文件或目录名称
# os.path.abspath(path)               # 获取指定相对路径的绝对路径
# os.path.split(path)                 # 获取指定路径的目录名或文件名
# os.path.isfile(path)                # 判断指定路径目标是否为文件
# os.path.isdir(path)                 # 判断指定路径目标是否为目录
# os.path.exists(path)                # 判断指定路径是否存在
# os.path.splitext(path)              # 分离文件拓展名
# os.path.join(path,*paths)           # 路径连接
# os.path.base(path)                  # 提取文件名
# os.path.dirname(path)               # 提取文件路径
# os.path.getsize(path)               # 返回文件大小

import os

print(os.path.abspath('30内置高阶函数.py'))
print(os.path.abspath('file_stream.txt'))
print(os.path.split(r'C:/Users/lihao/Desktop/python/file_stream.txt')) #分割文件名和路径