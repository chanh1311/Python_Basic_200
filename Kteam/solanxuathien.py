# def count_string(s):
#     tu_da_duyet = ""
#     for i in s:
#         if i not in tu_da_duyet:
#             count = s.count(i)
#             tu_da_duyet += i
#             print(" '{}': {}".format(i, count), end="; ")


# s = input()
# count_string(s)
############################################
def ky_tu_khong_trung_lap(s):
    # Chuoi luu cac ky tu khong trung lap
    chuoiKetQua = ""
    # Su dung vong lap for duyet qua cac ky tu cua chuoi s
    for kyTu in s:
        # Neu ky tu chua xuat hien trong chuoiKetQua thi them vao
        if kyTu not in chuoiKetQua:
            chuoiKetQua += kyTu
    return chuoiKetQua


def dem_ky_tu(s):
    # Goi ham de tra ve chuoi gom cac ky tu xuat hien trong chuoi s
    chuoiKyTu = ky_tu_khong_trung_lap(s)

    # Su dung vong lap for de duyet cac ky tu
    for kyTu in chuoiKyTu:
        # Su dung phuong thuc count() de dem so lan xuat hien trong chuoi s
        dem = s.count(kyTu)
        # Hien thi ra man hinh
        print("'{}': {}; ".format(kyTu, dem), end="")


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
dem_ky_tu(s)
