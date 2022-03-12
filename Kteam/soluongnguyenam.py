# def soluong_nguyenam(s):
#     songuyenam = 0
#     for i in range(len(s)):
#         if s[i] in ("o", "u", "i", "a", "e") or s[i] in ("O", "U", "I", "A", "E"):
#             songuyenam += 1
#             s = s.replace(s[i], "&")
#     return songuyenam, s


# s = input()
# soluong, chuoi = soluong_nguyenam(s)
# print(soluong, chuoi, sep="\n")
#############################
def thay_the_nguyen_am(s):
    # Liet ke cac ky tu nguyen am
    nguyenAm = "ueoaiUEOAI"
    tongNguyenAm = 0
    # Duyet qua tung ky tu nguyen am
    for c in nguyenAm:
        # Dem cac ky tu nguyen am va cong don vao tong
        tongNguyenAm += s.count(c)
        # Thay the cac ky tu nguyen am thanh ky tu "$"
        s = s.replace(c, "$")
    return tongNguyenAm, s


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
soLuongNguyenAm, chuoiKetQua = thay_the_nguyen_am(s)

# In ket qua
print(soLuongNguyenAm)
print(chuoiKetQua)
