from itertools import product

A = sorted(input().split(" "))
B = sorted(input().split(" "))
print(A)
print(B)

result = product(A, B)

print(*result)
