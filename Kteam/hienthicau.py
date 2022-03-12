def xoa_khoang_trang(s):
    s = s.strip()
    while "  " in s:
        s = s.replace("  ", " ")
    return s


def hien_thi_cau(s):
    s = xoa_khoang_trang(s)
    s = s.split(".")
    for i in s:
        i = xoa_khoang_trang(i)
        print(i.title())


s = input()
hien_thi_cau(s)
##################################
# def String_handling(string):
#     return string.split(".")


# def String_lines():
#     In = input("Enter the string: ")
#     for obj in String_handling(In):
#         # split() -> join() -> title()
#         print(" ".join(obj.split()).title())


# if __name__ == "__main__":
#     String_lines()
######################################
# def xoa_khoang_trang_thua(s):
#    #Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
#    s = s.strip()
#    #Su dung vong lap while de lap cho toi khi nao het khoang trang thua
#    while "  " in s:
#        #Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
#        s = s.replace("  ", " ")
#    return s

# def hien_thi_cau(s):
#    #Su dung phuong thuc split() de cat chuoi s thanh cac cau ngan cach bang dau cham
#    dsCacCau = s.split('.')
#    #Su dung vong lap for de duyet cau trong danh sach cac cau cua chuoi s
#    for cau in dsCacCau:
#        #Goi ham xoa khoang trang thua
#        cau = xoa_khoang_trang_thua(cau)
#        #Hien thi ra man hinh cau voi dinh dang title()
#        print(cau.title())

# #Nhap gia tri tu ban phim
# s = input()

# #Goi ham va truyen cac tham so can thiet
# hien_thi_cau(s)
