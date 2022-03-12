import math

start = [0, 0]

len_xuong = start[0]
trai_phai = start[1]

while True:
    s = input()
    if not s:
        break
    list_s = s.split()
    kh_di_chuyen = list_s[0]
    di_chuyen = int(list_s[1])

    if kh_di_chuyen == "UP":
        len_xuong += di_chuyen
    elif kh_di_chuyen == "DOWN":
        len_xuong -= di_chuyen
    elif kh_di_chuyen == "LEFT":
        trai_phai -= di_chuyen
    elif kh_di_chuyen == "RIGHT":
        trai_phai += di_chuyen
    else:
        pass
print(int(round(math.sqrt(len_xuong ** 2 + trai_phai ** 2))))
