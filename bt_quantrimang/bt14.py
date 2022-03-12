# list_so = input().split(",")
# int_x = [str(x) for x in list_so if int(x, 2) % 5 == 0]
# print(" ".join(int_x))

value = []
items = [x for x in input("Nhập các số nhị phân: ").split(",")]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)
# Bài tập Python 14, viết bởi Quantrimang.com
print(",".join(value))
