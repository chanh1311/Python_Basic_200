# def tong_chuoi(s):
#     ds_tu = s.split()
#     tong = 0
#     trung_binh_cong = 0
#     count = 0
#     for i in ds_tu:
#         if i.isnumeric():
#             tong += int(i)
#             count += 1
#     if count:
#         trung_binh_cong = tong / count
#     return tong, trung_binh_cong


# s = input()
# tong, trung_binh_cong = tong_chuoi(s)
# print(tong, trung_binh_cong, sep="\n")
####################################
def tong_trung_binh_cac_so(s):
    # Su dung phuong thuc split() de cat chuoi s thanh cac tu ngan cach bang khoang trang
    dsCacTu = s.split()

    tong = 0
    dem = 0

    # Su dung vong lap for de duyet cac tu trong danh sach cac tu cua chuoi s
    for tu in dsCacTu:
        # Kiem tra tu do co phai la so tu nhien khong
        if tu.isdigit():
            # Tinh tong va tang bien dem
            tong += int(tu)
            dem += 1
    if dem == 0:
        return 0, 0
    trungBinh = tong / dem
    return tong, trungBinh


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
tong, trungBinh = tong_trung_binh_cac_so(s)

print(tong)
print(trungBinh)
