# import math


# def pt_bacnhat(a, b):
#     if a == 0:
#         if b == 0:
#             return "Phuong Trinh Co Vo  So Nghiem"
#         else:
#             return "Phuong Trinh Vo Nghiem"
#     else:
#         return "Phuong trinh co nghiem duy nhat: {}".format(-b / a)


# def pt_bachai(a, b, c):
#     if a == 0 and b == 0:
#         if c == 0:
#             return "Phuong Trinh Vo So Nghiem!"
#         else:
#             return "Phuong Trinh Vo  Nghiem!"
#     elif a == 0:
#         pt_bacnhat(b, c)
#     else:
#         delta = pow(b, 2) - 4 * a * c
#         if delta < 0:
#             return "Phuong Trinh Vo Nghiem!"
#         elif delta == 0:
#             return "Phuong Trinh Co Nghiem Kep: {}".format(-b / (2 * a))
#         else:
#             return "Phuong Trinh Co 2 Nghiem Phan Biet: x1 = {} va x2 = {}".format(
#                 (-b - math.sqrt(delta)) / (2 * a), (-b + math.sqrt(delta)) / (2 * a)
#             )


# try:
#     print("Ban muon giai phuong trinh gi?")
#     loai_phuong_trinh = int(input())
#     print("Nhap he so phuong trinh can giai:")
#     if loai_phuong_trinh == 1:
#         a, b = map(float, input().strip().split())
#         ket_qua = pt_bacnhat(a, b)
#         print(ket_qua)
#     elif loai_phuong_trinh == 2:
#         a, b, c = map(float, input().strip().split())
#         ket_qua = pt_bachai(a, b, c)
#         print(ket_qua)
#     else:
#         print(
#             """Vui long chon mot trong hai chuc nang:
#         1. Giai phuong trinh bac nhat
#         2. Giai phuong trinh bac hai"""
#         )
# except:
#     print("Dau vao khong hop le!")
######################################
import math

# Dinh nghia ham
def giai_pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem"
        return "Phuong trinh vo nghiem"
    return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)


def giai_pt_bac_hai(a, b, c):
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    # Tinh delta
    delta = b * b - 4 * a * c
    # Kiem tra cac truong hop cua delta
    if delta > 0:
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(
            x1, x2
        )
    if delta == 0:
        x = -b / (2 * a)
        return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
    return "Phuong trinh vo nghiem"


# Khoi lenh co the phat sinh loi
try:
    # Doc dong du lieu dau tien
    chucNang = input()

    # Truong hop 1: Giai phuong trinh bac nhat
    if chucNang == "1":
        # Doc dong du lieu thu hai
        # Ep kieu du lieu sang so thuc
        a, b = map(float, input().split())
        # Goi ham giai phuong trinh bac nhat
        print(giai_pt_bac_nhat(a, b))
    # Truong hop 2: Giai phuong trinh bac hai
    elif chucNang == "2":
        a, b, c = map(float, input().split())
        print(giai_pt_bac_hai(a, b, c))
    else:
        print(
            "Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai"
        )

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
