# def check_hoan_thien(n):
#     tong = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             tong += i
#     if tong == n:
#         return True
#     return False


# def day_hoan_thien(n):
#     for i in range(1, n + 1):
#         if check_hoan_thien(i):
#             print(i, end=" ")


# try:
#     n = int(input())
#     if n < 0:
#         print("hay nhap so nguyen duong!")
#     else:
#         day_hoan_thien(n)
# except:
#     print("Dinh dang dau vao khong hop le!")
########################################
def kiem_tra_so_hoan_thien(n):
    tongCacUoc = 0
    # Su dung vong lap for de duyet cac so tu 1 den n // 2 + 1
    for i in range(1, n // 2 + 1):
        # Kiem tra tinh chia het
        if n % i == 0:
            # Tinh tong cac uoc
            tongCacUoc += i
    if n == tongCacUoc:
        return True
    return False


def liet_ke_so_hoan_thien(n):
    for i in range(1, n):
        if kiem_tra_so_hoan_thien(i):
            print(i, end=" ")


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n < 0
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        liet_ke_so_hoan_thien(n)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
