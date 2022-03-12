# def hoandoi_chuoi(ds_1, ds_2):
#     vitrigiua_1 = len(ds_1) // 2
#     vitrigiua_2 = len(ds_2) // 2

#     ds_ketqua1 = ds_1[:vitrigiua_1] + ds_2[vitrigiua_2:]  # nua dau ds1 + nua sau ds2#
#     ds_ketqua2 = ds_2[:vitrigiua_2] + ds_1[vitrigiua_1:]

#     return ds_ketqua1, ds_ketqua2


# danhsach1 = input().split()
# danhsach2 = input().split()
# ds_ketqua1, ds_ketqua2 = hoandoi_chuoi(danhsach1, danhsach2)
# print(*ds_ketqua1)
# print(*ds_ketqua2)
########################################################
def hoan_doi_danh_sach(danhSach1, danhSach2):
    nuaDoDaiDS1 = len(danhSach1) // 2
    nuaDoDaiDS2 = len(danhSach2) // 2
    # Su dung ky thuat Indexing vaf Cat list de thuc hien yeu cau de bai
    nuaDanhSach1 = danhSach1[nuaDoDaiDS1:]
    nuaDanhSach2 = danhSach2[nuaDoDaiDS2:]
    danhSach1 = danhSach1[:nuaDoDaiDS1] + nuaDanhSach2
    danhSach2 = danhSach2[:nuaDoDaiDS2] + nuaDanhSach1
    return danhSach1, danhSach2


# Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()

# Goi thuc thi ham va truyen tham so cho ham
dsHoanDoi1, dsHoanDoi2 = hoan_doi_danh_sach(danhSach1, danhSach2)
# Unpacking arguments
print(*dsHoanDoi1)
print(*dsHoanDoi2)
