class chanh:
    name = "chanh"

    def __init__(self, name=None) -> None:
        self.name = name


ten = chanh("Mai Phương")
print("%s <3 %s" % (chanh.name, ten.name))
ten = chanh()
ten.name = "Mai Phương"
print("%s <3 %s" % (chanh.name, ten.name))
