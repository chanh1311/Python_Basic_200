n = 5
songuyento = True
for i in range(2, n):
    if n % i == 0:
        songuyento = False
        break
if songuyento:
    print("{} la so nguyen to!".format(n))
else:
    print("{} khong la so nguyen to!".format(n))
