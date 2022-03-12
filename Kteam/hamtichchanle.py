# def tong_chan_le(n, tuychon):
#     tong = 0
#     while n > 0:
#         if n % 2 == tuychon:  # kiem tra so cuoi la chan hay le
#             tong += n % 10
#         n //= 10
#     return tong


# def tich_chan_le(tong_chan, tong_le):
#     return tong_chan * tong_le


# try:
#     n = int(input())
#     if n <= 0:
#         print("Vui long nhap so tu nhien!")
#     else:
#         print(
#             "Tich chan le la: {}".format(
#                 tich_chan_le(tong_chan_le(n, 0), tong_chan_le(n, 1))
#             )
#         )
# except:
#     print("Dau vao khong hop le!")
########################################
# Dinh nghia ham

# tuyChon == 0: tinh tong cac chu so chan
# tuyChon == 1: tinh tong cac chu so le
def tong_chu_so(soTuNhien, tuyChon):
    tong = 0
    while soTuNhien > 0:
        # Kiem tra chu so cuoi la chan hay le
        if soTuNhien % 2 == tuyChon:
            tong += soTuNhien % 10
        soTuNhien = soTuNhien // 10
    return tong


def tich_chan_le(soTuNhien):
    return tong_chu_so(soTuNhien, 0) * tong_chu_so(soTuNhien, 1)


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        print(tich_chan_le(n))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
