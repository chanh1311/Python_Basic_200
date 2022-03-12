# try:
#     print("Nhap vao gia tri n:")
#     n = int(input())
#     if n < 1 or n > 9:
#         print("n phai trong khoang tu 1 den 9!")
#     else:
#         for i in range(1, n + 1):
#             if i > 1:
#                 print("\n")
#             for j in range(i, n + 1):
#                 print(j, end=" ")
# except:
#     print("Vui long nhap dung dinh dang!")
###################################
# Khoi lenh co the phat sinh loi
try:
    # Nhap gia tri tu ban phim
    # Ep kieu du lieu sang so nguyen
    n = int(input())

    # Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
    if n < 1 or n > 9:
        print("Vui long nhap gia tri tu 1 den 9!")
    else:
        # Su dung vong 2 vong for long nhau de thuc hien yeu cau bai toan
        for hang in range(n):
            for cot in range(n - hang, 0, -1):
                # Tham so end=' ' de cac so trong hang cach nhau 1 khoang trong
                print(cot, end=" ")
            # Xong 1 hang thi xuong dong
            print()
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
