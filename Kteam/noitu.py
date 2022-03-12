# def noi_tu(s):
#     s = s.split()
#     chuoi_ket_qua = "-".join(s)
#     return chuoi_ket_qua


# s = input()
# print(noi_tu(s))
#######################
def noi_chuoi(s):
    # Su dung phuong thuc split() de chia cac phan tu cua chuoi
    danhSachCacTu = s.split()
    # Su dung phuong thuc join() de noi cac chuoi con bang ky tu '-'
    chuoiKetQua = "-".join(danhSachCacTu)
    return chuoiKetQua


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(noi_chuoi(s))
