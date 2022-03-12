def count_substring(string, sub_string):
    count = 0
    # Nhan ve chuoi tu phan tu dang xet so voi chuoi con
    for i in range(len(string)):
        # Neu ton tai thi tang len 1
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


# Đếm số lần xuất hiện của một chuỗi con trong chuỗi lớn
# Nhập chuỗi con và chuỗi lớn
# Gọi hàm đếm(Tạo biến count, duyệt qua từng phần tử của chuỗi: nếu chuỗi con là bắt đầu trong chuỗi đang xét duyệt thì cộng thêm 1, trả về giá trị)
# Hiển thị
