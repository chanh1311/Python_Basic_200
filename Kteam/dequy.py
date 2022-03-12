# def de_quy(n):
#     if n:
#         return n + de_quy(n - 1)
#     return 0


# try:
#     print("Nhap vao so can tinh tong:")
#     n = int(input())
#     if n <= 0:
#         print("Hay nhap vao 1 so duong!")
#     else:
#         print("Tong cua day tu 1 den n la: {}".format(de_quy(n)))
# except:
#     print("Dinh dang dau vao khong hop le!")

# Dinh nghia ham
def tinh_tong(n):
    if n:
        return n + tinh_tong(n - 1)
    return 0


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())
    # Su dung cau truc re nhanh xu ly truong hop so am
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        # Goi thuc thi ham va truyen tham so cho ham
        print(tinh_tong(n))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
