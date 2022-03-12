class Shape:
    def __init__(self) -> None:
        self.r = 10

    def Area(self):
        return 0


class Square(Shape):
    def __init__(self, l) -> None:
        super().__init__()
        self.length = l

    def Area(self):
        return self.r * self.length


obj = Square(10)
print(obj.Area())
