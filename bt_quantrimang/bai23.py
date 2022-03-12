# n = int(input("Nhap gia tri n: "))
# ds_chia7 = []
# for i in range(0, n):
#     if i % 7 == 0:
#         ds_chia7.append(i)
# print(*ds_chia7)
########################vong lap while
# n = int(input("Nhap gia tri n: "))
# ds_chia7 = []
# i = 0
# while i < n:
#     if i % 7 == 0:
#         ds_chia7.append(str(i))
#     i += 1
# print("\n".join(ds_chia7))
##########################mau
# def putNumbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i = i + 1
#         if j % 7 == 0:
#             yield j


# # Bài tập Python 23 Code by Quantrimang.com
# for i in putNumbers(100):  # su dung ham putNumbers như 1 interable(yield)
#     print(i)


def putNumbers(n):
    i = 0
    while i < n:
        if i % 7 == 0:
            yield i  # tra ve ket qua nhung khong thoat luon ham
        i += 1


for i in putNumbers(100):
    print(i)
