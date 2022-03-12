# def hello(ten, tuoi):
#     print("Xin chao! Toi la {}, toi {} tuoi.".format(ten, tuoi))


# try:
#     print("Nhap vao ten cua ban:")
#     ten = input()
#     print("nhap vao so tuoi")
#     tuoi = int(input())
#     if tuoi < 1:
#         print("tuoi phai la so nguyen duong!")
#     else:
#         hello(ten, tuoi)
# except:
#     print("Dinh dang dau vao khong hop le!")

###################################
# Dinh nghia ham
def xin_chao(ten, tuoi):
    print("Xin chao! Toi la {}, toi {} tuoi.".format(ten, tuoi))


# Khoi lenh co the phat sinh loi
try:
    # Nhap hai gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    ten = input()
    tuoi = int(input())

    # Su dung cau truc re nhanh xu ly truong hop tuoi am
    if tuoi < 1:
        print("Vui long nhap tuoi la so nguyen duong!")
    else:
        # Goi thuc thi ham
        xin_chao(ten, tuoi)
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
