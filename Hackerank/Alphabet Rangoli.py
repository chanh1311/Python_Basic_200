# import string

# alpha = string.ascii_lowercase  # de chuyen so sang chu thuong #

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     print(s)
#     L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
#     print(L)
# print("\n".join(L[:0:-1] + L))


# cach lam:
# b1: Nhap so n de dinh dang, va tao 1 list rong!
# b2: Vong for tao chuoi s chu theo so va phan cach boi dau '-'
# b3: Cong chuoi nguoc cua chuoi s voi chuoi s nhung bat dau bang vi tri 1 theo dinh dang, sau do canh giua chieu dai cho bang cong thuc voi n
# b4: Hien thi List(List se bang list nguoc vua tao(bo phan tu 0) + voi list vua tao)


# print(L[:0:-1])
# --> chuoi nguoc bo phan tu vi tri 0
# print(L[::-1])
# --> chuoi nguoc

import string

alpha = string.ascii_lowercase  # de chuyen so thanh chu thuong
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
print("\n".join(L[:0:-1] + L))
