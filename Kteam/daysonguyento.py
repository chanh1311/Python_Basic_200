# try:
#     print("nhap vao a:")
#     a = int(input())
#     print("nhap vao b:")
#     b = int(input())
#     if a < 0 or b < 0:
#         print("a va b phai lon hon 0!")
#     elif a > b:
#         print("So thu nhat lon hon so thu hai!")
#     else:
#         for i in range(a, b + 1):
#             if i < 2:
#                 continue
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(i, end=" ")
# except:
#     print("Dinh dang dau vao khong hop le!")
#####################################
import math

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
        # Su dung vong lap for duyet cac so tu a den b
        for i in range(a, b + 1):
            if i > 1:
                # Su dung vong lap for de duyet cac so tu 2 den can bac hai cua i
                for j in range(2, int(math.sqrt(i)) + 1):
                    # Kiem tra tinh chia het
                    if i % j == 0:
                        # Thoat vong lap
                        break
                # Neu khong thoat vong lap thi khoi lenh else se duoc thuc hien
                else:
                    print(i, end=" ")
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
