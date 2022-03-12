string = input()

list_kq = [string[x] for x in range(len(string)) if x % 2 == 0]
print("".join(list_kq))
#####################
chuoi = input("Nhập chuỗi vào đây: ")
# Code by Quantrimang.com
chuoi = chuoi[::2]  # lap 2 vi tri
print(chuoi)
