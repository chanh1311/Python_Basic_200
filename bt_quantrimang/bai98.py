def soluonggatho(dau, chan):
    for ga in range(dau + 1):
        tho = dau - ga  # dau con con lai
        if (ga * 2 + tho * 4) == chan:
            return ga, tho
    return 0


if not soluonggatho(35, 94):
    print("Khong co so luong ga, tho phu hop!")
else:
    ga, tho = soluonggatho(35, 94)
    print(ga, tho)
#############################################
def giai(dau, chan):
    klg = "Không có dáp án phù hợp!"
    for i in range(dau + 1):
        j = dau - i
        if 2 * i + 4 * j == chan:
            return i, j
    return klg, klg


# Code by Quantrimang.com
dau = 35
chan = 94
dap_an = giai(dau, chan)
print(dap_an)
