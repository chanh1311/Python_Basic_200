# def ds_trunglap(list_duynhat):
#     ds_trunglap = []
#     for i in range(len(list_duynhat)):
#         for j in range(i + 1, len(list_duynhat)):
#             if (list_duynhat[i] == list_duynhat[j]) and (
#                 list_duynhat[i] not in ds_trunglap
#             ):
#                 ds_trunglap.append(list_duynhat[i])
#     return ds_trunglap


# def ds_duynhat(list_duynhat):
#     ds_duynhat = [i for i in list_duynhat if i not in ds_trunglap(list_duynhat)]
#     return ds_duynhat


# danhsach = input().split()
# ds_duynhat = ds_duynhat(danhsach)
# print(*ds_duynhat)
###################################################
def ds_ptu_duy_nhat(danhSach):
    # Su dung ham count() de dem so lan xuat hien trong danh sach
    dsPtuDuyNhat = [ptu for ptu in danhSach if danhSach.count(ptu) == 1]
    return dsPtuDuyNhat


# Nhap danh sach tu ban phim
danhSach = input().split()

# Goi ham va truyen cac tham so can thiet
dsPtuDuyNhat = ds_ptu_duy_nhat(danhSach)

# Unpacking arguments
print(*dsPtuDuyNhat)
