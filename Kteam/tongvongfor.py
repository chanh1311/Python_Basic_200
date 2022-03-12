# try:
#     print("Nhap vao 2 so nguyen:")
#     a, b = map(int, input().strip().split())
#     if a >= b:
#         print("a phai nho hơn b !")
#     else:
#         tong = 0
#         for x in range(a, b + 1):
#             tong = tong + x
#         print("tong cua day tren la {}".format(tong))
# except:
#     print("Dinh dang nhap vao khong hop le!")
###########################################
# Khoi lenh co the phat sinh loi
try:
    # Nhap hai so tu ban phim
    # Ep kieu du lieu sang so nguyen
    a = int(input())
    b = int(input())

    # Su dung cau truc re nhanh xu ly truong hop a>b
    if a > b:
        print("So thu nhat lon hon so thu hai!")
    else:
        tong = 0
        # Su dung vong lap for voi a <= i <= b
        for i in range(a, b + 1):
            # Cong don cac gia tri i de tinh tong
            tong += i
        print(tong)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
