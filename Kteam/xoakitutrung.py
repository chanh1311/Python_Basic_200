# def xoa_ki_tu_trung(s):
#     for i in range(len(s)):
#         ki_tu = s[i]
#         for j in range(i + 1, len(s)):
#             if ki_tu == s[j]:
#                 s = s.replace(s[j], "")  # Khong thuc hien duoc
#     return s


# s = input()
# print(xoa_ki_tu_trung(s))


def xoa_ki_tu_trung(s):
    chuoi_ket_qua = ""
    for ki_tu in s:
        if ki_tu not in chuoi_ket_qua:
            chuoi_ket_qua += ki_tu
    return chuoi_ket_qua


s = input()
print(xoa_ki_tu_trung(s))
