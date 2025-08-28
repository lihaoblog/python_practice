# IO流
# 输入输出都是文件叫文件流
# 文件流用法：文件对象=open(目标文件,访问模式)来进行读写
# 文件对象.read（）读整个文件，或指定大小
#以盘符开始的是windows的根目录
f = open(r'C:/Users/lihao/Desktop/python/file_stream.txt', mode='r+',encoding='utf-8')
#上面的地址一定要复制过来修改为/，原来的\被认为是转义字符，可以在前面加个r来表示不要它当转义，原字符表达
print(f.read(3))        #指定几个字符，注意大文件一定要指定不然会把内存撑爆
print(f.readline())     #读一行，这里几个read是串行的不会重复读前面读过的东西
print(f.readlines())    #所有的行都读出来，换行符也会被显示，这里几个read是串行的不会重复读前面读过的东西
f.close()


# 写操作，给其w或w+的model值，都会覆盖原文件，w+是读写，
# 用r+才不会覆盖，直接写，但是在第一行的数据后面写，也不会自动换行，所以会打乱原有的文件，要用seek改变写的位置
wf=open('C:/Users/lihao/Desktop/python/write.txt', mode='w+',encoding='utf-8')
for i in range(10):
    wf.write('hello\n')
# seek(偏移量，从哪开始偏移)，0，1，2分别是开头当前和结尾,一般文件都是最开头开始的
wf.seek(5,0)  #光标移到第一个hello后面，后面读写都从这里开始
aft=wf.read()  #从指针光标之后开始读，读完后指针会到文件末尾，切记
wf.seek(5,0)   #这是把指针再次调到需要的位置
print(aft)
wf.write(' world'+aft)  #写入自己想要的和刚刚读取的后续数据，会覆盖原有的，不用担心重复问题
wf.close()

#为了防止忘记关闭文件，以后但凡文件流或数据库等需要关闭的都统一写成with形式

with open('C:/Users/lihao/Desktop/python/write_read.txt', mode='w+',encoding='utf-8') as wrf:
    for i in range(10):
        wrf.write('this is \n')




