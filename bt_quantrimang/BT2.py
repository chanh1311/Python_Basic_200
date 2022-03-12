# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
# n = int(input("Nhap n: "))
# if n == 0 or n == 1:
#     print(1)
# else:
#     giai_thua = 1
#     for i in range(1, n + 1):
#         giai_thua *= i
#     print(giai_thua)
# c2: de quy
n = int(input("Nhap n: "))


def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)


ket_qua = giai_thua(n)
print(ket_qua)
