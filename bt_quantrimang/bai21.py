# import re

# pass_true = []

# list_pass = input().split(",")
# # tach pass thanh ds
# for pas in list_pass:  # kt tung pas xem cai nao thoa#
#     if len(pas) < 6 or len(pas) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", pas):
#         continue
#     elif not re.search("[0-9]", pas):
#         continue
#     elif not re.search("[A-Z]", pas):
#         continue
#     elif not re.search("[$#@]", pas):
#         continue
#     elif re.search("\s", pas):
#         continue
#     else:
#         pass
#     pass_true.append(pas)
#     # them vao list
# # hien thi theo dinh dang dau ,
# print(",".join(pass_true))
import re

value = []

password = [x for x in input("Enter password: ").split(",")]

for i in password:
    if (
        re.search("[a-z]", i)
        and re.search("[0-9]", i)
        and re.search("[$#@]", i)
        and (not (len(i) < 6) or (len(i) > 12))
        and not re.search("\s", i)
    ):
        value.append(i)

print(",".join(value))
