#range迭代生成整数，包头不包尾 range(起，终，间隔）
# break和countinue 只能用在循环

# my_sum=0
# for n in range(1,100,2):
#     my_sum+=n
# print(my_sum)


for i in range(1,10,1) :
    for j in range(1,i+1,1):
        print(f'{j}*{i}={i*j}',end='\t')
    print()
