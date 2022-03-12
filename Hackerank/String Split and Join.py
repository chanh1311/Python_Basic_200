def split_and_join(line):
    List = line.split()
    string = "-".join(List)
    return string


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)


# chuyen chuoi cach nhau boi dau phan cach thành dấu gạch nối
# 1. Phân tách chuỗi thành List
# 2. Nối chuỗi thành String cách nhau bởi dấu gạch chéo
# 3. Trả về chuỗi
