# def nhan_ds(ds_1, ds_2):
#     ds_2_daonguoc = ds_2[::-1]
#     ds_ketqua = [ds_1[i] * ds_2_daonguoc[i] for i in range(len(ds_1))]
#     return ds_ketqua


# danhsach1 = input().split()
# danhsach2 = input().split()

# try:
#     ds_1 = list(map(float, danhsach1))
#     ds_2 = list(map(float, danhsach2))
#     if len(ds_1) != len(ds_2):
#         print("Hay nhap 2 danh sach cung kich thuoc!")
#     else:
#         ds_ketqua = nhan_ds(ds_1, ds_2)
#         print(*ds_ketqua)
# except:
#     print("Vui long nhap cac phan tu la so thuc!")
#########################################
def nhan_hai_danh_sach(danhSach1, danhSach2):
    # Su dung Comprehension va ham zip() de ghep 2 chuoi
    dsKetQua = [so1 * so2 for so1, so2 in zip(danhSach1, danhSach2[::-1])]

    # for so1, so2 in zip(danhSach1, danhSach2[::-1]):
    #     dsKetQua.append(so1*so2)
    return dsKetQua


# Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()
# Kiem tra xem danh sach co rong hay khong
if len(danhSach1) != len(danhSach2):
    print("Vui long nhap hai danh sach cung kich thuoc!")
else:
    # Khoi lenh co the phat sinh loi
    try:
        # Ep kieu du lieu sang so thuc
        danhSach1 = list(map(float, danhSach1))
        danhSach2 = list(map(float, danhSach2))
        # Goi thuc thi ham va truyen tham so cho ham
        dsKetQua = nhan_hai_danh_sach(danhSach1, danhSach2)
        # Unpacking arguments
        print(*dsKetQua)

    # Khoi lenh duoc thuc thi khi loi xay ra
    except:
        print("Vui long nhap cac phan tu la so thuc!")
