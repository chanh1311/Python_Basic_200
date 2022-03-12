# M = int(input())
# set1 = set(map(int, input().split()))
# N = int(input())
# set2 = set(map(int, input().split()))

# result = list(set1.symmetric_difference(set2))
# result.sort()


# print("\n".join(map(str, result)))
############################
a, b = [set(input().split()) for _ in range(4)][
    1::2  # phân cách 2 đơn vị
]  # doc ca 4 dong nhung lay dong 1 va dong 3
print("\n".join(sorted(a ^ b, key=int)))
# ^ co nghia la giao
