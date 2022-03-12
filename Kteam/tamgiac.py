# print("Nhập vào 3 cạnh của 1 tam giác:")
# a, b, c = input().split()
# a = float(a)
# b = float(b)
# c = float(c)

# if a + b > c and b + c > a and a + c > b:
#     print("Ba cạnh trên là cạnh của 1 tam giác")
# else:
#     print("Ba cạnh trên không phải là cạnh của 1 tam giác")
############################################
# Nhap so do ba canh tu ban phim
# Su dung ham map() va float de ep kieu du lieu sang so thuc
def write_file(text):
    with open("Kteam/tamgiacoutput.txt", "w") as f:
        f.write(text)


try:
    with open("Kteam/tamgiacinput.txt", "r") as f:
        a, b, c = map(float, f.read().split())

    # Dung cau lenh re nhanh de kiem tra dieu kien
    if a <= 0 or b <= 0 or c <= 0:
        write_file("Cac canh cua tam giac phai lon hon 0!")
    elif a + b > c and a + c > b and b + c > a:
        if (
            pow(a, 2) == pow(b, 2) + pow(c, 2)
            or pow(b, 2) == pow(a, 2) + pow(c, 2)
            or pow(c, 2) == pow(b, 2) + pow(a, 2)
        ):
            write_file("La 1 tam giac vuong!")
        elif a == b == c:
            write_file("La tam giac deu!")
        elif a == b or b == c or a == c:
            write_file("La tam giac can")
        elif (
            pow(a, 2) > pow(b, 2) + pow(c, 2)
            or pow(b, 2) > pow(a, 2) + pow(c, 2)
            or pow(c, 2) > pow(b, 2) + pow(a, 2)
        ):
            write_file("La tam giac tu!")
        else:
            write_file("la tam giac nhon!")
    else:
        # Neu dieu kien sai thi xuat thong bao
        write_file("{}, {}, {} khong la ba canh cua mot tam giac".format(a, b, c))
except FileNotFoundError:
    write_file("Khong tim thay duong dan input phu hop!")
except:
    write_file("Input khong dung dinh dang!!")
#######################################
# Khoi lenh co the phat sinh loi
# try:
#    #Mo file voi mode='r' de doc file
#    with open('Bai2.9.inp', 'r') as fileInp:
#        #Doc dong du lieu dau tien tu file
#        #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
#        dongDauTien = fileInp.readline().rstrip('\n')

#    #Su dung ham map() va float de ep kieu du lieu sang so thuc
#    a, b, c = map(float, dongDauTien.split())

#    #Dung cau lenh re nhanh de kiem
#    tra dieu kien cac tam giac
#    #Xu ly truong hop du lieu a, b, c am
#    if a<=0 or b<=0 or c<=0:
#        thongBao = "Cac canh cua tam giac phai lon hon 0!"
#    #Kiem tra dieu kien la ba canh cua tam giac
#    elif a+b>c and a+c>b and b+c>a:
#        #Kiem tra tam giac vuong
#        if a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
#            loaiTamGiac = 'vuong'
#        #Kiem tra tam giac deu
#        elif a==b and b==c:
#            loaiTamGiac = 'deu'
#        #Kiem tra tam giac can
#        elif a==b or a==c or b==c:
#            loaiTamGiac = 'can'
#        #Kiem tra tam giac tu
#        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
#            loaiTamGiac = 'tu'
#        #Cac truong hop con lai la tam giac nhon
#        else:
#            loaiTamGiac = 'nhon'
#        #Thay doi thong bao theo yeu cau
#        thongBao = "{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)
#    else:
#        thongBao = "{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c)

# #Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
# except FileNotFoundError:
#    thongBao = "Khong tim thay file input!"

# #Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
# except:
#    thongBao = "Dinh dang dau vao khong hop le!"

# #Mo file voi mode='w' de ghi file
# with open('Bai2.9.out', 'w') as fileOut:
#    #Xuat thong bao ra file out
#    fileOut.write(thongBao)
