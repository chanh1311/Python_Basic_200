print("Nhap vao day muon ting tong(cach nhau boi khoang trang):")
try:
    a, b = map(int, input().strip().split("\n"))
    if a > b:
        print("a phai nho hon b!")
    else:
        tong = 0
        while a < b + 1:
            tong += a
            a += 1
        print("Tong cua day tren la: {}".format(tong))
except:
    print("Ding dang dau vao chua hop le!")
