# def Excep():
#     try:
#         pheptinh = 5 / 0
#     except:
#         print("Phép tinh khong thuc hien duoc do so chia bang 0!")


# Excep()


def throws():
    return 5 / 0


# Bài Python 56, Code by Quantrimang.com
try:
    throws()
except ZeroDivisionError:
    print("Chia một số cho 0!")
except Exception as problem:
    print("Bắt được một exception: {}".format(problem))
finally:
    print("Phép tính bị hủy")
