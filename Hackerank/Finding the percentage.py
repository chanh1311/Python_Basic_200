# Nhap n
n = int(input())
# Khoi tao 1 dict rong
dict_input = {}
# vong for nhap du lieu va lay gia tri
for i in range(n):
    name, *scores = input().split()
    # Them cac gia tri vao 1 dict
    dict_input[name] = scores
# Nhap ten can query
query = input()
# xu li
for x in dict_input:
    if x == query:
        result = round(sum(map(float, dict_input[x])) / 3, 2)
# Hien thi ket qua
print("{:.2f}".format(result))


# Đầu vào là 1 số nguyên chỉ số cac diem cua Sinh Vien, các dòng thông tin của số nguyên, tên cần tính điểm trung bình
# 1. Nhập n, gán giá trị cho list theo dữ liệu đầu vào(chú ý điểm lưu kiển interable)dùng vòng for, tên cần tính điểm
# 2. Dùng câu lệnh if tính kết quả theo tên khi duyệt qua dict
# 3. Hiển thị kết quả theo format
