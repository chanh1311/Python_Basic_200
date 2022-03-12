# def phatunhonhat(list_sothuc):
#     phantu_min = list_sothuc[0]
#     for i in list_sothuc:
#         if i < phantu_min:
#             phantu_min = i
#     return phantu_min


# try:
#     s = input()
#     danhdach = s.split()
#     if not len(danhdach):
#         print("Danh sach rong!")
#     else:
#         list_sothuc = list(map(float, danhdach))
#         print(phatunhonhat(list_sothuc))
# except:
#     print("Hay nhap danh sach cac so thuc!")
#####################################
def so_nho_nhat(danhSachSo):
    soNhoNhat = danhSachSo[0]
    for so in danhSachSo:
        if so < soNhoNhat:
            soNhoNhat = so
    return soNhoNhat


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
        soNhoNhat = so_nho_nhat(danhSachSo)
        print(soNhoNhat)
    # Khoi lenh duoc thuc thi khi loi xay ra
    except:
        print("Vui long nhap cac phan tu la so thuc!")
