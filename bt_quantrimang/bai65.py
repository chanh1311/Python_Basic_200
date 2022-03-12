def giatribieuthuc(n):
    if n > 0:
        return giatribieuthuc(n - 1) + 100
    return 0


n = int(input())
if n <= 0:
    print("n phai lon hon 0!")
else:
    print(giatribieuthuc(n))
