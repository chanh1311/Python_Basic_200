from itertools import product

A = map(int, input().split(" "))
B = map(int, input().split(" "))
# Nhập

result = list(product(A, B))  # tao ra 1 list cac tuple nhan cheo

print(*result)  # hien thi
#################################
