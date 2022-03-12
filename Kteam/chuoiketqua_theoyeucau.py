# def thaythe_chuoi(s):
#     if len(s) < 3 or "ing" == s[-3:]:
#         s = s.replace("ing", "ly")
#     else:
#         s += "ing"
#     return s


# s = input()
# print(thaythe_chuoi(s))
###########################
def chuoi_ket_qua(s):
    # Cat 3 ky tu cuoi cua chuoi s de so sanh
    if len(s) < 3 or s[-3:] != "ing":
        # Them duoi "ing" cho chuoi s
        s += "ing"
    else:
        # Thay the duoi "ing" thanh duoi "ly"
        s = s[:-3] + "ly"
    return s


# Nhap gia tri tu ban phim
s = input()

# Goi ham va truyen cac tham so can thiet
print(chuoi_ket_qua(s))
