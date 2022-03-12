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
        list_giatri = [str(giatribieuthuc(x)) for x in range(0, n + 1)]
        print(",".join(list_giatri))
except:
    print("Dinh dang dau vao khong hop le!")
# tinh gia tri bieu thuc cho tung phan tu trong day 0 -->n
