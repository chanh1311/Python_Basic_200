# def ds_GTLN(ds_sothuc):
#     value_max = 0
#     for i in range(len(ds_sothuc)):
#         if ds_sothuc[i] > value_max:
#             value_max = ds_sothuc[i]
#     count_max = 0

#     for i in ds_sothuc:
#         if i == value_max:
#             count_max += 1

#     index_max = [i for i in range(len(ds_sothuc)) if ds_sothuc[i] == value_max]
#     return value_max, count_max, index_max


# danhsach = input().split()
# if not len(danhsach):
#     print("Danh sach rong nhe!")
# else:
#     try:
#         ds_sothuc = list(map(float, danhsach))
#         value_max, count_max, index_max = ds_GTLN(ds_sothuc)
#         print(value_max, count_max, sep="\n")
#         print(*index_max)
#     except:
#         print("Dinh dang dau vao khong hop le!")
###################################
def phan_tu_lon_nhat(danhSachSo):
    giaTri = max(danhSachSo)
    soLuong = danhSachSo.count(giaTri)
    dsViTri = [vt for vt in range(0, len(danhSachSo)) if danhSachSo[vt] == giaTri]
    return giaTri, soLuong, dsViTri


# Nhap danh sach tu ban phim
danhSach = input().split()
# Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    # Khoi lenh co the phat sinh loi
    try:
        # Ep kieu du lieu sang so thuc
        danhSachSo = list(map(float, danhSach))
        # Goi thuc thi ham va truyen tham so cho ham
        giaTri, soLuong, dsViTri = phan_tu_lon_nhat(danhSachSo)
        print(giaTri)
        print(soLuong)
        # Unpacking arguments
        print(*dsViTri)

    # Khoi lenh duoc thuc thi khi loi xay ra
    except:
        print("Vui long nhap cac phan tu la so thuc!")
