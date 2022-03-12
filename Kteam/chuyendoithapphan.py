print("Nhập vào số thập phân muốn chuyển đổi:")
a = input()
try:
    a = int(a)
    print("Số thập phân %d sau khi được chuyển đổi sang hệ bát phân  là %o" % (a,a))
except:
    print("Nhập vào với 1 định dạng không hợp lệ!")

    