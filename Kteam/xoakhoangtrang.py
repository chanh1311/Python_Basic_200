# def xoa_khoang_trang(s):
#     s = s.split()
#     s = " ".join(s)
#     return s


# s = "    kasdkchasnd sadl      dk            "
# print(xoa_khoang_trang(s))
#################################
def xoa_khoang_trang_thua(s):
    # Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
    s = s.strip()
    # Su dung vong lap while de lap cho toi khi nao het khoang trang thua
    while "  " in s:
        # Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
        s = s.replace("  ", " ")
    return s


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(xoa_khoang_trang_thua(s))
