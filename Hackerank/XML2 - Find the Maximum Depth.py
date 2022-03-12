import xml.etree.ElementTree as etree


maxdepth = 0


def depth(elem, level):
    global maxdepth
    # Kiem tra max
    if level == maxdepth:
        maxdepth += 1
    # Co bao nhieu the con se cong len bay  nhieu lan
    for child in elem:
        depth(child, level + 1)


# Nhap cau truc xml
if __name__ == "__main__":
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# Hiển thị số cấp của thẻ
# 1. Nhập số n, cây thẻ
# 2. Gọi cây thẻ xml để đếm số cấp tối đa ( Khởi tạo biến max, kiểm tra cấp của 1 thẻ nếu bằng max thì cho lên 1, duyệt đệ quy các con của thẻ, kết quả sao cùng là tối đa)
# 3. Hiển thị
