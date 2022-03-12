# # def solve(s):
# #     List = []
# #     List = [x.capitalize() for x in s.split()]
# #     return List


# # if __name__ == "__main__":
# #     hoten = input()
# #     result = solve(hoten)
# #     print(" ".join(result))
# ################################
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# def solve(s):
#     for x in s.split():
#         s = s.replace(x, x.capitalize())
#     return s


# if __name__ == "__main__":
#     fptr = open(os.environ["OUTPUT_PATH"], "w")

#     s = input()

#     result = solve(s)

#     fptr.write(result + "\n")

#     fptr.close()
################################
# s = input()
# print(s[:].split())
# print(s.split())
# for x in s[:].split():
#     s = s.replace(x, x.capitalize())
# print(s)


####################################
import os


def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == "__main__":
    file = open(os.environ["FILE_OUTPUT"], "w")

    s = input()
    result = solve(s)
    file.write(result)
    file.close()
    print(result)


# Bài toán nhập vào 1 chuỗi in Chuỗi vào File
# 1. Tạo 1 file output
# 2. Nhập dữ liệu vào
# 3. Gọi hàm xử lí(cho for từng từ cách nhau bởi dấu phân cách, In hoa chữ cái đầu tiên)
# 4.Hien thi ket qua
