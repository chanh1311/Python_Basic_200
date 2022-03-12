# import math

# print("Nhap lan luot cac he so bac 2:")
# a, b, c = map(float, input().split())

# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("Phuong trinh co vo so nghiem!")
#         else:
#             print("Phuong trinh vo nghiem!")
#     else:
#         x1 = -c / b
#         print("Phuong trinh co nghiem duy nhat do la x =  {}".format(x1))
# else:
#     delta = pow(b, 2) - (4 * a * c)
#     if delta < 0:
#         print("Phuong trinh vo nghiem!")
#     elif delta == 0:
#         x1 = -b / (2 * a)
#         print("Phuong trinh co nghiem kep do la x1 = x2 = {}".format(x1))
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         print(
#             "Phuong trinh da cho co 2 nghiem phan biet: x1 = {}, x2 = {}".format(x1, x2)
#         )
########################################################
# Import thu vien math de su dung ham sqrt tinh can bac 2
import math

# Nhap so do ba canh tu ban phim
# Su dung ham map() va float de ep kieu du lieu sang so thuc
try:
    a, b, c = map(float, input().split())
    # Dung cau lenh re nhanh de kiem tra cac truong hop cua bai toan
    # Dung ham print de xuat thong bao phu hop voi tung truong hop
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phuong trinh co vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b))
    else:
        # Tinh delta
        delta = b * b - 4 * a * c
        # Kiem tra cac truong hop cua delta
        if delta > 0:
            x1 = float((-b + math.sqrt(delta)) / (2 * a))
            x2 = float((-b - math.sqrt(delta)) / (2 * a))
            print(
                "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(
                    x1, x2
                )
            )
        elif delta == 0:
            x = -b / (2 * a)
            print("Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x))
        else:
            print("Phuong trinh vo nghiem")
except:
    print("Dinh dang dau vao khong hop le!")
