def tinh_Tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong


print("1 + 2 + 3 = {}".format(tinh_Tong(1, 2, 3)))
print("1 + 2 + 3 + 4 + 5 = {}".format(tinh_Tong(1, 2, 3, 4, 5)))
