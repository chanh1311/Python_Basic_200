n, m = map(int, input().split())
pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
# tao list cac dong tren dong giua //
print("\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1]))
# cong dong giua va in nguoc cac dong tren

# Bài toán hiển thị theo định dạng #
# 1. Nhập vào số dòng và số cột
# 2. Tính ra số kí tự đặt biệt từng dòng thành một công thức
# 3. Tạo định dạng theo dòng, và lặp ra tạo thành 1 list các chuỗi trước Welcome
# 4. Nối chuỗn
