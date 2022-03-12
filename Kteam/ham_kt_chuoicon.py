# def kt_chuoi(s1, s2):
#     if s2 not in s1:
#         print("Chuoi {} khong ton tai trong chuoi {}!".format(s2, s1))
#     else:
#         print(s1.count(s2))


# s1 = input()
# s2 = input()
# kt_chuoi(s1, s2)
###################################
def kiem_tra_chuoi_con(s1, s2):
    # Su dung toan tu in de kiem tra su xuat hien cua chuoi con
    if s2 in s1:
        # Su dung phuong thuc count() de dem so lan xuat hien cua chuoi con
        print(s1.count(s2))
    else:
        print('Chuoi "{}" khong xuat hien trong chuoi "{}"'.format(s2, s1))


# Nhap cac chuoi tu ban phim
s1 = input()
s2 = input()

# Goi ham xu ly va truyen cac tham so can thiet
kiem_tra_chuoi_con(s1, s2)
