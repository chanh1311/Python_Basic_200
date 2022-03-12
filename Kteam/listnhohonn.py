# import math

##################khong su dung list#################
# def list_sotunhien(n):
#     for i in range(int(n)):
#         print(i, end=" ")
#     print()
#     for i in range(int(n)):
#         print(int(math.pow(i, 2)), end=" ")


# n = input()
# list_sotunhien(n)
################su dung list###########################
# def list_va_listbinhphuong(n):
#     list_so = [i for i in range(int(n))]
#     list_binhphuong = [i * i for i in range(int(n))]
#     return list_so, list_binhphuong


# try:
#     n = int(input())
#     if n < 0:
#         print("n phai la so tu nhien!")
#     else:
#         list_so, list_binhphuong = list_va_listbinhphuong(n)
#         print(*list_so)  # khong co dau * thi se co dau ngoac nhe#
#         print(*list_binhphuong)
# except:
#     print("Dinh dang dau vao khong hop le!")
#######################################
def list_va_list_binh_phuong(n):
    # Khoi tao list su dung List Comprehension
    dsSoTuNhien = [i for i in range(n)]
    dsBinhPhuong = [i * i for i in range(n)]
    return dsSoTuNhien, dsBinhPhuong


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())
    # Su dung cau truc re nhanh xu ly truong hop so am
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        # Goi thuc thi ham va truyen tham so cho ham
        dsSoTuNhien, dsBinhPhuong = list_va_list_binh_phuong(n)
        print(*dsSoTuNhien)
        print(*dsBinhPhuong)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
