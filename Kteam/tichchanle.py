# print("Nhap vao so can tinh tong:")
# try:
#     n = int(input())
#     if n < 0:
#         print("n phai lon hon 0 a!")
#     else:
#         chan = 0
#         le = 0
#         while n > 0:
#             chu_so = n % 10
#             if chu_so % 2 == 0:
#                 chan += chu_so
#             else:
#                 le += chu_so
#             n //= 10
#         print(chan * le)
# except:
#     print("Sai dinh dang roi!")
##############################
# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        tongChuSoChan = 0
        tongChuSoLe = 0
        # Su dung vong while de tach cac chu so
        while n > 0:
            # Kiem tra chu so cuoi la chan hay le
            if n % 2 == 0:
                tongChuSoChan += n % 10
            else:
                tongChuSoLe += n % 10
            n = n // 10

        ketQua = tongChuSoChan * tongChuSoLe
        print(ketQua)

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
