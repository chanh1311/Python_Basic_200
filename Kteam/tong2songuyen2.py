print("Nhập vào số nguyên a:")
a  = input()
print("Nhập vào số nguyên b:")
b = input()
try:
        a = int(a)
        b = int(b)
        tong = a + b
        print("Tổng 2 số là:",tong)
except:
        print("Đầu vào không hợp lệ!")
