# print("Nhap vao so ban muon tinh giai thua:")
# try:
#     n = int(input())
#     if n < 0:
#         print("Muon tinh giai thua phai nhap so lon hon 0!")
#     else:
#         if n == 0:
#             giai_thua = 1
#         else:
#             giai_thua = 1
#             for x in range(n, 0, -1):
#                 giai_thua *= x
#         print("Giai thua la:", giai_thua)
# except:
#     print("Ding dang dau vao chua hop le!")


#########################################
# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        ketQua = 1
        # Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, n + 1):
            ketQua *= i
        print(ketQua)

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
