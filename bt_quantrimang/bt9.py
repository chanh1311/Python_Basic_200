import math

Day_D = [100, 150, 180]


def bieuThuc(Day_D):
    Day_Q = [str(int(round(math.sqrt((2 * 50 * i) / 30)))) for i in Day_D]
    return Day_Q


danhsach = bieuThuc(Day_D)
print(",".join(danhsach))

#############################################
#!/usr/bin/env python
# import math

# c = 50
# h = 30
# value = []
# items = [x for x in input("Nhập giá trị của d: ").split(",")]
# for d in items:
#     value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
# # Code by Quantrimang.com
# print(",".join(value))
