# def so_sanh(ten1, chieucao1, ten2, chieucao2):
#     if chieucao1 > chieucao2:
#         print("{} cao hon {}".format(ten1, ten2))
#     elif chieucao1 < chieucao2:
#         print("{} cao hon {}".format(ten2, ten1))
#     else:
#         print("hai nguoi bang nhau")


# try:
#     print("Nhap vao ten va chieu cao nguoi thu nhat:")
#     ten1, chieucao1 = input().split()
#     chieucao1 = int(chieucao1)
#     print("Nhap vao ten va chieu cao nguoi thu hai:")
#     ten2, chieucao2 = input().split()
#     chieucao2 = int(chieucao2)
#     if chieucao1 <= 0 or chieucao2 <= 0:
#         print("chieu cao phai la so duong!")
#     else:
#         so_sanh(ten1, chieucao1, ten2, chieucao2)
# except:
#     print("dau vao chua hop le!")
################################
# Dinh nghia ham
def ten_ban_cao_hon(tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai):
    # So sanh chieu cao cua hai ban
    if chieuCaoBanThuNhat > chieuCaoBanThuHai:
        # Tra ve ten cua ban thu nhat
        return tenBanThuNhat
    # Tra ve ten cua ban thu hai
    return tenBanThuHai


# Khoi lenh co the phat sinh loi
try:
    # Nhap cac gia tri tu ban phim
    tenBanThuNhat, chieuCaoBanThuNhat = input().split()
    tenBanThuHai, chieuCaoBanThuHai = input().split()
    # Ep kieu du lieu chieu cao sang so nguyen
    chieuCaoBanThuNhat = int(chieuCaoBanThuNhat)
    chieuCaoBanThuHai = int(chieuCaoBanThuHai)

    # Su dung cau truc re nhanh xu ly truong hop chieu cao nho hon 1 va chieu cao bang nhau
    if chieuCaoBanThuNhat < 1 or chieuCaoBanThuHai < 1:
        print("Chieu cao phai lon hon 0!")
    elif chieuCaoBanThuNhat == chieuCaoBanThuHai:
        print("{} cao bang {}".format(tenBanThuNhat, tenBanThuHai))
    else:
        # Goi thuc thi ham va truyen cac tham so cho ham
        tenBanCaoHon = ten_ban_cao_hon(
            tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai
        )
        print("{} cao hon.".format(tenBanCaoHon))
# Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")
