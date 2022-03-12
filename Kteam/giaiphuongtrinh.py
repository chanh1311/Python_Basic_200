import math

thong_bao = None
try:
    with open("Kteam/inputgpt.txt", "r") as f:
        chuoi = f.read().split("\n")
    for x in chuoi:
        if x == "":
            chuoi.remove(x)
    chuc_nang, he_so = chuoi
    if chuc_nang == "1":
        a, b = map(float, he_so.split())
        if b == 0:
            thong_bao = "Phuong trinh vo so nghiem!"
        elif a != 0:
            x = -b / a
            thong_bao = "Phuong trinh da cho co nghiem la {}".format(x)
        else:
            thong_bao = "Phuong trinh vo nghiem!"
    elif chuc_nang == "2":
        a, b, c = map(float, he_so.split())
        if a == 0:
            if b == 0:
                if c == 0:
                    thong_bao = "Phuong trinh co vo so nghiem"
                else:
                    thong_bao = "Phuong trinh vo nghiem"
            else:
                thong_bao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(
                    -c / b
                )
        else:
            # Tinh delta
            delta = b * b - 4 * a * c
            # Kiem tra cac truong hop cua delta
            if delta > 0:
                x1 = float((-b + math.sqrt(delta)) / (2 * a))
                x2 = float((-b - math.sqrt(delta)) / (2 * a))
                thong_bao = "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(
                    x1, x2
                )

            elif delta == 0:
                x = -b / (2 * a)
                thong_bao = "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
            else:
                thong_bao = "Phuong trinh vo nghiem"
    else:
        thong_bao = """Vui long chon 2 chuc nang sau:
 1.Giai phuong trinh bac 1
 2.Giai phuong trinh bac 2
                             """

except FileNotFoundError:
    thong_bao = "Khong tim thay file input!"
except:
    thong_bao = "Dinh dang khong hop le!"
if thong_bao != None:
    with open("Kteam/outputgpt.txt", "w") as f:
        f.write(thong_bao)
#########################################################
# Import thu vien math de su dung ham sqrt tinh can bac 2
# import math

# # Khoi lenh co the phat sinh loi
# try:
#     # Mo file voi mode='r' de doc file
#     with open("Bai2.10.inp", "r") as fileInp:
#         # Doc dong du lieu dau tien tu file
#         # Su dung phuong thuc strip de loai bo ky tu xuong dong hay khoang trang
#         dongDauTien = fileInp.readline().strip()

#         # Truong hop 1: Giai phuong trinh bac nhat
#         if dongDauTien == "1":
#             # Doc dong du lieu thu hai tu file
#             dongThuHai = fileInp.readline()
#             a, b = map(float, dongThuHai.split())

#             # Thuat toan giai phuong trinh bac nhat
#             if a == 0:
#                 if b == 0:
#                     thongBao = "Phuong trinh co vo so nghiem"
#                 else:
#                     thongBao = "Phuong trinh vo nghiem"
#             else:
#                 thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(
#                     -b / a
#                 )

#         # Truong hop 2: Giai phuong trinh bac hai
#         elif dongDauTien == "2":
#             # Doc dong du lieu thu hai tu file
#             dongThuHai = fileInp.readline()
#             a, b, c = map(float, dongThuHai.split())

#             # Thuat toan giai phuong trinh bac hai
#             if a == 0:
#                 if b == 0:
#                     if c == 0:
#                         thongBao = "Phuong trinh co vo so nghiem"
#                     else:
#                         thongBao = "Phuong trinh vo nghiem"
#                 else:
#                     thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(
#                         -c / b
#                     )
#             else:
#                 # Tinh delta
#                 delta = b * b - 4 * a * c
#                 # Kiem tra cac truong hop cua delta
#                 if delta > 0:
#                     x1 = float((-b + math.sqrt(delta)) / (2 * a))
#                     x2 = float((-b - math.sqrt(delta)) / (2 * a))
#                     thongBao = "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(
#                         x1, x2
#                     )
#                 elif delta == 0:
#                     x = -b / (2 * a)
#                     thongBao = "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
#                 else:
#                     thongBao = "Phuong trinh vo nghiem"

#         # Truong hop khong chon dung chuc nang
#         else:
#             thongBao = "Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2.Giai phuong trinh bac hai"

# # Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
# except FileNotFoundError:
#     thongBao = "Khong tim thay file input!"

# # Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
# except:
#     thongBao = "Dinh dang dau vao khong hop le!"

# # Mo file voi mode='w' de ghi file
# with open("Bai2.10.out", "w") as fileOut:
#     # Xuat thong bao ra file out
#     fileOut.write(thongBao)
