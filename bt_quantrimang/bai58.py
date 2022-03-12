# def get_Name():
#     list_name = []
#     while True:
#         email = input()
#         if not email:
#             break
#         if "@" not in email:
#             print("Dinh dang email chua dung!")
#             continue
#         list_split = email.split("@")
#         list_name.append(list_split[0])
#     return list_name


# list_name = get_Name()
# print(*list_name)


# Bài Python 58, Code by Quantrimang.com
import re

emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"  # ---> (abc)@((abc+a1!.)+(com))
# \w --> la cac ki tu chu va so va _
# + --> xuat hien 1 hoac nhiu lan
#  () --> tao 1 nhom
# \ --> Tra ve 1 chuoi DB nao do
# \. --> Chuoi bat ki tru xuong dong
# --> (\w+\.)+ co nghia la 1 hoac nhiu cum nay xuat hien
re2 = re.search(pat2, emailAddress)  # math() cung tuong tu-->tra ve doi tuong math
print(re2)
print(re2.group(1))
