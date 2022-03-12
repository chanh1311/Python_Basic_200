# def nhap_Ds2chieu(M, N):
#     ds_2chieu = []
#     for i in range(M):
#         dong = input("Nhap dong {}: ".format(i + 1)).split()
#         if N != len(dong):
#             print("Nhap chua dung so cot!")
#             return None
#         else:
#             ds_2chieu.append(dong)
#     return ds_2chieu


# def hienThi(DS):
#     for i in DS:
#         print(*i)


# def ds_phantugiao(DS):
#     ds_giao = []
#     hang_1 = DS[0]
#     # lay hang 1 so voi cac hang con lai
#     for i in hang_1:
#         for j in DS[1:]:
#             if i not in j:
#                 break
#         else:  # nguoc lai chay het vong for
#             ds_giao.append(i)
#     return ds_giao


# MvaN = input("Nhap M va N: ").split()
# if len(MvaN) == 0:
#     print("Khong duoc de trong!")
# elif len(MvaN) != 2:
#     print("Hay nhap theo dinh dang M x N")
# else:
#     try:
#         M, N = map(int, MvaN)
#         assert M > 0 or N > 0
#         ds_2chieu = nhap_Ds2chieu(M, N)
#         ds_giao = ds_phantugiao(ds_2chieu)
#         print(*ds_giao)
#     except AssertionError:
#         print("M hoac N phai lon hon 0")
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
            print("Danh sach 2 chieu khong dung kich thuoc")
            return None
        # Them hang vao danh sach 2 chieu
        danhSach2Chieu.append(hang)
    return danhSach2Chieu


def ds_ptu_chung(danhSach2Chieu):
    # Cach 1:
    # Khoi tao danh sach rong
    dsPtuChung = []
    hangDauTien = danhSach2Chieu[0]
    # Su dung vong lap for de lay cac ptu cua hang thu nhat tim kiem trong cac hang con lai
    # Neu ptu o trong tat ca cac hang thi them vao danh sach dsPtuChung
    for ptu in hangDauTien:
        for hang in danhSach2Chieu[1:]:
            if ptu not in hang:
                break
        # Neu vong for khong bi break thi se chay lenh trong khoi else
        else:
            dsPtuChung.append(ptu)
    return dsPtuChung

    # Cach 2:
    # Su dung List Comprehension ket hop voi ham all
    # return [ptu for ptu in danhSach2Chieu[0] if all(ptu in hang for hang in danhSach2Chieu[1:])]


# Khoi lenh co the phat sinh loi
try:
    # Nhap kich thuoc danh sach 2 chieu tu ban phim
    # M - So dong, N - So cot
    M, N = map(int, input().split())

    # Kiem tra dieu kien M, N <=0
    if M <= 0 or N <= 0:
        print("Vui long nhap kich thuoc danh sach la so nguyen duong!")
    else:
        # Goi ham nhap danh sach va truyen vao tham so kich thuoc M, N
        danhSach2Chieu = nhap_danh_sach(M, N)
        if danhSach2Chieu is not None:
            # Goi ham va truyen vao tham so la danh sach 2 chieu
            dsPtuChung = ds_ptu_chung(danhSach2Chieu)
            # Unpacking arguments
            print(*dsPtuChung)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
