print("Ban muon hien thi bang cuu chuong may?")
try:
    n = input()
    n = int(n)
    if n <= 0 or n > 9:
        print("bang cuu chuong khong the co so am va gia tri phai nho hon 10!")
    else:
        print("-----------Bang cuu chuong {} la:--------------".format(n))
        for x in range(1, 11):
            print("{} x {} = {}".format(n, x, n * x))
except:
    print("Dinh dang dau vao chua hop le!")
