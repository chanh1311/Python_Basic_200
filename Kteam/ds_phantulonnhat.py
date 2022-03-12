# def nhap_ds(M, N):
#     ds_nhap = []
#     for i in range(M):
#         ds_dong = input("Nhap dong {}: ".format(i + 1)).split()
#         if len(ds_dong) != N:
#             return False
#         else:
#             ds_nhap.append(ds_dong)
#     return ds_nhap


# def phantulonnhat(DS):
#     ds_Max = []
#     for i in DS:
#         max = 0
#         for j in i:
#             if len(j) > max:
#                 max = len(j)
#         for j in i:
#             if len(j) == max:
#                 ds_Max.append(j)
#                 break
#     return ds_Max


# ds_MN = input("Nhap vao so dong va so cot: ").split()
# if not len(ds_MN):
#     print("Danh sach rong!")
# elif len(ds_MN) != 2:
#     print("Dau vao phai theo dinh dang MxN")
# else:
#     try:
#         M, N = map(int, ds_MN)
#         assert M > 0 or N > 0
#         ds_nhap = nhap_ds(M, N)
#         if not ds_nhap:
#             print("Chua dung dinh dang da khai bao so dong hoac so cot!")
#         else:
#             ds_Max = phantulonnhat(ds_nhap)
#             if ds_Max:
#                 print(*ds_Max)
#     except AssertionError:
#         print("M va N phai la so duong!")
#     except:
#         print("Dinh dang dau vao chua hop le!")
########################################
def nhap_danh_sach(M, N):
    # Khoi tao danh sach rong
    danhSach2Chieu = []
    for i in range(M):
        # Nhap du lieu tung hang tu ban phim va cat thanh list cac phan tu
        hang = input().split()
        # Kiem tra so phan tu co dung kich thuoc
        if len(hang) != N:
            print("Danh sach hai chieu khong dung kich thuoc!")
            return None
        # Them hang vao danh sach 2 chieu
        danhSach2Chieu.append(hang)
    return danhSach2Chieu


def phan_tu_dai_nhat(danhSach):
    # Su dung List Comprehension liet ke Danh sach do dai cac phan tu
    dsDoDai = [len(ptu) for ptu in danhSach]
    # Tim phan tu dai nhat
    maxDoDai = max(dsDoDai)
    # Tim vi tri dau tien cua phan tu dai nhat
    viTriMaxDoDai = dsDoDai.index(maxDoDai)
    # Tra ve gia tri phan tu dai nhat
    return danhSach[viTriMaxDoDai]
