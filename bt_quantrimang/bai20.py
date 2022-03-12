# def nhap():
#     list_nkgd = []
#     while True:
#         nhap = input("Nhap nhat ki giao dich: ")
#         if nhap:
#             list_nkgd.append(nhap)
#         else:
#             break

#     return list_nkgd


# def tinh_Tien(nkgd):
#     so_du = 0
#     for x in nkgd:
#         if "D" in x:
#             for y in x.split():
#                 if y.isdigit():
#                     so_du += int(y)
#         else:
#             for y in x.split():
#                 if y.isdigit():
#                     so_du -= int(y)
#     return so_du


# nkgd = nhap()

# so_du = tinh_Tien(nkgd)
# print(so_du)
#################################
def tin_Tien():
    so_du = 0
    # nhap nhat ki hiao dich#
    while True:
        s = input("Nhap lich su giao dich: ")
        if not s:
            break
        nhat_ki = s.split()
        # lay tung ki hieu ra so sanh#
        ki_hieu = nhat_ki[0]
        tien = nhat_ki[1]
        if ki_hieu == "D":
            so_du += int(tien)
        elif ki_hieu == "W":
            so_du -= int(tien)
        else:
            pass
    return so_du


so_du = tin_Tien()
print(so_du)
