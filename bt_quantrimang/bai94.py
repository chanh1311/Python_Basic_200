string = input()
for x in string:
    print(x, string.count(x))


######################################
dic = {}
chuoi = input("Nhập chuỗi cần đếm ký tự: ")
# Code by Quantrimang.com
for c in chuoi:
    dic[c] = dic.get(c, 0) + 1  # moi lan trung se cong them 1 don vi
print("\n".join(["%s,%s" % (k, v) for k, v in dic.items()]))
