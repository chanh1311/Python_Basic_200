list_BanDau = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_KetQua = list(
    map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, list_BanDau)))
)
print(list_KetQua)
