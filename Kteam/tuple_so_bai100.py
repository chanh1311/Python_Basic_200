import math


def conver_number(tupleA):
    number = int("".join(tupleA))
    return number


tupleA = tuple(input().split())
kt_songuyen = all(i.isdigit() for i in tupleA)

if kt_songuyen:
    number = conver_number(tupleA)
    print(number)

else:
    print("Dau vao chua dung!")
