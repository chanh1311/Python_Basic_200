# def phantukhac(ds_1, ds_2):
#     ds_ketqua1 = [i for i in ds_1 if i not in ds_2]
#     ds_ketqua2 = [i for i in ds_2 if i not in ds_1]
#     return ds_ketqua1 + ds_ketqua2


# danhsach1 = input().split()
# danhsach2 = input().split()
# ds_ketqua = phantukhac(danhsach1, danhsach2)
# print(*ds_ketqua)
###########################################
def ds_phan_tu_rieng(danhSach1, danhSach2):
    # Su dung List Comprehension
    ptuRiengDS1 = [ptu for ptu in danhSach1 if ptu not in danhSach2]
    ptuRiengDS2 = [ptu for ptu in danhSach2 if ptu not in danhSach1]
    ptuRieng = ptuRiengDS1 + ptuRiengDS2
    return ptuRieng


# Nhap danh sach tu ban phim
danhSach1 = input().split()
danhSach2 = input().split()

# Goi thuc thi ham va truyen tham so cho ham
ptuRieng = ds_phan_tu_rieng(danhSach1, danhSach2)
# Unpacking arguments
print(*ptuRieng)
