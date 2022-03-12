# def giai_thua(n):
#     if n:
#         return n * giai_thua(n - 1)
#     return 1


# try:
#     n = int(input())
#     if n < 0:
#         print("Vui long nhap so tu nhien!")
#     else:
#         print(giai_thua(n))
# except:
#     print("Dinh dang dau vao khong hop le!")
#####################################
def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        print(giai_thua(n))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
