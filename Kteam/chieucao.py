# try:
#     print("Nhập vào tên chiều cao của người thứ nhất:(cách nhau bởi khoảng trắng)")
#     a = input()
#     a = a.split()
#     tena = a[0]

#     chieucaoa = int(a[1])

#     print("Nhập vào tên chiều cao của người thứ hai:(cách nhau bởi khoảng trắng)")
#     b = input()
#     b = b.split()
#     tenb = b[0]

#     chieucaob = int(b[1])

#     if chieucaoa <= 0:
#         print("chiều cao người a phải lớn hơn 0!")
#     elif chieucaob <= 0:
#         print("chiều cao người b phải lớn hơn 0!")
#     elif chieucaoa > chieucaob:
#         print(tena, "cao hơn", tenb)
#     elif chieucaoa < chieucaob:
#         print(tenb, "cao hơn", tena)
#     else:
#         print("Hai người bằng nhau")
# except:
#     print("Định dạng không hợp lệ!")
############################
# Nhap ten va chieu cao cua ban thu nhat
tenBan1, chieuCaoBan1 = input().split()

# Nhap ten va chieu cao cua ban thu hai
tenBan2, chieuCaoBan2 = input().split()

# Khoi lenh co the phat sinh loi
try:
    # Ep kieu sang so nguyen
    chieuCaoBan1 = int(chieuCaoBan1)
    chieuCaoBan2 = int(chieuCaoBan2)

    # Xu ly truong hop du lieu chieu cao am
    if chieuCaoBan1 <= 0 or chieuCaoBan2 <= 0:
        print("Chieu cao phai lon hon 0!")
    # Xu ly truong hop chieu cao bang nhau
    elif chieuCaoBan1 == chieuCaoBan2:
        print(tenBan1 + " cao bang " + tenBan2)
    # So sanh chieu cao va xuat thong bao
    elif chieuCaoBan1 > chieuCaoBan2:
        print(tenBan1 + " cao hon " + tenBan2)
    else:
        print(tenBan2 + " cao hon " + tenBan1)

# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("dinh dang dau vao khong hop le!")  # In thong bao
