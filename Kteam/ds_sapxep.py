def sap_xep(ds_sothuc):
    for i in range(len(ds_sothuc)):
        for j in range(i + 1, len(ds_sothuc)):
            if ds_sothuc[j] < ds_sothuc[i]:
                tam = ds_sothuc[i]
                ds_sothuc[i] = ds_sothuc[j]
                ds_sothuc[j] = tam
    return ds_sothuc


danhsach = input().split()
if not len(danhsach):
    print("danh sach rong!")
else:
    try:
        list_sothuc = list(map(float, danhsach))
        list_sapxep = sap_xep(list_sothuc)
        print(*list_sapxep)
    except:
        print("Hay nhap vao danh sach so thuc!")
######################################
# def sap_xep_ds_tang(danhSachSo):
#     for i in range(len(danhSachSo)):
#         # Luu vi tri nho nhat
#         viTriNhoNhat = i
#         for j in range(i + 1, len(danhSachSo)):
#             if danhSachSo[j] < danhSachSo[viTriNhoNhat]:
#                 viTriNhoNhat = j
#         # Doi vi tri phan tu thu i dang xet voi phan tu nho nhat
#         danhSachSo[i], danhSachSo[viTriNhoNhat] = (
#             danhSachSo[viTriNhoNhat],
#             danhSachSo[i],
#         )


# # Nhap danh sach tu ban phim
# danhSach = input().split()
# # Kiem tra xem danh sach co rong hay khong
# if len(danhSach) == 0:
#     print("Danh sach rong")
# else:
#     # Khoi lenh co the phat sinh loi
#     try:
#         # Ep kieu du lieu sang so thuc
#         danhSachSo = list(map(float, danhSach))
#         # Goi thuc thi ham va truyen tham so cho ham
#         sap_xep_ds_tang(danhSachSo)
#         # Unpacking arguments
#         print(*danhSachSo)

#     # Khoi lenh duoc thuc thi khi loi xay ra
#     except:
#         print("Vui long nhap cac phan tu la so thuc!")
