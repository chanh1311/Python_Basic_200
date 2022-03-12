n = int(input())
l = list(map(int, input().split()))
if n != len(l):
    print("Dinh dang dau vao khong dung!")
else:
    max_element = max(l)
    while max_element == max(l):
        l.remove(max_element)
    result = max(l)
    print(result)

# Lấy phần tử lớn thứ 2 trong list
# 1. Nhập n, list
# 2. Lấy phần tử lớn nhất đầu tiên
# 3. Vòng lặp while nếu phần tử có trong list bằng phần tử max thì xóa bỏ
# 4. Lấy kết quả của phần tử max(là phần tử lớn thứ 2)
