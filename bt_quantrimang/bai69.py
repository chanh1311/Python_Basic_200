# def generator(n):
#     i = 0
#     while i <= n:
#         if i % 5 == 0 and i % 7 == 0:
#             yield i

#         i += 1


# # Phia tren la mot generator
# list_giatri = []
# n = int(input())
# for x in generator(
#     n
# ):  # Khong biet no chay ntn nhung biet moi lan lap no se duoc goi lai sau tu yield bao gio het thoa dieu kien trong vong while thi thoi se dung
#     list_giatri.append(str(x))

# print(",".join(list_giatri))


# def NumGenerator(n):
#     for i in range(n + 1):
#         if i % 5 == 0 and i % 7 == 0:
#             yield i


# # Bài tập Python 69, Code by Quantrimang.com
# n = int(input("Nhập n: "))
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))

# print("Các số chia hết cho 5 và 7 trong khoảng 0 và n là: ", ",".join(values))


###################################################################
# def test(n):
#     yield n  # giong nhu khi tao 1 interable[n]


# for x in test(10):
#     print(10)
# 10
