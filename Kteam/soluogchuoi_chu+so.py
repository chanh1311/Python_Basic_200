# def so_luong_chuoi(s):
#     count = 0
#     ds_tu = s.split()
#     for i in ds_tu:
#         is_num = False
#         is_alpha = False
#         for j in i:
#             if j.isdigit():
#                 is_num = True
#             elif j.isalpha():
#                 is_alpha = True
#         if is_alpha and is_num:
#             count += 1
#     return count


# s = input()
# count = so_luong_chuoi(s)
# print(count)
####################################
def dem_tu(s):
    dem = 0
    # Su dung phuong thuc split() de cat chuoi s thanh cac tu ngan cach bang khoang trang
    dsCacTu = s.split()

    # Su dung vong lap for de duyet cac tu trong danh sach cac tu cua chuoi s
    for tu in dsCacTu:
        coKyTu = False
        coChuSo = False

        # Duyet cac ky tu trong tu
        for kyTu in tu:
            # Kiem tra ky tu
            if kyTu.isalpha():
                coKyTu = True
            # Kiem tra chu so
            if kyTu.isdigit():
                coChuSo = True

        # Neu tu vua chua ky tu vua chua chu so thi tang bien dem
        if coKyTu and coChuSo:
            dem += 1
    return dem


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(dem_tu(s))
