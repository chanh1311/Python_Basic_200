class HinhChuNhat:
    def __init__(self, dai, rong) -> None:
        self.dai = dai
        self.rong = rong

    def tinh_DienTich(self):
        DienTich = self.dai * self.rong
        return DienTich


obj = HinhChuNhat(20, 10)
print(obj.tinh_DienTich())
