# class nguoi:
#     def __init__(self) -> None:
#         pass

#     def getGender(self):
#         pass


# class nam(nguoi):
#     def getGender(self):
#         print("nam")


# class nu(nguoi):
#     pass

#     def getGender(self):
#         print("nu")


# obj1 = nam()
# obj1.getGender()
# obj2 = nu()
# obj2.getGender()
####################################
class Nguoi(object):
    def getGender(self):
        return "Unknown"


class Nam(Nguoi):
    def getGender(self):
        return "Nam"


# Code by Quantrimang.com
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"


aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
