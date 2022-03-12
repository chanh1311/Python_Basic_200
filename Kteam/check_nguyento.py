# def nguyen_to(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def day_nguyen_to(a, b):
#     day_nguyen_to = ""
#     for i in range(a, b + 1):
#         if nguyen_to(i):
#             day_nguyen_to += str(i) + " "
#     return day_nguyen_to


# try:
#     print("Nhap vao so a:")
#     a = int(input())
#     print("Nhap vao so b:")
#     b = int(input())
#     if a < 0 or b < 0:
#         print("a hoac b phai lon hon 0!")
#     elif a > b:
#         print("So thu nhat phai nho hon hoac bang so thu 2!")
#     else:
#         print(day_nguyen_to(a, b))
# except:
#     print("Dau vao khong hop le!")
#################################
import math


def kiem_tra_so_nguyen_to(n):
    if n == 1:
        return False
    # Su dung vong lap for de duyet cac so tu 2 den can bac hai cua n
    for i in range(2, int(math.sqrt(n)) + 1):
        # Kiem tra tinh chia het
        if n % i == 0:
            return False
    return True


def liet_ke_so_nguyen_to(a, b):
    for i in range(a, b + 1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=" ")


# Khoi lenh co the phat sinh loi
try:
    # Nhap hai so tu ban phim
    # Ep kieu du lieu sang so nguyen
    a = int(input())
    b = int(input())

    # Su dung cau truc re nhanh xu ly cac truong hop
    if a < 0 or b < 0:
        print("Vui long nhap so tu nhien!")
    elif a > b:
        print("So thu nhat lon hon so thu hai!")
    else:
        liet_ke_so_nguyen_to(a, b)

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
