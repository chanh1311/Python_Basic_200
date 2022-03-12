class MyError(Exception):
    """My own exception class
    # Bài Python 57, Code by Quantrimang.com
         Attributes:
            msg -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


error = MyError("Có gì đó sai sai!")
print(error)
# Class ke thua Exception khi goi doi tuong se hien thi thuoc tinh ra man hinh chu khong phai 1 doi tuong nhu bt

# class test:
#     def __init__(self, t):
#         self.t = t


# obj = test("Hello Minh La Chanh!")

# print(obj)
