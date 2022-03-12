# print("Nhập vào số thập phân muốn làm tròn:")
# so_a = input()
# print("Bạn muốn làm tròn mấy chữ số?")
# so_b = input()
# try:
#     so_a = float(so_a)
#     so_b = int(so_b)
#     so_c = round(so_a,so_b)
#     result = "Số {} sau khi được làm tròn {} chữ số là: {}"
#     print(result.format(so_a,so_b,so_c))
# except:
#     print("Đầu vào không hợp lệ!")


giaTriA = input() #Nhap gia tri dau tien tu ban phim
giaTriB = input() #Nhap gia tri thu hai tu ban phim

try: #Khoi lenh co the phat sinh loi
    soA = float(giaTriA) #Ep kieu giaTriA sang kieu so thuc
    soB = int(giaTriB) #Ep kieu giaTriB sang kieu so nguyen

   #Dung ham format de dinh dang chuoi dau ra
    print('{0:.{1}f}'.format(soA, soB))

except: #Khoi lenh duoc thuc thi khi loi xay ra
    print("Dinh dang dau vao khong hop le!") #In thong bao