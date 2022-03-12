# def chuyen_doi_chu(s):
#     if len(s) == 0:
#         return ""
#     if s[0].islower():
#         s = s.lower()
#     elif s[0].isupper():
#         s = s.upper()
#     return s


# s = str(input())
# print(chuyen_doi_chu(s))
########################
def bien_doi_chuoi(s):
    # Neu la chuoi rong thi tra ve chuoi rong
    if len(s) == 0:
        return ""
    # Su dung phuong thuc islower() de kiem tra ky tu viet thuong
    if s[0].islower():
        # Su dung phuong thuc lower() de tra ve chuoi voi cac ky tu viet thuong
        return s.lower()
    # Su dung phuong thuc isupper() de kiem tra ky tu in hoa
    if s[0].isupper():
        # Su dung phuong thuc upper() de tra ve chuoi voi cac ky tu viet hoa
        return s.upper()
    # Neu ky tu dau cua chuoi khong phai alphabet thi tra ve chuoi s
    return s


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(bien_doi_chuoi(s))
