# def ds_lonnho_tbc(ds_sothuc):
#     trung_binh_cong = sum(ds_sothuc) / len(ds_sothuc)
#     ds_nho = []
#     ds_lon = []
#     for i in ds_sothuc:
#         if i < trung_binh_cong:
#             ds_nho.append(i)
#         else:
#             ds_lon.append(i)
#     return trung_binh_cong, ds_nho, ds_lon


# danhsach = input().split()
# try:
#     ds_sothuc = list(map(float, danhsach))
#     if not len(ds_sothuc):
#         print("danh sach rong!")
#     else:
#         trung_binh_cong, ds_nho, ds_lon = ds_lonnho_tbc(ds_sothuc)
#         print(trung_binh_cong)
#         print(*ds_nho)
#         print(*ds_lon)
# except:
#     print("dinh dang dau vao khong hop le!")
####################################
def tach_danh_sach(danhSachSo):
    trungBinhCong = sum(danhSachSo) / len(danhSachSo)
    dsNhoHon = [so for so in danhSachSo if so < trungBinhCong]
    dsLonHon = [so for so in danhSachSo if so >= trungBinhCong]
    return trungBinhCong, dsNhoHon, dsLonHon


# Nhap danh sach tu ban phim
danhSach = input().split()
# Khoi lenh co the phat sinh loi
try:
    # Ep kieu du lieu sang so thuc
    danhSachSo = list(map(float, danhSach))
    # Goi thuc thi ham va truyen tham so cho ham
    trungBinhCong, dsNhoHon, dsLonHon = tach_danh_sach(danhSachSo)
    print(trungBinhCong)
    # Unpacking arguments
    print(*dsNhoHon)
    print(*dsLonHon)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Vui long nhap cac phan tu la so thuc!")
