# def cong_chuoi(s1, s2):
#     if len(s1) <= 5:
#         s1 *= 3
#     if len(s2) <= 5:
#         s2 *= 3
#     return s1 + s2


# s1 = input()
# s2 = input()
# print(cong_chuoi(s1, s2))
########################
def chuoi_ket_qua(s1, s2):
    # Su dung ham len de tra ve do dai chuoi
    if len(s1) <= 5:
        # Su dung toan tu * de tao chuoi lap lai
        s1 = s1 * 3
    if len(s2) <= 5:
        s2 = s2 * 3
    # Su dung toan tu + de noi cac chuoi
    return s1 + s2


# Nhap cac chuoi tu ban phim
s1 = input()
s2 = input()

# Goi ham xu ly va truyen cac tham so can thiet
print(chuoi_ket_qua(s1, s2))
