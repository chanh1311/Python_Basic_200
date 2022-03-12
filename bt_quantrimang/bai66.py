def giatribieuthuc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return giatribieuthuc(n - 1) + giatribieuthuc(n - 2)


try:
    n = int(input())
    if n < 0:
        print("Vui  long nhap n la so duong!")
    else:
        print(giatribieuthuc(n))
except:
    print("Dinh dang dau vao khong hop le!")
