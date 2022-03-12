# def ds_laplai(danhsach, n):
#     ds_moi = []

#     so_lan_lap = n // len(danhsach)
#     so_phan_tu_du = n % len(danhsach)

#     ds_moi = so_lan_lap * danhsach
#     for i in range(so_phan_tu_du):
#         ds_moi.append(danhsach[i])
#     return ds_moi


# try:
#     danhsach = list(input("Nhap danh sach: ").split())
#     n = int(input("Nhap N: "))
#     if n < 0:
#         print("N phai lon hon 0!")
#     else:
#         ds_laplai = ds_laplai(danhsach, n)
#         print(*ds_laplai)
# except:
#     print("Dau vao chua hop le!")
############################################
def nhan_ban_danh_sach(danhSach, n):
    # Su dung ham len() de lay so luong phan tu cua danh sach
    soPhanTu = len(danhSach)
    # Tinh toan so lan toi thieu can lap lai danh sach
    soLanNhanBan = n // soPhanTu + 1
    # Su dung toan tu * de lap danh sach voi so lan mong muon
    dsNhanBan = danhSach * soLanNhanBan
    # Cat danh sach cho dung n phan tu
    dsNPhanTu = dsNhanBan[:n]
    return dsNPhanTu


# Nhap danh sach tu ban phim
danhSach = input().split()
# Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    # Khoi lenh co the phat sinh loi
    try:
        # Nhap gia tri n tu ban phim
        # Ep kieu du lieu sang so nguyen
        n = int(input())
        # Goi thuc thi ham va truyen tham so cho ham
        dsKetQua = nhan_ban_danh_sach(danhSach, n)
        # Unpacking arguments
        print(*dsKetQua)

    # Khoi lenh duoc thuc thi khi loi xay ra
    except:
        print("Dinh dang dau vao khong hop le!")
