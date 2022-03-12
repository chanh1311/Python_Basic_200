# try:
#     print("Nhap X de tinh da thuc:")
#     x = float(input())
#     print("Nhap n:")
#     n = int(input())
#     if n < 0:
#         print("n phai lon hon 0!")
#     else:
#         ket_qua = 1
#         giai_thua = 1
#         for i in range(1, 2 * n + 1):
#             giai_thua *= i
#             if i % 2 != 0:
#                 ket_qua -= pow(x, i) / giai_thua
#             else:
#                 ket_qua += pow(x, i) / giai_thua
#         print("Ket qua: {:.5f}".format(ket_qua))
# except:
#     print("Ban nhap sai dau vao!")
####################################
# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    x = float(input())
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap n la so tu nhien!")
    elif n == 0:
        print(1)
    else:
        ketQua = 1
        giaiThua = 1
        # Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, 2 * n + 1):
            giaiThua *= i
            if i % 2 == 0:
                ketQua += pow(x, i) / giaiThua
            else:
                ketQua -= pow(x, i) / giaiThua
        print("{:.5f}".format(ketQua))

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
