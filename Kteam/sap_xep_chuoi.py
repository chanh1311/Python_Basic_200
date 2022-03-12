# def phan_loai_chuoi(s):
#     chuoi_so = ""
#     chuoi_chu = ""
#     chuoi_db = ""
#     for i in s:
#         if i.isnumeric():
#             chuoi_so += i
#         elif i.isalpha():
#             chuoi_chu += i
#         else:
#             chuoi_db += i
#     return chuoi_so, chuoi_chu, chuoi_db


# s = input()
# chuoi_so, chuoi_chu, chuoi_db = phan_loai_chuoi(s)
# print(len(chuoi_so), len(chuoi_chu), len(chuoi_db), sep="\n")
# print(chuoi_so + chuoi_chu + chuoi_db)
##############################################
def digit_char_symbol(s):
    digits = ""
    chars = ""
    symbols = ""

    for c in s:
        if c.islower() or c.isupper():
            chars += c
        elif c.isdigit():
            digits += c
        else:
            symbols += c
    chuoiSapXep = digits + chars + symbols

    return len(digits), len(chars), len(symbols), chuoiSapXep


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
slChuSo, slKyTu, slKyHieu, chuoiSapXep = digit_char_symbol(s)

print(slChuSo, slKyTu, slKyHieu, sep="\n")
print(chuoiSapXep)
