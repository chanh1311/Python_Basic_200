# n = int(input())
# list_result = [str(i * i) for i in range(n)]

# print("\n".join(list_result))
# ####################################
# [print(i ** 2) for i in range(n)]
############################
n = int(input())
print(*[num ** 2 for num in range(n)], sep="\n")
