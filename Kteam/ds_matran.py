# def Nhap_danh_sach(M, N):
#     DS2chieu = []
#     for i in range(M):
#         Hang = input("Nhap hang {}: ".format(i + 1)).split()
#         if len(Hang) != N:
#             return
#         else:
#             DS2chieu.append(Hang)
#     return DS2chieu


# def In_danh_sach(DS):
#     for j in DS:
#         print(*j)


# Danhsachdauvao = input("Nhap kich thuoc cua danh sach hai chieu: ").split()
# if len(Danhsachdauvao) == 0:
#     print("Danh sach rong!")
# elif len(Danhsachdauvao) != 2:
#     print("Danh sach dau vao gom hai phan tu: Cot va Hang!")
# else:
#     try:
#         M, N = map(int, Danhsachdauvao)
#         assert M > 0 or N > 0
#         Danhsach_2chieu = Nhap_danh_sach(M, N)
#         print(Danhsach_2chieu)
#         if Danhsach_2chieu:
#             In_danh_sach(Danhsach_2chieu)
#     except AssertionError:
#         print("Kich thuoc cua hang va cot phai lon hon 0!")
#     except ValueError:
#         print("Dinh dang dau vao khong hop le!")
#################################################
def nhap_ds(M, N):
    ds_nhap = []
    for i in range(M):
        ds_dong = input("Nhap dong {}: ".format(i + 1)).split()
        if len(ds_dong) != N:
            return
        else:
            ds_nhap.append(ds_dong)
    return ds_nhap


def hienThi_ds(DS):
    for i in DS:
        print(*i)


ds_MN = input("Nhap vao so dong va so cot: ").split()
if not len(ds_MN):
    print("Danh sach rong!")
elif len(ds_MN) != 2:
    print("Dau vao phai theo dinh dang MxN")
else:
    try:
        M, N = map(int, ds_MN)
        assert M > 0 or N > 0
        ds_nhap = nhap_ds(M, N)
        if ds_nhap:
            hienThi_ds(ds_nhap)
    except AssertionError:
        print("M va N phai la so duong!")
    except:
        print("Dinh dang dau vao chua hop le!")
