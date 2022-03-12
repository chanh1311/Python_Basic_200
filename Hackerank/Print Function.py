if __name__ == "__main__":
    n = int(input())
    string = ""
    for i in range(1, n + 1):
        string += str(i)
    print(string)
################################
# print(*range(1, int(input()) + 1), sep="")

# Hiển thị chuỗi từ 1 số đã cho
# 1. Nhập số vào
# 2. Tạo 1 chuỗi rỗng
# 3. Cộng chuỗi rỗng cho từng phần tử số để tạo ra chuỗi số
