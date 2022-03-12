def chuoitrave_chanle(s):
    chuoimoi = ""
    for i in range(len(s)):
        if len(s) % 2 != i % 2:
            chuoimoi += s[i]
    return chuoimoi


print("Nhap vao 1 chuoi:")
s = input()
print(chuoitrave_chanle(s))
