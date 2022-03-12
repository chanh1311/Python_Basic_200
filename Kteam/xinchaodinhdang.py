try:
    print("Nhap vao ten cua ban:")
    ten = input()
    print("nhap vao so tuoi")
    tuoi = int(input())
    if tuoi < 0:
        print("tuoi phai lon hon 0!")
    print("Xin chao! Toi la {}, toi {} tuoi.".format(ten, tuoi))
except:
    print("Dinh dang dau vao khong hop le!")
