print("Nhập vào day số muốn tính tổng(Số nguyên):")
a = input()
l = a.split()
i = 0 
tong = 0
while( i < len(l)):
        try:
             tong += int(l[i])
        except:
            tong += 0
        finally:
            i = i +1
print("Tổng dãy số trên là:",tong)
###################################
#Nhap dong du lieu chua day gia tri tu ban phim
# dayGiaTri = input()

# #Su dung ham split() de cat day gia tri thanh cac chuoi con
# danhSachGiaTri = dayGiaTri.split()

# #Su dung ham map() de thuc hien viec chuyen cac chuoi con sang kieu so nguyen(đối tượng 1 object)
# danhSachSo = map(int, danhSachGiaTri)
# print(danhSachSo)

# #Su dung ham sum() de tinh tong day so
# tongDaySo = sum(danhSachSo)

# #In ket qua ra man hinh
# print(tongDaySo)