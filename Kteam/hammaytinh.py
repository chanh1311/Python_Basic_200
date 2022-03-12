# def cong(sothunhat, sothuhai):
#     return sothunhat + sothuhai


# def tru(sothunhat, sothuhai):
#     return sothunhat - sothuhai


# def nhan(sothunhat, sothuhai):
#     return sothunhat * sothuhai


# def chia(sothunhat, sothuhai):
#     if sothuhai == 0:
#         print("So chia phai khac 0")
#         return 0
#     return sothunhat / sothuhai


# def may_tinh(sothunhat, sothuhai, phep_tinh):
#     if phep_tinh == "+" or phep_tinh == "cong":
#         return cong(sothunhat, sothuhai)
#     elif phep_tinh == "-" or phep_tinh == "tru":
#         return tru(sothunhat, sothuhai)
#     elif phep_tinh == "x" or phep_tinh == "nhan":
#         return nhan(sothunhat, sothuhai)
#     elif phep_tinh == ":" or phep_tinh == "chia":
#         return chia(sothunhat, sothuhai)
#     else:
#         print("Khong co phep tinh nay!")
#         return 0


# try:
#     print("Nhap vao phep tinh can tinh:")
#     sothunhat, phep_tinh, sothuhai = input().strip().split()
#     sothunhat = float(sothunhat)
#     sothuhai = float(sothuhai)
#     if may_tinh(sothunhat, sothuhai, phep_tinh):
#         print(
#             "{} {} {} = {}".format(
#                 sothunhat, phep_tinh, sothuhai, may_tinh(sothunhat, sothuhai, phep_tinh)
#             )
#         )
# except:
#     print("Dinh dang dau vao khong hop le!")
###############################################
# Dinh nghia ham
def cong(soHangThuNhat, soHangThuHai):
    return soHangThuNhat + soHangThuHai


def tru(soBiTru, soTru):
    return soBiTru - soTru


def nhan(thuaSoThuNhat, thuaSoThuHai):
    return thuaSoThuNhat * thuaSoThuHai


def chia(soBiChia, soChia):
    if soChia == 0:
        return "ChiaCho0"
    return soBiChia / soChia


def may_tinh(soThuNhat, soThuHai, phepTinh):
    if phepTinh == "+":
        return cong(soThuNhat, soThuHai)
    if phepTinh == "-":
        return tru(soThuNhat, soThuHai)
    if phepTinh == "x":
        return nhan(soThuNhat, soThuHai)
    if phepTinh == ":":
        return chia(soThuNhat, soThuHai)


# Khoi lenh co the phat sinh loi
try:
    # Nhap bieu thuc tu ban phim
    soThu1, phepTinh, soThu2 = input().split()

    # Ep kieu du lieu sang so thuc
    soThu1 = float(soThu1)
    soThu2 = float(soThu2)

    # Goi thuc thi ham va truyen cac tham so cho ham
    ketQua = may_tinh(soThu1, soThu2, phepTinh)

    if ketQua == "ChiaCho0":
        print("So chia phai khac 0!")
    else:
        # In ra man hinh bieu thuc va ket qua
        print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
