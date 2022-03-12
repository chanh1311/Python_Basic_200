def mutate_string(string, position, character):
    List = list(string)
    List[position] = character
    result = "".join(List)
    return result


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Nhập vào 1 chuỗi, một vị trí và một kí tự. Thay đổi vị trí thứ i thành kí tự

# 1. Chuyển chuỗi thành list
# 2. Thay đổi vị trí i thành một kí tự
# 3. Dùng join để trả về chuỗi
