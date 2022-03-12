# def songuyento(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, n // 2 + 1):
#             if n % i == 0:
#                 return False
#     return True


# def ds_songuyento(list_songuyen):
#     ds_nguyento = []
#     for i in list_songuyen:
#         if songuyento(i):
#             ds_nguyento.append(i)
#     return ds_nguyento


# danhsach = input().split()
# if not len(danhsach):
#     print("danh sach rong!")
# else:
#     try:
#         ds_songuyen = list(map(int, danhsach))
#         ds_nguyento = ds_songuyento(ds_songuyen)
#         print(*ds_nguyento)
#     except:
#         print("Hay nhap vao danh sach so nguyen!")
##########################################
import math


def kt_so_nguyen_to(n):
    if n < 2:
        return False
    # Su dung vong lap for de duyet cac so tu 2 den can bac hai cua n
    for i in range(2, int(math.sqrt(n)) + 1):
        # Kiem tra tinh chia het
        if n % i == 0:
            return False
    return True


def ds_so_nguyen_to(danhSachSo):
    dsSoNguyenTo = [so for so in danhSachSo if kt_so_nguyen_to(so)]
    return dsSoNguyenTo


# Nhap danh sach tu ban phim
danhSach = input().split()
# Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    # Khoi lenh co the phat sinh loi
    try:
        # Ep kieu du lieu sang so nguyen
        danhSachSo = list(map(int, danhSach))
        # Goi thuc thi ham va truyen tham so cho ham
        dsSoNguyenTo = ds_so_nguyen_to(danhSachSo)
        # Unpacking arguments
        print(*dsSoNguyenTo)
    # Khoi lenh duoc thuc thi khi loi xay ra
    except:
        print("Vui long nhap cac phan tu la so nguyen!")
