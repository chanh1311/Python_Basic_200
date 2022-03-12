n = int(input())
for i in range(n + 1):
    pad = n.bit_length()  # chiều dài khi trả về số nhị phân
    print(f"{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}")
