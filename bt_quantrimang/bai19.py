list_so = list(map(int, input().split(",")))
list_le = [str(x) for x in list_so if x % 2 != 0]
print(",".join(list_le))
#########################
# values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
# numbers = [x for x in values.split(",") if int(x) % 2 != 0]
# print(",".join(numbers))
