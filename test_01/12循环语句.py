#计算1-100的所有奇数和
# sum = 0
# i=1
# while i<=100 :
#     if i%2==1 :
#         sum+=i
#     i+=1
# print(sum)


#n*n乘法表
n=int(input('shuru:'))
i=0
while i<n:
    j=1
    while j<=i:
        print(f'{j}*{i}={i*j}',end='\t')
        j+=1
    i+=1
    print('\n')



