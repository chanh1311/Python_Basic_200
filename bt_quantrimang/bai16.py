# string = input()
# count_char = 0
# count_number = 0
# for x in string:
#     if x.isdigit():
#         count_number += 1
#     elif x.isalpha():
#         count_char += 1

# print(count_char)
# print(count_number)
######################
s = input("Nhập câu của bạn: ")
# Bài tập Python 16, Code by Quantrimang.com
d = {"DIGITS": 0, "LETTERS": 0}
for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("Số chữ cái là:", d["LETTERS"])
print("Số chữ số là:", d["DIGITS"])
