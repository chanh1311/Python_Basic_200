# try:
#     n = int(input())
#     if n <= 0:
#         print("Hay nhap so lon hon 0!")
#     else:
#         so_1, so_2 = 1, 1
#         for i in range(n - 2):
#             so_1, so_2 = so_2, so_1 + so_2
#         print(so_2)
# except:
#     print("Dau vao khong hop le")
##################################
# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n <= 0:
        print("Vui long nhap so nguyen duong!")
    elif n == 1 or n == 2:
        print(1)
    else:
        soThuNhat, soThuHai = 1, 1
        for i in range(n - 2):
            # soThuNhat (moi) = soThuHai (cu)
            # soThuHai (moi) = soThuNhat (cu) + soThuHai (cu)
            soThuNhat, soThuHai = soThuHai, soThuNhat + soThuHai
        print(soThuHai)

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
