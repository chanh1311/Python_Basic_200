# with open("Kteam/tuoi.txt", "r") as f:
#     ten = f.readline().rstrip("\n")
#     tuoi = f.readline()

# with open("Kteam/output.txt", "w") as f:
#     try:
#         f.write(
#             "Toi la {}, Nhat dinh 1 nam sau toi se la 1 lap trinh vien chuyen nghiep. Voi so tuoi la {}".format(
#                 ten, int(tuoi) + 1
#             )
#         )
#         print("Đã ghi thành công!")
#     except:
#         print("Đầu vào không hợp lệ!")
###############################
# Khoi lenh co the phat sinh loi
try:
    # Mo file voi mode='r' de doc file

    with open("Kteam/tuoi.txt", "r") as fileInp:
        # Doc 1 dong du lieu tu file va luu vao bien ten

        # Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
        ten = fileInp.readline().rstrip("\n")

        # Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
        tuoiHienTai = int(fileInp.readline())

    # Mo file voi mode='w' de ghi file
    with open("Kteam/output.txt", "w") as fileOut:

        # Ghi noi dung vao file theo mau
        fileOut.write(
            "Vao 20 nam nua, tuoi cua {} se la {}".format(ten, tuoiHienTai + 20)
        )

# Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
    with open("Kteam/output.txt", "w") as fileOut:

        # Xuat thong bao loi
        fileOut.write("Khong tim thay file input!")


# Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"

except:
    with open("Kteam/output.txt", "w") as fileOut:

        # Xuat thong bao loi
        fileOut.write("Dinh dang dau vao khong hop le!")
