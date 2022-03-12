# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# try:
#     n = int(input())
#     if n <= 0:
#         print("hay nhap vao so tu nhien!")
#     else:
#         print(fibonacci(n))
# except:
#     print("Dinh dang dau vao khong hop le!")
###################################
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n <= 0
    if n <= 0:
        print("Vui long nhap so nguyen duong!")
    else:
        print(fibonacci(n))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
