n = int(input())
tong = 0
for i in range(1, n + 1):
    tong += i / (i + 1)
print(round(tong, 2))

# #Bài Python 64, Code by Quantrimang.com
# n=int(input("Nhập số n >0: "))
# sum=0.0
# for i in range(1,n+1):
#     sum += float(float(i)/(i+1))
# print (sum)
