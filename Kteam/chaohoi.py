# string_chao = ""
# try:
#     with open("Kteam/chaoin.txt", "r") as f:
#         for chao in f:
#             string_chao = string_chao.strip() + " " + chao.strip("\n")
#     with open("Kteam/chaoout.txt", "w") as f:
#         f.write(string_chao)
# except FileNotFoundError:
#     with open("Kteam/chaoout.txt", "w") as f:
#         f.write("Khong tim thay file input!")

############################
# Khoi lenh co the phat sinh loi
try:
    # Mo file voi mode='r' de doc file
    with open("Kteam/chaoin.txt", "r") as fileInp:
        # Dung ham read() doc toan bo du lieu tu file
        toanBoFile = fileInp.read()

    # Dung ham splitlines() cat du lieu theo tung dong va luu thanh danh sach
    danhSachCacDong = toanBoFile.splitlines()
    # Dung ham join() noi cac dong du lieu lai cach nhau 1 khoang trang
    cauChaoHoanChinh = " ".join(danhSachCacDong)
    print(cauChaoHoanChinh)

    # Xu ly them truong hop co nhieu dong trong
    # Dung ham split() de tach cac tu va luu thanh danh sach
    danhSachCacTu = cauChaoHoanChinh.split()
    print(danhSachCacTu)
    # Mot lan nua dung ham join() de noi cac tu lai
    cauChaoDaXuLy = " ".join(danhSachCacTu)

    # Mo file voi mode='w' de ghi file
    with open("Kteam/chaoout.txt", "w") as fileOut:
        # Ghi noi dung vao file
        fileOut.write(cauChaoDaXuLy)

# Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
    with open("Kteam/chaoout.txt", "w") as fileOut:
        # Xuat thong bao loi
        fileOut.write("Khong tim thay file input!")
