# def list_cothutu(danhsach):
#     list_thutu = enumerate(danhsach)
#     for i in list_thutu:
#         print(*i)


# s = input()
# danhsach = s.split()
# list_cothutu(danhsach)
#########################
def in_list(danhSach):
    # Su dung ham enumerate de them mot bo dem vao truoc moi doi tuong
    for soThuTu, giaTri in enumerate(danhSach):
        print(soThuTu, giaTri)


# Nhap danh sach tu ban phim
danhSach = input().split()

# Goi ham va truyen cac tham so can thiet
in_list(danhSach)
