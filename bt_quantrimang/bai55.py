# raise RuntimeError("Ngoai le xay ra!")

# c2
class RuntimeError(Exception):
    def __init__(self, mismatch):
        super().__init__(
            mismatch
        )  # ham khoi tao cua ham cha duoc goi truyen vao 2 doi so


try:
    print("And now, the Vocational Guidance Counsellor Sketch.")
    raise RuntimeError("CHANH CHANH CHÁNH")
    print("This print statement will not be reached.")
except RuntimeError as problem:
    print("Vocation problem: {0}".format(problem))


# obj = e_RuntimeError("Chanh")
# print(e_RuntimeError)

# try:
#     print("And now, the Vocational Guidance Counsellor Sketch.")
#     raise RuntimeError("Does not have proper hat")  # tra ve ngoai le!
#     print(
#         "This print statement will not be reached."
#     )  # dong nay se ko duoc chay boi vi da tra ve exception
# except RuntimeError as problem:  # dua exception vao problem
#     print("Vocation problem: {0}".format(problem))  # hien thi exception
