def nhap():
    x, y, z, n = int(input()), int(input()), int(input()), int(input())

    return x, y, z, n


def list_comprehensions(x, y, z, n):
    list_result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    return list_result


def main():
    x, y, z, n = nhap()
    list_result = list_comprehensions(x, y, z, n)
    print(list_result)


if __name__ == "__main__":
    main()


# Nhập vào 4 tham số là chữ số, Hiển thị danh sách các danh sách chứa phần tử nhỏ hơn các tham số đã cho, sao cho tổng 3 phần tử dó phải khác số thứ 4.
# 1. Nhập 4 tham số
# 2. Tạo 1 list[i,j,k] trong 3 vòng lặp nếu ! so với số thứ 4
# 3. Hiển thị
