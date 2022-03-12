def them_kitu(s):
    chuoi_ket_qua = ""
    if len(s) % 2 == 0:
        for i in range(len(s)):
            if i % 2 != 0:
                chuoi_ket_qua += s[i]
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                chuoi_ket_qua += s[i]
    return chuoi_ket_qua


s = str(input())
print(them_kitu(s))
###############################
def xoa_ky_tu(s):
    chuoiKetQua = ""
    doDaiChuoi = len(s)
    # Su dung vong lap for de duyet cac ky tu cua chuoi
    for i in range(doDaiChuoi):
        # Neu do dai chuoi la so chan thi giu lai ky tu le
        # Neu do dai chuoi la so le thi giu lai ky tu chan
        if i % 2 != doDaiChuoi % 2:
            chuoiKetQua += s[i]
    return chuoiKetQua


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(xoa_ky_tu(s))
