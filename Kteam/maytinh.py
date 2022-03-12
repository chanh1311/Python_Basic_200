# print("Nhap phep tinh:")
# a, toantu, b = input().split()
# try:
#     a = float(a)
#     toantu = str(toantu)
#     b = float(b)
#     try:
#         if "+" == toantu or "cong" == toantu:
#             result = a + b
#         elif "-" == toantu or "tru" == toantu:
#             result = a - b
#         elif "x" == toantu or "nhan" == toantu:
#             result = a * b
#         elif ":" == toantu or "chia" == toantu:
#             result = a / b
#         print("{} {} {} = {}".format(a, toantu, b, result))
#     except:
#         print("Số bị chia phải khác 0!")
# except:
#     print("Định dạng đầu vào không hợp lệ!")
#####################################
# Nhap bieu thuc tu ban phim
soThu1, phepTinh, soThu2 = input().split()

# Ep kieu du lieu sang so thuc
soThu1 = float(soThu1)
soThu2 = float(soThu2)

# Bien luu ket qua cua bieu thuc
ketQua = None

# Dung cau lenh re nhanh de phan loai phep tinh
# Luu ket qua cua loai phep tinh phu hop
if phepTinh == "+":
    ketQua = soThu1 + soThu2
elif phepTinh == "-":
    ketQua = soThu1 - soThu2
elif phepTinh == "x":
    ketQua = soThu1 * soThu2
elif phepTinh == ":":
    # Xu ly truong hop o phep chia va so bi chia bang 0
    if soThu2 == 0:
        print("So chia phai khac 0!")
    else:
        ketQua = soThu1 / soThu2

# Neu bien ketQua khac None thi chung to bieu thuc hop le
if ketQua != None:
    # In ra man hinh bieu thuc va ket qua
    print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))
